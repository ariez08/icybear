import asyncio
import os
import discord
from discord.ext import commands
import info as inf

tkn = inf.token
intents=discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="", intents=intents, help_command=None)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.active, activity=discord.Game("Ur Mom"))

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    await bot.start(tkn)

asyncio.run(main())

# @bot.event
# async def on_ready():
#     print("Bot Online")

# @bot.command()
# async def halo(ctx) :
#     await ctx.send("Oi")

# @bot.command()
# async def hai(ctx) :
#     await ctx.reply("Oi")


# class abot(discord.Client) :
#     def __init__ (self):
#         super().__init__(intents=discord.Intents.default())
#         self.synced = False

#     async def on_ready(self) :
#         await bot.change_presence(status=discord.Status.dnd, activity=discord.Game("Ur Mom"))
#         await tree.sync(guild=discord.Object(id="699509549127827516"))
#         self.synced = True
#         print("Tree is Online")

# bot = abot()
# tree = app_commands.CommandTree(bot)

# @tree.command(name="cek", description="Cek status",guild=discord.Object(id="699509549127827516"))
# async def self(interation: discord. Interaction):
#     await interation.response.send_message(f"Assalamualaikum")

# @tree.command(name="ask",description="gives you a answer",guild=discord.Object(id="699509549127827516"))
# async def self(interation: discord. Interaction, question: str):
#     responses = ["As 1 see it, yes." , "Ask again later." , "Better not tell you now." , "cannot predict now. " , "Dont count on it", "It is certain." , "It is decidedly so." , "most likely." , "My reply is no." "outlook not so good." , "outlook good." , "Reply hazy, try again." , "signs point to yes." , "very g definitely.", "Yes You may rely on it.", "Concentrate and ask again ", "My sources say no." , "doubtful." , "without a doubt." ]
#     await interation.response.send_message(f"**Question: ** {question}\n**Answer: ** {random.choice(responses)}")

# bot.run(tkn)