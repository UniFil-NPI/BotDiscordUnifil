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
        
materias = [
    {"nome": "Algoritmos e Estruturas de Dados", "professor": "Professor Exemplo", "descricao": "Introdução aos conceitos fundamentais de algoritmos e estruturas de dados."},
    {"nome": "Programação Orientada a Objetos", "professor": "Professor Exemplo", "descricao": "Princípios e práticas da programação orientada a objetos."},
    {"nome": "Desenvolvimento Web", "professor": "Professor Exemplo", "descricao": "Introdução ao desenvolvimento web usando HTML, CSS e JavaScript."},
    {"nome": "Banco de Dados", "professor": "Professor Exemplo", "descricao": "Conceitos básicos de bancos de dados e linguagem SQL."},
    {"nome": "Inteligência Artificial", "professor": "Professor Exemplo", "descricao": "Fundamentos e aplicações da inteligência artificial."}
]

class SelectCourse(discord.ui.View):  
    def __init__(self):
        super().__init__()
        for materia in materias:
            self.add_item(self.create_button(materia))

    def create_button(self, materia_info):
        materia_nome = materia_info["nome"]
        return self.button_disable(materia_nome)

    class button_disable(discord.ui.Button):  
        def __init__(self, materia_nome):
            super().__init__(label=materia_nome)    
            self.materia_nome = materia_nome

        async def callback(self, interaction: discord.Interaction):
            for materia in materias:
                if materia["nome"].lower() == self.materia_nome.lower():
                    embed = discord.Embed(title=materia["nome"], description=materia["descricao"], color=discord.Color.blue())
                    embed.add_field(name="Professor", value=materia["professor"])
                    await interaction.response.send_message(embed=embed, ephemeral=False)
                    break

@bot.tree.command(name="materia")
async def embed_command(interaction: discord.Interaction):
    user = interaction.user
    view = SelectCourse()

    embed = discord.Embed(title="Matérias Disponíveis", color=0x00ff00)
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
