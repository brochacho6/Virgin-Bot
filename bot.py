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

@client.command()
async def ping(ctx):
    pingEmbed = discord.Embed(
        colour=discord.Colour.red()
    )
    pingEmbed.set_author(name=f'Pong! 🏓 {round(client.latency * 1000)}ms',
                         icon_url="https://cdn.discordapp.com/attachments/744916487801929811/745424638795972728/firefox_6Zw1KYZS2b.png")
    await ctx.send(embed=pingEmbed)


@client.command()
async def stats(ctx):
    pythonVersion = platform.python_version()
    dpyVersion = discord.__version__
    serverCount = len(client.guilds)
    memberCount = len(set(client.get_all_members()))
    await ctx.send(
        f"Bot Stats:\nI'm in {serverCount} servers with a total of {memberCount} members. :sunglasses:\nI'm running Python {pythonVersion} and discord.py {dpyVersion}.")



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
