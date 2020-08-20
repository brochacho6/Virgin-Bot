import random
from discord.ext import commands


class _2b2tMemeCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def brownpill(self, ctx):
        await ctx.send(
            f"*blows vape cloud* smoke weed every day! are you playing constantiam bro? major cringe. yeah i joined "
            f"2b2t in 2012. *dabs* ew, youre a rusher? brownpill alert. *flips hair* yeah, ive heard of fitmc, "
            f"but have you heard of pekee of 2b2t? *sneers in disgust* no? bluepill alert. well, i guess ill see you "
            f"on the oldest anarchy server in minecraft history!")

    @commands.command()
    async def clout(self, ctx):
        await ctx.send(
            f"DO YOU HAVE ANY IDEA OF HOW MUCH CLOUT I HAVE? HOW MUCH RELEVANCE FLOWS THROUGH MY VETERAN VEINS? YOU "
            f"CANT POSSIBLY DENY ME!")

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
    client.add_cog(_2b2tMemeCommands(client))
