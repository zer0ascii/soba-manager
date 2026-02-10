import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")  # GitHub Secret

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot {bot.user} ist online!")

@bot.command()
async def test(ctx):
    await ctx.send("Hello from Soba Manager! 🍜")

bot.run(TOKEN)
