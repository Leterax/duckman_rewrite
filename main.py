import discord
from embeds import *
from discord.ext import commands
from secrets import BOT_TOKEN as TOKEN


bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Ready")

@bot.command()
async def help(ctx, arg):
    await ctx.send(embed=await get_help_embed(ctx, arg))

bot.run(TOKEN)