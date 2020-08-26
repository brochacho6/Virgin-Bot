import datetime

import cogs as cogs
import discord
from discord.ext import commands
import platform


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation Cog has been loaded")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

        channel = self.client.get_channel(745893964175114260)
        embed = discord.Embed(
            title=f"{ctx.author.name} banned: {member.name}",
            description=reason
        )
        embed.timestamp = datetime.datetime.utcnow()
        await channel.send(embed=embed)
        print(f"{ctx.author.name} banned: {member.name}")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            banError = discord.Embed(
                colour=discord.Colour.red()
            )
            banError.set_author(name="Please mention a person at the end of the command.",
                                 icon_url="https://cdn.discordapp.com/attachments/744916487801929811/745424638795972728/firefox_6Zw1KYZS2b.png")
            await ctx.send(embed=banError)

    # ban command

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} has been unbanned.')

                channel = self.client.get_channel(745893964175114260)
                embed = discord.Embed(
                    title=f"{ctx.author.name} unbanned: {member.name}",
                )
                embed.timestamp = datetime.datetime.utcnow()
                await channel.send(embed=embed)
                print(f"{ctx.author.name} unbanned: {member.name}")
                return

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            unbanError = discord.Embed(
                colour=discord.Colour.red()
            )
            unbanError.set_author(name="Please add the person's discord user at the end of the command. ($unban Example#1234)",
                                 icon_url="https://cdn.discordapp.com/attachments/744916487801929811/745424638795972728/firefox_6Zw1KYZS2b.png")
            await ctx.send(embed=unbanError)

    # unban command

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.guild.kick(user=member, reason=reason)

        channel = self.client.get_channel(745893964175114260)
        embed = discord.Embed(
            title=f"{ctx.author.name} kicked: {member.name}",
            description=reason
        )
        embed.timestamp = datetime.datetime.utcnow()
        await channel.send(embed=embed)
        print(f"{ctx.author.name} kicked: {member.name}")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            kickError = discord.Embed(
                colour=discord.Colour.red()
            )
            kickError.set_author(name='Please mention a person at the end of the command.',
                                 icon_url="https://cdn.discordapp.com/attachments/744916487801929811/745424638795972728/firefox_6Zw1KYZS2b.png")
            await ctx.send(embed=kickError)

    # kick command

    @commands.command(aliases=['quit', 'eject'])
    @commands.is_owner()
    async def logout(self, ctx):
        logError = discord.Embed(
            colour=discord.Colour.red()
        )
        logError.set_author(name=f'Hey {ctx.author.mention}, I am now logging out :wave:',
                           icon_url="https://cdn.discordapp.com/attachments/744916487801929811/745424638795972728/firefox_6Zw1KYZS2b.png")
        logError.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=logError)

        await self.client.logout()

    @logout.error
    async def logout_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            exError = discord.Embed(
                colour=discord.Colour.red()
            )
            exError.set_author(name="Hey, you can't do that >:^(",
                               icon_url="https://cdn.discordapp.com/attachments/744916487801929811/745424638795972728/firefox_6Zw1KYZS2b.png")
            await ctx.send(embed=exError)

    # logout command

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def echo(self, ctx, *, message=None):
        message = message or "Please provide message to be echo'd"
        await ctx.message.delete()
        await ctx.send(message)

    # echo command

    @commands.command(aliases=['nuke', 'purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)

        nuke = discord.Embed(
            colour=discord.Colour.green()
        )
        nuke.set_author(name=f'{amount} messages deleted',
                        icon_url="https://cdn.discordapp.com/attachments/744916487801929811/745424638795972728/firefox_6Zw1KYZS2b.png")
        nuke.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=nuke)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            nukeError = discord.Embed(
                colour=discord.Colour.red()
            )
            nukeError.set_author(name='Please specify an amount of messages to delete.',
                                 icon_url="https://cdn.discordapp.com/attachments/744916487801929811/745424638795972728/firefox_6Zw1KYZS2b.png")
            await ctx.send(embed=nukeError)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        pass


    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def lockdown(self, ctx, channel: discord.TextChannel=None):
        channel = channel or ctx.channel

        if ctx.guild.default_role not in channel.overwrites:
            overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)
            }
            await channel.edit(overwrites=overwrites)
            await ctx.send(f"```I have put {channel.name} on lockdown.```")
        elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[ctx.guild.default_role].send_messages == None:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send(f"I have put `{channel.name}` on lockdown.")
        else:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send(f"I have removed `{channel.name}` from lockdown.")




    @commands.command()
    @commands.has_permissions(administrator=True)
    async def modHelp(self, ctx):
        modHelpEmb = discord.Embed(
            colour=discord.Colour.orange(),
            title="⚠️ Staff Commands ⚠️",
            description="Displays the purpose of Mod-Only commands."
        )

        modHelpEmb.set_author(name="Powered by Virgin Bot™",
                              icon_url="https://cdn.discordapp.com/attachments/744916487801929811/745424638795972728/firefox_6Zw1KYZS2b.png")
        modHelpEmb.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/744916487801929811/747543601927422013/74a.jpg")
        modHelpEmb.add_field(name="echo", value="Makes the bot say anything you want.\nUsage: `$echo [message]`",
                             )
        modHelpEmb.add_field(name="kick", value="Kicks mentioned user.\nUsage: `$kick @example`", )
        modHelpEmb.add_field(name="ban", value="Bans mentioned user.\nUsage: `$ban @example`", )
        modHelpEmb.add_field(name="unban", value="Unbans user.\nUsage: `$unban example#1234`", )
        modHelpEmb.add_field(name="clear", value="Clears messages.\nUsage: `$clear [ammount of messages]`.",
                             )
        modHelpEmb.add_field(name="mute", value="Mutes a person.\nUsage; `$mute [user]`")
        modHelpEmb.add_field(name="lockdown", value="Makes it so its not possible to send messages in the channel")
        modHelpEmb.add_field(name="userinfo", value="Tells you a bunch of intel about a user\nUsage: `$userinfo [user]`")
        modHelpEmb.add_field(name="logout",
                             value="Shuts bot down and commands will only become usable again upon a manual restart of the bot.\n⚠️ This command can only be ran by brochacho6. ⚠️",
                             inline=False)
        modHelpEmb.set_footer(text="Bot Created by brochacho6#4023.",
                              icon_url="https://cdn.discordapp.com/attachments/744916487801929811/745438993361010768/IMG_20200812_183924.jpg")
        modHelpEmb.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=modHelpEmb)
    # mod help command


def setup(client):
    client.add_cog(Moderation(client))
