import discord
import random 
import os 
import requests 
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def saludo(ctx):
    await ctx.send("Hola bienvenido a mi canal de discord!")

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

@bot.command()
async def password(ctx,num:int):
    await ctx.send(f"Tu contraseña es: {gen_pass(num)}")

@bot.command()
async def suma(ctx, num1:int, num2:int):
    resultado = num1 + num2
    await ctx.send(f"El resultado de la suma es: {resultado}")

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@bot.command()
async def ayuda(ctx):
    await ctx.send("Mi bot tiene los siguientes comandos.....")

@bot.command()
async def meme1(ctx):
    with open("imagenes/meme1.jpeg" , "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def memes(ctx):
    nombre_img = random.choice(os.listdir("imagenes"))
    with open(f"imagenes/{nombre_img}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def notas(ctx):
    nombre_img = random.choice(os.listdir("notas"))
    with open(f"notas/{nombre_img}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command()
async def botar(ctx):
    await ctx.send("Los lugares a los que puedes ir a botar tu basura son:")
    await ctx.send("1. Cerca de la calle 24 hay un contedor.")


@bot.command()
async def reciclar(ctx,*, objeto):
    if objeto == "botella de plastico":
        await ctx.send("La botella de plastico la puede convertir en:")
        await ctx.send("En dos macetas si la partes a la mitad:")
        await ctx.send("....")
    if objeto == "cajas de cartos":
        await ctx.send("La botella de plastico la puede convertir en:")
        await ctx.send("En dos macetas si la partes a la mitad:")
        await ctx.send("....")

@bot.command()
async def camion(ctx):
    await ctx.send("El camion de la basura pasa a las: 7pm")

bot.run("")
