import platform
import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='$', case_insensitive=True, owner_id=322814668445974529)


@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name} : {client.user.id}')
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name='Virgin and Proud!'))


@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send(
                "Hello! Thanks for adding me to your server!\nThis bot was coded by <@322814668445974529> as a "
                "way to get started in Python.\nTo get started using this bot, this is all you have to "
                "know!: My command prefix is `$` and to look at my commands, any user can do `$help` and "
                "to learn moderator commands, do `$modhelp` (note that both the modhelp command and "
                "moderator commands can only be executed by someone with Administrator permissions.) ")
        break


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
        f"Bot Stats:\nI'm in **{serverCount}** servers with a total of **{memberCount}** members.\nI'm running Python **{pythonVersion}** and discord.py **{dpyVersion}**.")


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
        url="https://cdn.discordapp.com/attachments/744916487801929811/747543601927422013/74a.jpg")
    embed.add_field(name="Prefix", value="The prefix for this bot is **$**.", inline=False)
    embed.add_field(name="8ball", value="Ask the 8Ball a question!\nUsage: $8ball [question]", inline=False)
    embed.add_field(name="ping", value="Checks Bot's ping.", inline=False)
    embed.add_field(name="2b2tcopypasta", value="Sends a random 2b2t Copypasta.", inline=False)
    embed.add_field(name="pvg", value="Holy.", inline=False)
    embed.add_field(name="stats", value="Checks the Bot's Statistics.", inline=False)
    embed.add_field(name="fact", value="Sends random animal fact!\nUsage: `$fact [dog/cat/panda/fox/bird/koala]`",
                    inline=False)
    embed.add_field(name="hello", value="Says hi back to you!", inline=False)
    embed.add_field(name="slap", value="Slaps someone\nUsage: `$slap [user]`", inline=False)
    embed.set_footer(text="Bot Created by brochacho6#4023.",
                     icon_url="https://cdn.discordapp.com/attachments/744916487801929811/745438993361010768/IMG_20200812_183924.jpg")

    await ctx.send(embed=embed)


client.run('NzQ1NDEwMjk5OTgwNDE1MDI2.XzxXcA.NKasQBtJZL5gor_E0cFDEGHj8Dw')
