import discord
import requests
from discord.ext import commands
from vd import get_class

i = discord.Intents.default()
i.message_content = True
bot = commands.Bot(command_prefix="$", intents=discord.Intents.default())


@bot.event
async def on_ready():
    print(f"{bot.user}")


def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachments in ctx.message.attachments:
            F_n = attachments.filename
            F_u = attachments.url
            await attachments.save(F_n)
            await ctx.send(get_class('keras_model.h5', 'labels.txt', F_n))

    else:
        await ctx.send('1')
bot.run("token")
