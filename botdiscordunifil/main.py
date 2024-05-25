from typing import Final
import discord
from discord.ext import commands
from discord import Embed
import os
import datetime
from dotenv import load_dotenv
from classroom_api import get_classroom_courses  # Importa a função do outro arquivo

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!", intents=intents)

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

    embed = discord.Embed(title="Cursos Disponíveis", color=0x00ff00)
    embed.set_author(name=user.display_name, icon_url=user.display_avatar.url)
    for course in courses:
        embed.add_field(name=course["name"], value=course.get("description", "Sem descrição"), inline=False)
    
    await interaction.response.send_message(embed=embed, ephemeral=True)

def main():
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
