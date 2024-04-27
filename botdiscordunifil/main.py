from typing import Final

import discord

from discord.ext import commands
from discord import Embed, app_commands, Button, ButtonStyle

import interactions
import time
import discord.ui

import os
import datetime

from dotenv import load_dotenv

load_dotenv()

intents=discord.Intents.default()
intents.message_content=True

TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} está rodando!')
    try:
        synced = await bot.tree.sync()
        print(f"Foram carregados {len(synced)} comando(s)")
    except Exception as e:
        print(e)

class SelectCourse(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='<', style=discord.ButtonStyle.green, custom_id='left')
    async def left(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.message.edit(embed=self.get_embed("Front End"), view=None)

    @discord.ui.button(label='Back End', style=discord.ButtonStyle.grey, custom_id='materia')
    async def materia(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.message.edit(embed=self.get_embed("Back End"), view=None)

    @discord.ui.button(label='>', style=discord.ButtonStyle.grey, custom_id='right')
    async def right(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.message.edit(embed=self.get_embed("Back End"), view=None)


@bot.tree.command(name="materia")
async def embed_command(interaction: discord.Interaction):
    user = interaction.user
    view = SelectCourse()

    embed = discord.Embed(title="Matérias Disponíveis", color=0x00ff00)
    embed.add_field(name="Front End", value="Professor: X", inline=False)
    embed.add_field(name="Back End", value="Professor: Y", inline=True)
    embed.add_field(name="P.I", value="Professor: Z", inline=True)
    embed.add_field(name="Redes", value="Professor: O", inline=True)
    embed.set_footer(text="Selecione a matéria que deseja visualizar")
    embed.set_author(name=user.display_name, icon_url=user.display_avatar.url)

    await interaction.response.send_message(embed=embed, view=view)

@bot.tree.command(name="calendario")
async def calendario_command(interaction: discord.Interaction):
    user = interaction.user
    embed = discord.Embed(title="Calendário de Atividades", color=0x3498db)

    datas = {
        "Programação": (datetime.datetime(2024, 5, 5, 15, 30), "`PENDENTE`"),
        "Back End": (datetime.datetime(2024, 5, 12, 14, 0), "`ENTREGUE`"),
        "Front End": (datetime.datetime(2024, 5, 19, 16, 45), "`PENDENTE`"),
        "Banco de Dados": (datetime.datetime(2024, 5, 26, 10, 0), "`PENDENTE`"),
        "Redes de Computadores": (datetime.datetime(2024, 6, 2, 13, 15), "`PENDENTE`"),
        "Projeto Interdisciplinar": (datetime.datetime(2024, 6, 9, 16, 30), "`PENDENTE`")
    }

    for atividade, (data, status) in datas.items():
        timestamp_data = f"<t:{int(data.timestamp())}:D>"
        timestamp_relative = f"<t:{int(data.timestamp())}:R>"
        status_note = f" - {status}"  
        
        timestamp_combined = f"{timestamp_data} {timestamp_relative}"

        embed.add_field(name=atividade, value=f"{timestamp_combined}{status_note}", inline=False)

    embed.set_author(name=user.display_name, icon_url=user.display_avatar.url)

    await interaction.response.send_message(embed=embed, ephemeral=False)

@bot.tree.command(name="atividades")
async def calendario_command(interaction: discord.Interaction):
    user = interaction.user
    embed = discord.Embed(title="Atividades Pendentes", color=0x3498db)

    datas = {
        "Aula VUE": (datetime.datetime(2024, 5, 5, 15, 30)),
        "Lista de Exercícios": (datetime.datetime(2024, 5, 12, 14, 0)),
        "Atividade de Redes": (datetime.datetime(2024, 5, 19, 16, 45))
    }

    for atividade, (data) in datas.items():
        timestamp_data = f"<t:{int(data.timestamp())}:D>"
        timestamp_relative = f"<t:{int(data.timestamp())}:R>"
        
        timestamp_combined = f"{timestamp_data} {timestamp_relative}"

        embed.add_field(name=atividade, value=f"{timestamp_combined}", inline=False)

    embed.set_author(name=user.display_name, icon_url=user.display_avatar.url)

    await interaction.response.send_message(embed=embed, ephemeral=False)
def main():
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
