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

    @commands.command()
    async def pvg(self, ctx):
        virginity = ["https://cdn.discordapp.com/emojis/736080066621997218.png?v=1",
                     "https://cdn.discordapp.com/emojis/717922779659501659.png?v=1",
                     "https://cdn.discordapp.com/emojis/737935384297734194.png?v=1",
                     "https://cdn.discordapp.com/emojis/698308907910562001.png?v=1",
                     "https://cdn.discordapp.com/emojis/686212562022301734.png?v=1",
                     "https://cdn.discordapp.com/emojis/697939921557782579.png?v=1",
                     "https://cdn.discordapp.com/emojis/737935217255514193.png?v=1",
                     "https://cdn.discordapp.com/emojis/738510553428787262.png?v=1",
                     "https://cdn.discordapp.com/emojis/737935704642027521.png?v=1",
                     "https://cdn.discordapp.com/emojis/745150242558574743.png?v=1",
                     "https://cdn.discordapp.com/emojis/745150242558574743.png?v=1", ]
        await ctx.send(f"{random.choice(virginity)}")




def setup(client):
    client.add_cog(Fun(client))