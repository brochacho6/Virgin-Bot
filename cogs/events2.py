import discord
import json
from discord.ext import commands

async def is_guild_owner(ctx):
    return ctx.author.id == ctx.guild.owner.id

class Events2(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check(is_guild_owner)
    async def prefix(self, ctx, *, pre):
        with open(r"C:\Users\gcpsa\PycharmProjects\Virgin-Bot\prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = pre
        await ctx.send(f"New prefix is `{pre}`")

        with open(r"C:\Users\gcpsa\PycharmProjects\Virgin-Bot\prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)



def setup(client):
    client.add_cog(Events2(client))