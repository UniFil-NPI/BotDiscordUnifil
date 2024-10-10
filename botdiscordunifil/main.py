from typing import List, Tuple, Any, Final
import discord
import asyncio
from discord.ext import commands, tasks
from discord import Embed
import json     
import os
import requests 
from dotenv import load_dotenv
from classroom_api import GoogleClassroomManager
import datetime

import pytz
load_dotenv()
NOTIFICATION_FILE = 'notifications.json'
intents = discord.Intents.default()
intents.message_content = True

TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!", intents=intents)

def get_student_by_discord_id(discord_id):
    try:
        url = f"http://54.198.99.22:8000/students/bydiscord/{discord_id}"
        response = requests.get(url)
        if response.status_code == 200:
            student_data = response.json()
            return student_data
        else:
            return None
    except Exception as e:
        print(f"Erro ao buscar dados do estudante: {e}")
        return None

def load_notification_preferences():
    if os.path.exists(NOTIFICATION_FILE):
        with open(NOTIFICATION_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_notification_preferences(preferences):
    with open(NOTIFICATION_FILE, 'w') as f:
        json.dump(preferences, f)

def set_notification_preference(user_id, enabled):
    preferences = load_notification_preferences()
    preferences[str(user_id)] = enabled
    save_notification_preferences(preferences)

def get_notification_preference(user_id):
    preferences = load_notification_preferences()
    return preferences.get(str(user_id), False)

def get_due_datetime(due_date, due_time):
    timezone_utc = pytz.utc
    timezone_local = pytz.timezone("America/Sao_Paulo")

    naive_datetime = datetime.datetime(
        year=due_date["year"],
        month=due_date["month"],
        day=due_date["day"],
        hour=due_time.get("hours", 0),
        minute=due_time.get("minutes", 0)
    )

    utc_datetime = timezone_utc.localize(naive_datetime)
    localized_datetime = utc_datetime.astimezone(timezone_local)

    return localized_datetime

class Paginator(discord.ui.View):
    def __init__(self, items: List[Any], per_page: int = 1, title: str = "Paginator", formatter: Any = None):
        super().__init__(timeout=None)
        self.items = items
        self.per_page = per_page
        self.page = 0
        self.title = title
        self.formatter = formatter
        self.update_buttons()

    @property
    def max_page(self):
        return (len(self.items) - 1) // self.per_page

    def generate_embed(self):
        embed = discord.Embed(title=self.title, color=0x00ff00)
        start = self.page * self.per_page
        end = start + self.per_page
        for item in self.items[start:end]:
            formatted_item = self.formatter(item)
            embed.add_field(name=formatted_item["title"], value=formatted_item["description"], inline=False)
        embed.set_footer(text=f"Página {self.page + 1} de {self.max_page + 1}")
        return embed

    def update_buttons(self):
        self.children[0].disabled = self.page == 0
        self.children[1].disabled = self.page >= self.max_page

    @discord.ui.button(label="<", style=discord.ButtonStyle.secondary, custom_id='left')
    async def previous_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.page > 0:
            self.page -= 1
        self.update_buttons()
        await interaction.response.edit_message(embed=self.generate_embed(), view=self)

    @discord.ui.button(label=">", style=discord.ButtonStyle.secondary, custom_id='right')
    async def next_page(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.page < self.max_page:
            self.page += 1
        self.update_buttons()
        await interaction.response.edit_message(embed=self.generate_embed(), view=self)

def format_course(course: Any) -> dict:
    return {
        "title": f"{course.name} (ID: {course.id})",
        "description": f'Descrição: {course.course_data.get("descriptionHeading", "Sem descrição")}\nCódigo: {course.course_data.get("enrollmentCode", "Nenhum Código")}'
    }

def format_coursework(coursework: Tuple[str, Any]) -> dict:
    course_name, work = coursework
    due_date = work.get("due_date")
    if due_date:
        due_display = due_date.strftime("%A, %d %B %Y, %H:%M")
    else:
        due_display = "Sem data de entrega"
    return {
        "title": f"{course_name} - {work['title']}",
        "description": f"Data de entrega: {due_display}"
    }

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} está online e sincronizado!')

    try:    
        await main()
        print("Cache carregado com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar o cache: {e}")

    await bot.tree.sync()

    loaded_commands = len(bot.tree.get_commands())
    print(f'{loaded_commands} comandos carregados.')

    if not send_daily_message.is_running():
        send_daily_message.start()

@bot.tree.command(name="materias")
async def courses_command(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)
    
    try:
        student = get_student_by_discord_id(str(interaction.user.id))

        if not student:
            await interaction.followup.send("Você não está registrado.", ephemeral=True)
            return

        email = student.get('email')

        manager = GoogleClassroomManager()
        courses = await manager.get_courses_for_student(email) 

        if not courses:
            await interaction.followup.send("Nenhum curso encontrado ou ocorreu um erro ao acessar a API do Google.", ephemeral=True)
            return

        paginator = Paginator(items=courses, per_page=5, title="Matérias Disponíveis", formatter=format_course)
        embed = paginator.generate_embed()
        await interaction.followup.send(embed=embed, view=paginator, ephemeral=True)
        
    except Exception as e:
        await interaction.followup.send(f"Ocorreu um erro: {e}", ephemeral=True)

@bot.tree.command(name="tarefas")
async def coursework_command(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)
    
    try:
        student = get_student_by_discord_id(str(interaction.user.id))

        if not student:
            await interaction.followup.send("Você não está registrado.", ephemeral=True)
            return

        email = student.get('email')

        manager = GoogleClassroomManager()
        courses = await manager.get_courses_for_student(email)  

        if not courses:
            await interaction.followup.send("Nenhum curso encontrado ou ocorreu um erro ao acessar a API do Google.", ephemeral=True)
            return

        all_coursework = []
        now = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))

        for course in courses:
            coursework = manager.get_coursework(course.id)
            if coursework:
                for work in coursework:
                    due_date = work.get("dueDate")
                    due_time = work.get("dueTime")
                    if due_date and due_time:
                        due_datetime = get_due_datetime(due_date, due_time)
                        if due_datetime > now:
                            work["due_date"] = due_datetime
                            all_coursework.append((course.name, work))

        all_coursework.sort(key=lambda x: x[1].get("due_date"))

        paginator = Paginator(items=all_coursework, per_page=5, title="Atividades Pendentes", formatter=format_coursework)
        embed = paginator.generate_embed()
        await interaction.followup.send(embed=embed, view=paginator, ephemeral=True)
        
    except Exception as e:
        await interaction.followup.send(f"Ocorreu um erro: {e}", ephemeral=True)

