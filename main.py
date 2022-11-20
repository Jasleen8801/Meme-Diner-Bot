import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv
import random
import json

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")

bot = commands.Bot(intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    print("online")
    return await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.streaming, name='Foodie Memes'))


@bot.slash_command(name="meme", guild_ids=[GUILD_ID], description="To get a random food related meme")
async def meme(ctx):
    fp = open("links.json")
    data = json.load(fp)
    img_url = random.choice(data['links'])
    embed = nextcord.Embed()
    embed.set_image(url=img_url)
    fp.close()
    await ctx.respond(embed=embed)


bot.run(DISCORD_TOKEN)
