import discord
from discord.ext import commands
import os
import asyncio

client = commands.Bot(command_prefix="$$", intents=discord.Intents.all())
with open("./token.txt") as token_file :
    token = token_file.readline()


@client.event
async def on_ready():
    print("chom_bot is ready!!")

async def load():
    for filename in os.listdir("./cogs/"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename}"[:-3])

@client.event   
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Error : Missing ...")

async def main():
    async with client:
        await load()
        await client.start(token)

asyncio.run(main())