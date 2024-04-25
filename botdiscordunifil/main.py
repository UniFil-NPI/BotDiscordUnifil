from typing import Final
import discord
from discord.ext import commands
from discord_interactions import InteractionClient
from discord_slash.context import MenuContext
from discord_slash.model import ContextMenuType

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)
slash = InteractionClient(bot, test_mode=True)

@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')

@slash.command(description="Envia um embed simples")
async def embed(ctx: MenuContext):
    embed = discord.Embed(
        colour = discord.Colour.dark_teal(),
        description="teste",
        title="título", 
    )
    embed.set_footer(text="111")
    embed.set_author(name="Bot")
    
    await ctx.send(embed=embed)

@slash.command(description="Um comando de teste")  
async def teste(ctx: MenuContext):  
    await ctx.send(f"Usuário {ctx.author.mention} {ctx.author.id} !!!", ephemeral=True)

@slash.command(description="Soma dois números")
async def soma(ctx: MenuContext, arg1: int, arg2: int):
    await ctx.send(f"A soma é de: {arg1 + arg2} !!!", ephemeral=True)

def main():
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
