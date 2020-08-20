import discord
from discord.ext import commands



class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    # ban command

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return
    # unban command

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    # kick command

    @commands.command(aliases=['quit', 'eject'])
    @commands.is_owner()
    async def logout(self, ctx):
        await ctx.send(f'Hey {ctx.author.mention}, I am now logging out :wave:')
        await self.client.logout()

    @logout.error
    async def logout_error(self,ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("Hey, you cant do that >:(")

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

    # clear command

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
            url="https://cdn.discordapp.com/attachments/744916487801929811/745438993361010768/IMG_20200812_183924.jpg")
        modHelpEmb.add_field(name="echo", value="Makes the bot say anything you want.\nUsage: `$echo [message]`",
                             inline=False)
        modHelpEmb.add_field(name="kick", value="Kicks mentioned user.\nUsage: `$kick @example`", inline=False)
        modHelpEmb.add_field(name="ban", value="Bans mentioned user.\nUsage: `$ban @example`", inline=False)
        modHelpEmb.add_field(name="unban", value="Unbans user.\nUsage: `$unban example#1234`", inline=False)
        modHelpEmb.add_field(name="clear", value="Clears messages.\nUsage: `$clear [ammount of messages]`.", inline=False)
        modHelpEmb.add_field(name="logout",
                             value="Shuts bot down and commands will only become usable again upon a manual restart of the bot.\n⚠️ This command can only be ran by brochacho6. ⚠️",
                             inline=False)
        modHelpEmb.set_footer(text="Bot Created by brochacho6#4023.",
                              icon_url="https://cdn.discordapp.com/attachments/744916487801929811/745438993361010768/IMG_20200812_183924.jpg")

        await ctx.send(embed=modHelpEmb)
    # mod help command


def setup(client):
    client.add_cog(Moderation(client))