@bot.tree.command(name="calendario")
async def calendar_command(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)
    
    try:
        student = get_student_by_discord_id(str(interaction.user.id))

        if not student:
            await interaction.followup.send("Você não está registrado.", ephemeral=True)
            return

        email = student.get('email')

        manager = GoogleClassroomManager()
        courses = await manager.get_courses_for_student(email)

        if not courses:
            await interaction.followup.send("Nenhum curso encontrado ou ocorreu um erro ao acessar a API.", ephemeral=True)
            return

        all_coursework = []
        now = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))

        for course in courses:
            coursework = manager.get_coursework(course.id)
            if coursework:
                for work in coursework:
                    due_date = work.get("dueDate")
                    due_time = work.get("dueTime")
                    if due_date and due_time:
                        due_datetime = get_due_datetime(due_date, due_time)
                        if due_datetime > now:
                            work["due_date"] = due_datetime
                            all_coursework.append((course.name, work))

        all_coursework.sort(key=lambda x: x[1].get("due_date"))

        paginator = Paginator(items=all_coursework, per_page=10, title="Calendário de Atividades", formatter=format_coursework)
        embed = paginator.generate_embed()
        await interaction.followup.send(embed=embed, view=paginator, ephemeral=True)
        
    except Exception as e:
        await interaction.followup.send(f"Ocorreu um erro: {e}", ephemeral=True)

@bot.tree.command(name="notificar")
async def notify_command(interaction: discord.Interaction):
    user_id = interaction.user.id
    current_preference = get_notification_preference(user_id)
    
    new_preference = not current_preference
    set_notification_preference(user_id, new_preference)
    
    if new_preference:
        await interaction.response.send_message("A notificação foi ativada", ephemeral=True)
    else:
        await interaction.response.send_message("A notificação foi desativada", ephemeral=True)

@tasks.loop(minutes=30)
async def update_cache():
    try:
        manager = GoogleClassroomManager()
        await manager.cache_all_data()
        print("Cache atualizado")
    except Exception as e:
        print(f"Erro ao atualizar o cache: {e}")

@tasks.loop(minutes=1)
async def send_daily_message():
    now = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))

    if now.hour == 12 and now.minute == 0:
        preferences = load_notification_preferences() 
        manager = GoogleClassroomManager()  

        for user_id, is_enabled in preferences.items():
            if is_enabled:
                student = get_student_by_discord_id(user_id)
                if not student:
                    continue

                email = student.get('email')

                pending_tasks = await manager.get_student_pendings_by_email(email)
                
                if pending_tasks:
                    user = await bot.fetch_user(int(user_id))
                    if user:
                        message = f"Olá, você tem {len(pending_tasks)} pendência(s) no Google Classroom:\n\n"
                        for task in pending_tasks:
                            due_date = task["due_date"].strftime("%d/%m/%Y")
                            message += f"- {task['coursework_title']} (Vencimento: {due_date})\n"
                        
                        await user.send(message)

async def main():
    try:
        manager = GoogleClassroomManager()
        await manager.cache_all_data()  
        print("Cache carregado com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar o cache: {e}")

if __name__ == '__main__':
    asyncio.run(main())
    bot.run(TOKEN)
