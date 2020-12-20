from discord.ext import commands
from random import randrange


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Enter an even number of players to make random teams of 2", brief="Random Teams of 2")
    async def teams(self, ctx, *args):
        if len(args) != 0 and len(args) % 2 == 0:
            random = []

            index = randrange(len(args))
            for i in range(len(args)):
                while args[index] in random:
                    index = randrange(len(args))
                random.append(args[index])

            team_number = 1
            team_string = ''
            for j in range(0, len(args), 2):
                team_string += "Team {}: {}, {}\n".format(team_number, random[j][:-5], random[j + 1][:-5])
                team_number += 1

            await ctx.send(team_string)

    @commands.command(description="Need I say who?", brief=">:)")
    async def GHOAT(self, ctx):
        await ctx.send("GHOAT: The Greatest Host Of All Time. You know who. 👑")


def setup(bot):
    bot.add_cog(Basic(bot))
