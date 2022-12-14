import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import os
import asyncio
from libs import yt_tools

class Join(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.voice = None
        self.songlist = []
        self.yt_tools = yt_tools.YTTools()

    @commands.Cog.listener()
    async def on_ready(self):
        print("\tjoin.py is ready.")

    @commands.command(pass_context = True)
    async def join(self, ctx):
        if not self.voice == None :
            await ctx.send("저 이미 들아와 있촘")
            return

        elif ctx.author.voice :
            channel = ctx.message.author.voice.channel
            self.voice = await channel.connect()
            await ctx.send("안녕하세요 MIT공대 교수 촘스키 입니촘.")
        else :
            await ctx.send("에러코드 J-j_27")

    @commands.command(pass_context = True)
    async def leave(self, ctx):
        if ctx.author.voice :
            await ctx.guild.voice_client.disconnect()
            self.voice = None
            await ctx.send("촘스키는 자러간다")
        else :
            await ctx.send("저 자는데요")


    @commands.command()
    async def test_play(self, ctx):
        f_loc = "./resouces/too_young_another.mp3"
        print (os.path.isfile(f_loc))
        source = FFmpegPCMAudio(f_loc)
        self.voice.play(source)

    @commands.command()
    async def stop(self, ctx):
        self.voice.stop()

    @commands.command()
    async def play_yt(self, ctx, url):
        try :
            await ctx.message.delete()
            hash_v, yt_title = self.yt_tools.get_file_by_url(url)
            await ctx.send(f"{ctx.author.display_name}이/가 {yt_title}을 재생함")
            f_loc = f"./music/{hash_v}.mp4"
            source = FFmpegPCMAudio(f_loc)
            if self.voice.is_playing() :
                await ctx.send("재생중이던 노래를 멈촘")
                self.voice.stop()
            self.voice.play(source, after=print("노래끝"))
        except Exception as e :
            print(e)

    @commands.command()
    async def add_yt(self, ctx, url):
        await ctx.message.delete()
        hash_v, yt_title = self.yt_tools.get_file_by_url(yt_url=url)
        await ctx.send(f"{ctx.author.display_name}이/가 {yt_title}을 추가함")
        self.songlist.append(hash_v)

        if not self.voice.is_playing() : # 재생중이 아닐경우 재생
            self.play_next()
        
    @commands.command()
    async def my_list(self, ctx, list_idx=0):
        # author_name = ctx.author.name
        author_nick = ctx.author.nick
        author_id = ctx.author.id
        await ctx.send(f"{author_nick}의 리스트")

    async def add_my_list(self, ctx, list_idx=0, url=None):
        pass



    def play_next (self) :

        curr_hash_v = self.songlist.pop(0)
        print("pop 이후",self.songlist)
        f_loc = f"./music/{curr_hash_v}.mp4"
        source = FFmpegPCMAudio(f_loc)
        self.voice.play(source, after=self.play_after_raise)


    def play_after_raise(self, error):
        print("PAR() colled!")
        try:
            fut = asyncio.run_coroutine_threadsafe(self.play_yt(), self.voice.loop)
            fut.result()
        except Exception as e :
            pass

        self.play_next()


async def setup(client):
    await client.add_cog(Join(client))