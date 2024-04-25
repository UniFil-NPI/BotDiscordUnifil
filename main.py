from typing import Final
import discord
from discord.ext import commands
from discord import app_commands 
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="teste")
async def comando(interaction: discord.Interaction):
    await interaction.response.send_message(f"Usuário {interaction.user.mention} {interaction.user.id} !!!", ephemeral=True)

@bot.tree.command(name="soma")
@app_commands.describe(arg1="primeiro número", arg2="segundo número")
async def soma(interaction: discord.Interaction, arg1: int, arg2: int):
    await interaction.response.send_message(f"A soma é de: {arg1 + arg2} !!!", ephemeral=True)

def main():
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
