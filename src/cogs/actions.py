import discord
import os
from discord.ext import commands
import random
import os

class Actions(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    # COMMANDS
    @commands.command(help="Description: Prints a line of text in ascii art")
    async def figlet(self, ctx, *args):
        text = ""
        for arg in args:
            text += " " + arg;
        figletText = os.popen(f"figlet {text}").read()
        await ctx.send(f"```{figletText}```")

    @commands.command(help="Description: Gets random ig post from an ig account")
    async def ig(self, ctx, acct):
        await ctx.send(f"Credit: ig@{acct}", file=discord.File(
            f"../instagram/{acct}/" +
            random.choice(os.listdir(f"../instagram/{acct}/"))
        ))

    @commands.command(help="Gets a random quote")
    async def quote(self, ctx, *persons):
        def __quote(person):
            quotes = open("../" + person + "_quotes.txt").read()
            qs = []
            for q in filter(lambda l: "====================" != l, quotes.splitlines()):
                qs.append(q.replace('[', '').replace(']', '').replace("'", ''))
            return "> " + qs[random.randint(0, len(qs) - 1)] + '\n- ai-' + person

        if len(persons) == 0:
            await ctx.send(__quote("joe"))
        else:
            await ctx.send(__quote(persons[0]))

    @commands.command(help="Learn how to contribute to this bot!")
    async def contribute(self, ctx):
        await ctx.send("Consider Contributing to dbot at: " +
                       "https://github.com/dmaahs2017/discord-bots. Message @Dabrick2017#9824 for help :smiley:")

    @commands.command(help="An emoji")
    async def mood(self, ctx):
        await ctx.send(":tophat:\n:eyes:\n:nose:\n:lips:")
