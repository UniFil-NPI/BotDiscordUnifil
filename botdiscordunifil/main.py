from typing import List, Tuple, Any, Final
import discord
from discord.ext import commands, tasks
from discord import Embed
import json     
import os
from dotenv import load_dotenv
from classroom_api import GoogleClassroomManager
import datetime
import pytz
import random

email_to_discord_id = {
    "gabriel.herculano@edu.unifil.br": "265980379545075712"
}

load_dotenv()
NOTIFICATION_FILE = 'notifications.json'
intents = discord.Intents.default()
intents.message_content = True

TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!", intents=intents)

def get_discord_id_by_email(email):
    return email_to_discord_id.get(email)

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
    await bot.tree.sync()  
    send_daily_message.start()

    loaded_commands = len(bot.tree.get_commands())
    print(f'{loaded_commands} comandos carregados.')

@bot.tree.command(name="materias")
async def courses_command(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)
    try:
        manager = GoogleClassroomManager()
        courses = manager.get_courses()

        if courses is None or not courses:
            await interaction.followup.send("Erro ao acessar a API do Google", ephemeral=True)
            return

        paginator = Paginator(items=courses, per_page=5, title="Matérias Disponíveis", formatter=format_course)
        embed = paginator.generate_embed()
        await interaction.followup.send(embed=embed, view=paginator, ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f"Ocorreu um erro: {e}", ephemeral=True)

@bot.tree.command(name="tarefas")
async def coursework_command(interaction: discord.Interaction, course_id: str):
    await interaction.response.defer(ephemeral=True)
    try:
        manager = GoogleClassroomManager()
        courses = manager.get_courses()
        course = next((course for course in courses if course.id == course_id), None)

        if course is None:
            await interaction.followup.send("Curso não encontrado.", ephemeral=True)
            return

        coursework = manager.get_coursework(course_id)

        if coursework is None or not coursework:
            await interaction.followup.send("Ocorreu um erro ao acessar a API.", ephemeral=True)
            return

        valid_coursework = []
        now = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))

        for work in coursework:
            due_date = work.get("dueDate")
            due_time = work.get("dueTime")
            if due_date and due_time:
                due_datetime = get_due_datetime(due_date, due_time)
                if due_datetime > now:
                    work["due_date"] = due_datetime
                    valid_coursework.append((course.name, work))

        valid_coursework.sort(key=lambda x: x[1].get("due_date"))

        paginator = Paginator(items=valid_coursework, title=f"Atividades de {course.name}", formatter=lambda work: format_coursework(work))
        embed = paginator.generate_embed()
        await interaction.followup.send(embed=embed, view=paginator, ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f"Ocorreu um erro: {e}", ephemeral=True)

@bot.tree.command(name="calendario")
async def calendar_command(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)
    try:
        manager = GoogleClassroomManager()
        courses = manager.get_courses()

        if courses is None or not courses:
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

@bot.tree.command(name="listar_emails")
async def list_emails_command(interaction: discord.Interaction, course_id: str):
    await interaction.response.defer(ephemeral=True)
    try:
        manager = GoogleClassroomManager()
        emails = manager.service.list_student_emails(course_id)

        if emails is None:
            await interaction.followup.send("Erro ao acessar a API do Google ou nenhum aluno encontrado.", ephemeral=True)
            return

        def format_email(email):
            return {
                "title": "Aluno",
                "description": email
            }

        paginator = Paginator(items=emails, per_page=10, title=f"Emails dos alunos da turma {course_id}", formatter=format_email)
        embed = paginator.generate_embed()
        await interaction.followup.send(embed=embed, view=paginator, ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f"Ocorreu um erro: {e}", ephemeral=True)

@bot.tree.command(name="simular_notificacao")
async def simulate_notification_command(interaction: discord.Interaction, email: str, course_id: str):
    await interaction.response.defer(ephemeral=True)
    try:
        manager = GoogleClassroomManager()
        courses = manager.get_courses()

        course = next((c for c in courses if c.id == course_id), None)
        if not course:
            await interaction.followup.send(f"Curso com ID {course_id} não encontrado.", ephemeral=True)
            return

        pending_tasks = await manager.get_student_pendings_by_email(email)

        filtered_tasks = [task for task in pending_tasks if task['course_id'] == course_id]

        if not filtered_tasks:
            await interaction.followup.send(f"Nenhuma pendência encontrada para o aluno com email {email} no curso {course.name}.", ephemeral=True)
            return

        def format_pending(pending):
            due_date = pending["due_date"].strftime("%d/%m/%Y")
            return {
                "title": f"{pending['coursework_title']}",
                "description": f"Curso: {pending['course_name']}\nData de Entrega: {due_date}"
            }

        paginator = Paginator(items=filtered_tasks, per_page=5, title=f"Pendências do Aluno {email} no curso {course.name}", formatter=format_pending)
        embed = paginator.generate_embed()

        user = interaction.user
        await user.send(embed=embed)
        await interaction.followup.send("As pendências foram enviadas para você em uma mensagem direta.", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f"Ocorreu um erro: {e}", ephemeral=True)

@bot.tree.command(name="tarefa_aleatoria")
async def random_task_command(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)
    try:
        manager = GoogleClassroomManager()
        courses = manager.get_courses()

        if courses is None or not courses:
            await interaction.followup.send("Erro ao acessar a API do Google", ephemeral=True)
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

        if not all_coursework:
            await interaction.followup.send("Nenhuma tarefa pendente encontrada.", ephemeral=True)
            return

        selected_task = random.choice(all_coursework)
        embed = discord.Embed(title="Alerta de Pendência", color=0x00ff00)
        embed.add_field(name="Nome da Matéria", value=selected_task[0], inline=False)
        embed.add_field(name="Nome da Atividade", value=selected_task[1]["title"], inline=False)
        description = selected_task[1].get("description", "Sem descrição")
        embed.add_field(name="Descrição", value=description, inline=False)
        
        due_date = selected_task[1].get("due_date", "Sem data de entrega")
        if due_date != "Sem data de entrega":
            due_timestamp = int(due_date.timestamp())
            due_date = f"<t:{due_timestamp}:F>"  
        embed.add_field(name="Data de Vencimento", value=due_date, inline=False)

        user = interaction.user
        await user.send(embed=embed)
        await interaction.followup.send("tste", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f"Ocorreu um erro: {e}", ephemeral=True)

@bot.tree.command(name="listar_pendencias")
async def list_pendings_command(interaction: discord.Interaction, email: str):
    await interaction.response.defer(ephemeral=True)
    try:
        manager = GoogleClassroomManager()
        pendings = await manager.get_student_pendings_by_email(email)

        if not pendings:
            await interaction.followup.send(f"Nenhuma pendência encontrada para o aluno com email {email}.", ephemeral=True)
            return

        def format_pending(pending):
            due_date = pending["due_date"].strftime("%d/%m/%Y")
            return {
                "title": f"{pending['coursework_title']}",
                "description": f"Curso: {pending['course_name']}\nData de Entrega: {due_date}"
            }

        paginator = Paginator(items=pendings, per_page=5, title=f"Pendências do Aluno {email}", formatter=format_pending)
        embed = paginator.generate_embed()

        await interaction.followup.send(embed=embed, view=paginator, ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f"Ocorreu um erro: {e}", ephemeral=True)

@tasks.loop(minutes=1)
async def send_daily_message():
    now = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
    if now.hour == 21 and now.minute == 0:
        channel = bot.get_channel(1210933046014902274)
        if channel:
            await channel.send("Mensagem diária das 21 horas")

def main():
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
