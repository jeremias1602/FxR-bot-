import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

@bot.command()
async def suma(ctx, a: int, b: int):
    await ctx.defer()
    await ctx.send(f"🧮 {a} + {b} = **{a + b}**")

@bot.command()
async def resta(ctx, a: int, b: int):
    await ctx.defer()
    await ctx.send(f"🧮 {a} - {b} = **{a - b}**")

@bot.command()
async def cuatro(ctx):
    await ctx.defer()
    await ctx.send("4️⃣ El número es **4**")

bot.run(os.environ["TOKEN"])
