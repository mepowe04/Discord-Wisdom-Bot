import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("token")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Bot sends a message on channel join and @mentions a specified user
@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            user_id = 99999999999999 # replace with the actual user ID
            user = bot.get_user(user_id)
            await channel.send(f"{user.mention} message here")
            break

@bot.event
async def on_ready():
    print(f'{bot.user} is ready to receive commands')

# Based on who is calling the bot, it will respond with tailored responses taken from a text file. The text files are shuffled on
# open and the responses are randomized

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if not message.content.startswith('!'):
        if (message.author.id == 9999999999999 or message.author.id == 99999999999) and message.channel.id == 999999999999:
            await message.delete()
            file = discord.File("rdlsticker.webp")
            await message.channel.send(file=file)
    await bot.process_commands(message)


with open("wisdom.txt", "r") as f:
    messages = f.read().splitlines()
    random.shuffle(messages)

with open("morgz.txt", "r") as f:
    morgzmessages = f.read().splitlines()
    random.shuffle(morgzmessages)

with open("ebox.txt", "r") as f:
    eboxmessages = f.read().splitlines()
    random.shuffle(eboxmessages)

with open("krak.txt", "r") as f:
    krakmessages = f.read().splitlines()
    random.shuffle(krakmessages)

with open("rdlstock.txt", "r") as f:
    rdlstockmessages = f.read().splitlines()
    random.shuffle(rdlstockmessages)

@bot.command(name='rdl')
async def random_rdlmessage(ctx):
    print("random_message function called")
    if ctx.author == bot.user:
        return
   
    if ctx.author.id == 999999999999999: 
        await ctx.invoke(bot.get_command('morgz'))    
        return
    if ctx.author.id == 999999999999999:
        await ctx.invoke(bot.get_command('ebox'))    
        return
    if ctx.author.id == 999999999999999: 
        await ctx.invoke(bot.get_command('krak'))
        return
    else:    
        message = random.choice(messages)
        await ctx.send(message)

@bot.command(name='morgz')
async def random_morgzmessage(ctx):
    print("random_message function called")
    morgzmessage = random.choice(morgzmessages)
    await ctx.send(morgzmessage)   

@bot.command(name='ebox')
async def random_eboxmessage(ctx):
    print("random_message function called")
    eboxmessage = random.choice(eboxmessages)
    await ctx.send(eboxmessage)   

@bot.command(name='krak')
async def random_krakmessage(ctx):
    print("random_message function called")
    krakmessage = random.choice(krakmessages)
    await ctx.send(krakmessage)       

@bot.command(name='rdlstock')
async def random_stockmessage(ctx):
    print("random_message function called")
    rdlstockmessage = random.choice(rdlstockmessages)
    call_or_put = random.choice(["calls on", "puts on"])
    await ctx.send(f"{call_or_put} {rdlstockmessage}")
 

@bot.command(name='kek')
async def kek_command(ctx):
    await ctx.send("<:kekrdl:1051722129361620992>")

@bot.command(name='icy')
async def icy_command(ctx):
    await ctx.send("<:peepothink:967947942096953405>")

@bot.command(name='ash')
async def ash_command(ctx):
    file = discord.File("rdlash.webp")
    await ctx.send(file=file)


bot.run(token)
