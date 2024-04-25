from typing import Final
import discord
from discord.ext import commands
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

@bot.command(description="Envia um embed simples")
async def embed(ctx: commands.Context):
    embed = discord.Embed(
        colour = discord.Colour.dark_teal(),
        description="teste",
        title="título", 
    )
    embed.set_footer(text="111")
    embed.set_author(name="Bot")
    
    await ctx.send(embed=embed)

@bot.command(description="teste")  
async def teste(ctx: commands.Context):
    await ctx.send(f"Usuário {ctx.author.mention} {ctx.author.id} !!!", ephemeral=True)

@bot.command(description="Soma dois números")
async def soma(ctx: commands.Context, arg1: int, arg2: int):
    await ctx.send(f"A soma é de: {arg1 + arg2} !!!", ephemeral=True)

bot.run(TOKEN)
