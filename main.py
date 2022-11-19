import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
import json

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("online")
    return await bot.change_presence(activity=discord.Activity(type=1, name='Foodie Meme Lover'))


@bot.command()
async def meme(ctx):
    fp = open("links.json")
    data = json.load(fp)
    img_url = random.choice(data['links'])
    embed = discord.Embed()
    embed.set_image(url=img_url)
    fp.close()
    await ctx.channel.send(embed=embed)


bot.run(DISCORD_TOKEN)
