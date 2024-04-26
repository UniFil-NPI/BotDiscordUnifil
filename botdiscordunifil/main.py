from typing import Final

import discord
from discord import Embed
from discord.ext import commands
from discord import app_commands 
import interactions
import time

import os
import datetime

from dotenv import load_dotenv

load_dotenv()
# install discord-py-interactions
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

@bot.tree.command(name="embed")
async def embed_command(interaction: discord.Interaction):
    user = interaction.user
    embed = Embed(title="Embed", color=0x00ff00)
    embed.add_field(name="1", value="1", inline=False)
    embed.add_field(name="2", value="2", inline=True)
    embed.set_footer(text="Fim")
    embed.set_author(name=user.display_name, icon_url=user.display_avatar.url)

    await interaction.response.send_message(embed=embed, ephemeral=False)

@bot.tree.command(name="calendario")
async def calendario_command(interaction: discord.Interaction):
    user = interaction.user
    embed = Embed(title="Calendário de Atividades", color=0x3498db)

    datas = {
        "Programação": datetime.datetime(2024, 5, 5, 15, 30),
        "Back End": datetime.datetime(2024, 5, 12, 14, 00),
        "Front End": datetime.datetime(2024, 5, 19, 16, 45)
    }

    for atividade, data in datas.items():
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
