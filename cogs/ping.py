import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("\tPing.py is ready.")

    @commands.command(aliases = ["핑", "핑!", "Ping!", "ping!", "시진핑", "시진핑!"])
    async def ping(self, ctx):
        bot_latnecy = round(self.client.latency * 1000)
        await ctx.send(f"pong! 응답속도{bot_latnecy}ms")


async def setup(client):
    await client.add_cog(Ping(client))