import discord
import asyncio

from settings import *
from discord.ext import commands
from random import randrange

bot = commands.Bot(command_prefix="!")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.command(description="React with an balanced number of players to make random teams of your chosen size", brief="xd")
async def rteams(ctx, size):
    embed = discord.Embed(title="Team Maker", description="React with ✅ to enter the random team generator!",
                          color=ctx.author.color)
    embed.set_footer(text="Starting Soon!")

    my_msg = await ctx.send(embed=embed)
    await asyncio.sleep(1)

    await my_msg.add_reaction("✅")

    for i in range(5, -1, -1):
        embed.set_footer(text="Ends in {} seconds!".format(i))
        await asyncio.sleep(1)
        await my_msg.edit(embed=embed)

    embed.set_footer(text="Time's Up!")
    await my_msg.edit(embed=embed)

    new_msg = await ctx.channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    # users.pop(users.index(bot.user))
    size_int = int(size)

    if len(users) != 0 and len(users) % size_int == 0:
        random = []

        index = randrange(len(users))
        for i in range(len(users)):
            while users[index] in random:
                index = randrange(len(users))
            random.append(users[index])

        team_number = 1
        team_string = ''
        for j in range(0, len(users), size_int):
            team_string += "Team {}: ".format(team_number)
            for k in range(j, j + size_int):
                team_string += "{}, ".format(str(random[k])[:-5])
            team_number += 1
            team_string = team_string[:-2]
            team_string += "\n"

        await ctx.send(team_string)


bot.run(DISCORD_BOT_TOKEN)
