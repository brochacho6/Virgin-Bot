import random
import platform
import discord
import json
import os
from discord.ext import commands

client = commands.Bot(command_prefix='$', case_insensitive=True)


@client.event
async def on_ready():
    print('Bot is Online!')
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(name='Virgin and Proud!'))


@client.command(brief = 'Echoes a message (admin only)')
@commands.has_permissions(administrator=True)
async def echo(ctx, *, message=None):
    message = message or "Please provide message to be echo'd"
    await ctx.message.delete()
    await ctx.send(message)


@client.event
async def on_member_join(member):
    await member.send("Welcome to the Server!")


@client.command(aliases=['nuke', 'purge'], brief='Clears a certain ammount of messages (admin only)')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of messages to delete.')


@client.event
async def on_command_error(ctx, error):
    pass


# chat purge command

@client.command(brief="Checks the Bot's Ping", description="Checks the Bot's Ping")
async def ping(ctx):
    await ctx.send(f'Pong! 🏓 {round(client.latency * 1000)}ms')


@client.command(brief= 'Goes beast mode')
async def brownpill(ctx):
    await ctx.send(f"*blows vape cloud* smoke weed every day! are you playing constantiam bro? major cringe. yeah i joined 2b2t in 2012. *dabs* ew, youre a rusher? brownpill alert. *flips hair* yeah, ive heard of fitmc, but have you heard of pekee of 2b2t? *sneers in disgust* no? bluepill alert. well, i guess ill see you on the oldest anarchy server in minecraft history!")

@client.command(brief = "clout")
async def clout(ctx):
    await ctx.send(f"DO YOU HAVE ANY IDEA OF HOW MUCH CLOUT I HAVE? HOW MUCH RELEVANCE FLOWS THROUGH MY VETERAN VEINS? YOU CANT POSSIBLY DENY ME!")


@client.command(brief = "Checks the Bot's statistics")
async def stats(ctx):
    pythonVersion = platform.python_version()
    dpyVersion = discord.__version__
    serverCount = len(client.guilds)
    memberCount = len(set(client.get_all_members()))
    await ctx.send(f"Bot Stats:\nI'm in {serverCount} servers with a total of {memberCount} members. :sunglasses:\nI'm running Python {pythonVersion} and discord.py {dpyVersion}.")

@client.command(aliases = ['quit', 'eject'], brief = "Makes it so the bot cant run commands until its rebooted (admin only)")
@commands.has_permissions(administrator=True)
async def logout(ctx):
    await ctx.send(f'Hey {ctx.author.mention}, I am now logging out :wave:')
    await client.logout()

@logout.error
async def logout_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Hey, you cant do that >:(")


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
                "https://cdn.discordapp.com/emojis/745150242558574743.png?v=1",]
    await ctx.send(f"{random.choice(virginity)}")


@client.command(aliases=['8ball'], brief='Ask the 8ball a question!',description='Ask the 8ball anything and it will randomize 1 out of 20 possible responses.')
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
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


# 8ball command

@client.command(brief='Kicks a member that is mentioned')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


# kick command

@client.command(brief='Bans the user that is mentioned', category='Moderation')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')



client.run('NzQ1MzIyOTM4MTAxNzkyOTAx.XzwGEw.xKauE9JYoJpvObXOUKD4rjJBJzk')
