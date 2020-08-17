import random

import discord
from discord.ext import commands
client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('Bot is Online!')
#online message

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')
#join message

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server!')
#leaving message

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

@client.command(aliases=['nuke', 'purge'])
async def clear(ctx, amount=20):
    await ctx.channel.purge(limit=amount + 1)
#chat purge command

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
#kick command

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')
#ban command

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
#unban command

client.run('NzQ0OTE0OTc4NDY0ODU4MjA0.XzqKIg.mOwN3yyJZCmkRCxMBb3-0wyxf6U')
