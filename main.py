import discord
import os
from discord.ext import commands
from discord import FFmpegPCMAudio

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = "!", intents=intents)

@client.event
async def on_ready():
  print ("Arranca el wingBot")

@client.command()
async def adios(ctx):
  await ctx.send("Adiowos")

@client.command()
async def join(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('Komm.wav')
    player = voice.play(source)
    await ctx.send(":)")
  else:
    await ctx.send("no")

@client.command()
async def leave(ctx):
  if(ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("adios")
  else:
    await ctx.send("no")

client.run('secreto')