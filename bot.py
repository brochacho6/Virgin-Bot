import random
import platform
import discord
import os
import asyncio
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix='$', case_insensitive=True)


@client.event
async def on_ready():
    print('Bot is Online!')
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name='Virgin and Proud!'))


@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# cog commands




# chat purge command

@client.command()
async def ping(ctx):
    pingEmbed = discord.Embed(
        colour=discord.Colour.red()
    )
    pingEmbed.set_author(name=f'Pong! 🏓 {round(client.latency * 1000)}ms',
                         icon_url="https://cdn.discordapp.com/attachments/744916487801929811/745424638795972728/firefox_6Zw1KYZS2b.png")
    await ctx.send(embed=pingEmbed)


@client.command()
async def brownpill(ctx):
    await ctx.send(
        f"*blows vape cloud* smoke weed every day! are you playing constantiam bro? major cringe. yeah i joined 2b2t in 2012. *dabs* ew, youre a rusher? brownpill alert. *flips hair* yeah, ive heard of fitmc, but have you heard of pekee of 2b2t? *sneers in disgust* no? bluepill alert. well, i guess ill see you on the oldest anarchy server in minecraft history!")


@client.command()
async def clout(ctx):
    await ctx.send(
        f"DO YOU HAVE ANY IDEA OF HOW MUCH CLOUT I HAVE? HOW MUCH RELEVANCE FLOWS THROUGH MY VETERAN VEINS? YOU CANT POSSIBLY DENY ME!")


@client.command()
async def stats(ctx):
    pythonVersion = platform.python_version()
    dpyVersion = discord.__version__
    serverCount = len(client.guilds)
    memberCount = len(set(client.get_all_members()))
    await ctx.send(
        f"Bot Stats:\nI'm in {serverCount} servers with a total of {memberCount} members. :sunglasses:\nI'm running Python {pythonVersion} and discord.py {dpyVersion}.")


@client.command()
async def pvg(ctx):
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


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
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


# 8ball command

client.remove_command('help')
@client.command()
async def help(ctx):
    embed = discord.Embed(
        colour=discord.Colour.red(),
        title="Commands",
        description="Displays the purpose of commands."
    )

    embed.set_author(name="Powered by Virgin Bot™",
                     icon_url="https://cdn.discordapp.com/attachments/744916487801929811/745424638795972728/firefox_6Zw1KYZS2b.png")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/744916487801929811/745438993361010768/IMG_20200812_183924.jpg")
    embed.add_field(name="Prefix", value="The prefix for this bot is **$**.", inline=False)
    embed.add_field(name="8ball", value="Ask the 8Ball a question!\nUsage: $8ball [question]", inline=False)
    embed.add_field(name="brownpill", value="Goes Beast-Mode.", inline=False)
    embed.add_field(name="clout", value="Emperor for President 2020.", inline=False)
    embed.add_field(name="ping", value="Checks Bot's ping.", inline=False)
    embed.add_field(name="pvg", value="Holy.", inline=False)
    embed.add_field(name="stats", value="Checks the Bot's Statistics.")
    embed.set_footer(text="Bot Created by brochacho6#4023.",
                     icon_url="https://cdn.discordapp.com/attachments/744916487801929811/745438993361010768/IMG_20200812_183924.jpg")

    await ctx.send(embed=embed)


client.run('NzQ1NDEwMjk5OTgwNDE1MDI2.XzxXcA.NKasQBtJZL5gor_E0cFDEGHj8Dw')
