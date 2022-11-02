import requests
import datetime
import random
import discord
from discord.ext import commands

time = datetime.datetime.now()
jam = time.hour +7
url = "https://pastebin.com/raw/"

class cek(commands.Cog) :
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cogs is Online")
    
# =========================================
    @commands.command(name="!mention")
    async def sofmsf(self, ctx):
        await ctx.send(ctx.author.mention) #username discord mention
    @commands.command(name="!nama")
    async def sofmsdad(self, ctx):
        await ctx.send(format(ctx.author.display_name)) #Username tanpa mention
    @commands.command(name="!jam")
    async def sofmsdad(self, ctx):
        await ctx.send(jam) #jam
# ========================================

    @commands.command(name="Pagi", aliases=["morning", "Morning", "pagii", "pagi"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def pagi(self, ctx):
        if jam<=10:
            pagi = random.choice(requests.get(url+"2ZNJyFa7").text.split(';')).strip()
            await ctx.send(pagi+" **"+ctx.author.display_name+"**!")
            if 0<jam<3:
                await ctx.reply("Eh buseeet, bukannya tidur kamu")
        else :
            await ctx.reply("Udah bukan pagi lagi atuh bang ╰（‵□′）╯")     

    @commands.command(name="Siang", aliases=["Syang", "syang","siang"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def siang(self, ctx):
        if 10<jam<=15:
            siang = random.choice(requests.get(url+"eMaHmi3F").text.split(';')).strip()
            await ctx.send("Hai **"+ctx.author.display_name+"!** "+siang)
        elif 0<jam<=10:
            await ctx.reply("Masih pagi, jangan buru-buru siang ihh (⊙ˍ⊙)")  
        else :
            await ctx.reply("Siang nya udah bobok, sssttt")

    @commands.command(name="Sore", aliases=["soreh", "Soreh","sore"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def sore(self, ctx):
        if 15<=jam<=18:
            sore = random.choice(requests.get(url+"2MHh6tmF").text.split(';')).strip()
            await ctx.send("Hai **"+ctx.author.display_name+"!** "+sore)
        elif jam<15:
            await ctx.reply("Plis deh... ini tuh belom sore")  
        else :
            await ctx.reply("Sore nya lagi cari kerja")
    
    @commands.command(name="Malam", aliases=["wan an", "Wan","wan", "night","Night", "Guden", "guden","malam"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def malam(self, ctx):
        if 18<=jam:
            malam = random.choice(requests.get(url+"NScPb7hS").text.split(';')).strip()
            await ctx.send("Hai **"+ctx.author.display_name+"!** "+malam)
        elif jam<18:
            await ctx.reply("Kamu habis ngobat ya kak?")  
    
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
