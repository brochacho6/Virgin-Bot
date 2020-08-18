from random import random
import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print('Bot is Online!')

@client.event
async def on_member_join(member):
    await member.send("Welcome to the Server!")

@client.event
async def on_member_remove(member):
    await member.send('Bye!')


# online message, only terminal side

@client.command(aliases=['nuke', 'purge'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an ammount of messages to delete.')


@client.event
async def on_command_error(ctx, error):
    pass
# chat purge command

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! 🏓 {round(client.latency * 1000)}ms')
#ping command


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
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
#8ball command

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
#kick command

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')
#ban command

client.run('NzQ0OTE0OTc4NDY0ODU4MjA0.XzqKIg.mOwN3yyJZCmkRCxMBb3-0wyxf6U')
