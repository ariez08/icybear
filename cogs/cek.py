import requests
import datetime
import random
import discord
from discord.ext import commands

time = datetime.datetime.now()
url = "https://pastebin.com/raw/"
pagi = requests.get(url+"2ZNJyFa7").text.split(';')
siang = requests.get(url+"eMaHmi3F").text.split(';')
sore = requests.get(url+"2MHh6tmF").text.split(';')
malam = requests.get(url+"NScPb7hS").text.split(';')

class cek(commands.Cog) :
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is Online")
    
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def cek(self, ctx):
        await ctx.send("Halo ges")

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def siang(self, ctx):
        if 10<time.hour<15:
            await ctx.send(random.choice(siang).strip())
        else :
            await ctx.reply("Sekarang bukan siang atuh")     

    @commands.command(name="!fatah")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def sfsffsf(self, ctx):
        await ctx.reply("Jomblo")

    @commands.command(name="!dimas", aliases=["#dimas","*dimas","di mas"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def aurnrgsg(self, ctx):
        await ctx.reply("Mabar slebew")

async def setup(bot):
    await bot.add_cog(cek(bot))