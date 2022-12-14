import discord
from discord.ext import commands
import random

class MyCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("\tMyCog.py is ready.")

    @commands.command()
    async def embed(self, ctx):
        embed_message = discord.Embed(title="Title of embed", description="디스크립션", color=discord.Color.green())
        
        embed_message.set_author(name=f"{ctx.author.mention}의 요청", icon_url=ctx.author.avatar)
        embed_message.set_thumbnail(url=ctx.guild.icon)
        embed_message.set_image(url=ctx.guild.icon)
        embed_message.add_field(name="필드 네임", value="필드 밸류", inline=False)
        embed_message.set_footer(text="이건 푸터", icon_url=ctx.author.avatar)

        await ctx.send(embed = embed_message)

async def setup(client):
    await client.add_cog(MyCog(client))