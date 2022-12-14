import discord
from discord.ext import commands
import random

class ChomSChoice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("\tChomSChoice.py is ready.")

    @commands.command()
    async def chomSChoice(self, ctx, *, question=None):
        print(question)
        if question == None :
            await ctx.send("질문이 없는거 같은데요...?")
            return

        await ctx.send("저의 선택은....")

        with open(".resouces/8_ball.txt", "r", encoding="UTF8") as f :
            random_response = f.readlines()
            response = random.choice(random_response)
        await ctx.send(response)

async def setup(client):
    await client.add_cog(ChomSChoice(client))