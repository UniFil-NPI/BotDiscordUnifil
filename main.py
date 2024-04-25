from typing import Final
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')

@slash.slash(name="embed",
             description="Envia um embed simples",
             guild_ids=None) 
async def embed(ctx: SlashContext):
    embed = discord.Embed(
        colour = discord.Colour.dark_teal(),
        description="teste",
        title="título", 
    )
    embed.set_footer(text="111")
    embed.set_author(name="Bot")
    
    await ctx.send(embed=embed)

@slash.slash(name="teste",
             description="Um comando de teste",
             guild_ids=None)  
async def teste(ctx: SlashContext):
    await ctx.send(f"Usuário {ctx.author.mention} {ctx.author.id} !!!", ephemeral=True)

@slash.slash(name="soma",
             description="Soma dois números",
             guild_ids=None, 
             options=[
                 create_option(
                     name="arg1",
                     description="Primeiro número",
                     option_type=4,
                     required=True
                 ),
                 create_option(
                     name="arg2",
                     description="Segundo número",
                     option_type=4,
                     required=True
                 )
             ])
async def soma(ctx: SlashContext, arg1: int, arg2: int):
    await ctx.send(f"A soma é de: {arg1 + arg2} !!!", ephemeral=True)

def main():
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
