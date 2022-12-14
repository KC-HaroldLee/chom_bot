import discord
from discord.ext import commands
import os
import asyncio

client = commands.Bot(command_prefix="$$", intents=discord.Intents.all())

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
        await client.start("MTA1MTg3OTkwMTE1MTY0NTc4OA.GU5aHD.FOH3CUVG3pPnkpPH_Xx5CEqMaz8iaOUhxutZTw")

asyncio.run(main())