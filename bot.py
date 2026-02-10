import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")  # GitHub Secret

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot {bot.user} ist online!")

@bot.command()
async def test(ctx):
    await ctx.send("Hello from Soba Manager! 🍜")
    
@bot.command()
async def day(ctx):
    await ctx.send("Hello! My first message this day! 🍜")

@bot.command()
async def changes(ctx):
    await ctx.send("We have new changes!🍜")
    
@bot.command()
async def douwantstaff(ctx):
    await ctx.send("Look in #❓apply-for-staff if you want to get @staffed 🍜")

  
@bot.command()
async def custom(ctx):
    await ctx.send("Here are the warnings if you violate the rules 🍜")

  
@bot.command()
async def emo1(ctx):
    await ctx.send(":MangaGirl1")






bot.run(TOKEN)
