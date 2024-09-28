import discord
import random, os
from discord.ext import commands
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
bot = commands.Bot(command_prefix='.', intents=intents)
# Evento que se activa cuando el bot está listo
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
# Comando simple
@bot.command()
async def hola(ctx):
    await ctx.send('¡Hola! ¿Cómo estás?')
@bot.command()
async def chao(ctx):
    await ctx.send('Adios, que pases buen dia!')

@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command()
async def memes(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def ja(ctx, count_heh = 5):
    await ctx.send("ja" * count_heh)

bot.run("TOKEN")
