from typing import Final
import discord
from discord.ext import commands
from discord import Embed
import os
from dotenv import load_dotenv
from classroom_api import get_classroom_courses  # Importa a função do outro arquivo

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!", intents=intents)

class CoursePaginator(discord.ui.View):
    def __init__(self, courses, per_page=5):
        super().__init__(timeout=None)
        self.courses = courses
        self.per_page = per_page
        self.page = 0
        self.update_buttons()

    @property
    def max_page(self):
        return (len(self.courses) - 1) // self.per_page

    def generate_embed(self):
        embed = discord.Embed(title="Cursos Disponíveis", color=0x00ff00)
        start = self.page * self.per_page
        end = start + self.per_page
        for course in self.courses[start:end]:
            embed.add_field(
                name=course["name"],
                value=f'Descrição: {course.get("descriptionHeading", "Sem descrição")}\nCódigo: {course.get("enrollmentCode", "Nenhum Código")}',
                inline=False
            )
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

@bot.event
async def on_ready():
    print(f'{bot.user} está rodando!')
    try:
        synced = await bot.tree.sync()
        print(f"Foram carregados {len(synced)} comando(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="cursos")
async def courses_command(interaction: discord.Interaction):
    user = interaction.user
    courses = get_classroom_courses()
    
    if courses is None or not courses:
        await interaction.response.send_message("Nenhum curso encontrado ou ocorreu um erro ao acessar a API do Google Classroom.", ephemeral=True)
        return

    paginator = CoursePaginator(courses)
    embed = paginator.generate_embed()
    await interaction.response.send_message(embed=embed, view=paginator, ephemeral=True)

def main():
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
