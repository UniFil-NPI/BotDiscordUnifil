from typing import Final
import discord
from discord.ext import commands
from discord import app_commands 
import os
from dotenv import load_dotenv
from response import get_response  # onde vai ficar o código de resposta

load_dotenv()

TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True  # Necessário para acessar o conteúdo das mensagens

# Inicialize o bot com o prefixo "!" e com todos os intents habilitados
bot = commands.Bot(command_prefix="!", intents=intents)

async def send_message(message: discord.Message, user_message: str) -> None:
    if not user_message:
        print('(Erro)')
        return
    is_private = user_message.startswith("?")
    if is_private:
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e)

@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return

    print(f'[{message.channel}] {message.author}: "{message.content}"')
    await send_message(message, message.content)
    # Importante! Isso permite que o processamento de comandos continue após este evento.
    await bot.process_commands(message)

# Registro dos comandos com barra
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
