import nextcord
from nextcord.ext import commands
import os
# from dotenv import load_dotenv
import random
import json

# load_dotenv()

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
GUILD_ID = 1040237301814546462

bot = commands.Bot(intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    print("online")
    return await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.streaming, name='Foodie Memes'))


@bot.slash_command(name="meme", guild_ids=[GUILD_ID], description="To get a random food related meme")
async def meme(interaction):
    fp = open("links.json")
    data = json.load(fp)
    img_url = random.choice(data['links'])
    embed = nextcord.Embed()
    embed.set_image(url=img_url)
    fp.close()
    await interaction.send(embed=embed)


bot.run(DISCORD_TOKEN)
