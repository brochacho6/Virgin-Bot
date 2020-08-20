import random

import discord
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain.",

                     "It is decidedly so.",

                     "Without a doubt.",

                     "Yes - definitely.",

                     "You may rely on it.",

                     "As I see it, yes.",

                     "Most likely.",

                     "Outlook good.",

                     "Yes.",

                     "Signs point to yes.",

                     "Reply hazy, try again.",

                     "Ask again later.",

                     "Better not tell you now.",

                     "Cannot predict now.",

                     "Concentrate and ask again.",

                     "Don't count on it.",

                     "My reply is no.",

                     "My sources say no.",

                     "Outlook not so good.",

                     "Very doubtful."]
        _8ballEmbed = discord.Embed(
            colour=discord.Colour.red()
        )
        _8ballEmbed.set_author(name=f'Question: {question}\nAnswer: {random.choice(responses)}')
        await ctx.send(embed=_8ballEmbed)




def setup(client):
    client.add_cog(Fun(client))