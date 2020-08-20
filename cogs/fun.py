import random
from random import choice, randint
from typing import Optional
from aiohttp import request
from discord import Member, Embed
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import BadArgument
from discord.ext.commands import command, cooldown
import discord
from discord.ext import commands

from bot import blacklist


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun Cog has been loaded")

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        if ctx.author.id in blacklist:
            return
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

    @commands.command()
    async def pvg(self, ctx):
        if ctx.author.id in blacklist:
            return
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

    @commands.command(aliases=['2b2tcopypasta'])
    async def _2b2tcopypasta(self, ctx):
        if ctx.author.id in blacklist:
            return
        pasta = ["*blows vape cloud* smoke weed every day! are you playing constantiam bro? major cringe. yeah i "
                 "joined 2b2t in 2012. *dabs* ew, youre a rusher? brownpill alert. *flips hair* yeah, ive heard of "
                 "fitmc, but have you heard of pekee of 2b2t? *sneers in disgust* no? bluepill alert. well, "
                 "i guess ill see you on the oldest anarchy server in minecraft history!",
                 "DO YOU HAVE ANY IDEA OF HOW MUCH CLOUT I HAVE? HOW MUCH RELEVANCE FLOWS THROUGH MY VETERAN VEINS? "
                 "YOU CANT POSSIBLY DENY ME!",
                 "Only active people are allowed to have an opinion. Maybe you midfags think you're going to even "
                 "become oldfags some day? Well you quit. You're irrelevant if you don't even log in. There are "
                 "newfags with more clout than you, and that redpill is the breakfast of champions. The door didn't "
                 "close on you. It was shut by your own hand. Whenever you want to become relevant again you know "
                 "what to do.",
                 "2b2t.org is the best Minecraft server. You hear my name, and you will know who I am. Everyone knows "
                 "who I am. My name is on the server. It is Popbob. And I'm always online because I have nothing "
                 "better to do. Here, I have autisms. Hausemaster, want to build a base?",
                 "Why you should buy me Priority Queue for 2b2t\nReason 1: I will be your slave on 2b2t. (mine "
                 "echests or something for you, or ez emp for you)\nReason 2: I am a part of the MEG team on 2b2t, "
                 "the MEG is a group (Motorway Extension Gurus) that digs the highways, making it easier for you to "
                 "get around\nReason 3: I am 2b2t deprived. I have not seen the magical world of 2b2t in a week. "
                 "\nReason 4: I cannot afford prio (a.k.a broke boy) \nReason 5: I need prio.",
                 "lisetrn you fucking retarded nigger stop being annoying bitch i can hear you saying that im "
                 "annoting to you and i didnt even talk to you you really need to die irl get cancer bitch\nits "
                 "neared\nfucking bitch die",
                 "I think that all tired with the recents actions of HauseMaster that are influencing in 2b2t.So many hacks were patched, all the 2b2t public dupes were patched, and also Illegals were patched recently forever, and innocent people without doing nothing banned! I'm sure we're all tired with this shit, I have an idea, I think that we must have a better admin, because I think that there're old players that I'm sure that they must be a good admins for 2b2t.\nAlso we must have admins with a better salary, I don't know how many money will earn HauseMaster, but I'm sure there are players that must be admins and they have a better salary than HauseMaster, for have a better queue.\nAlso, HauseMaster is breaking the principal and unic rule in the server ''Anarchy'' the own admin is the only man that is breaking the rules, also I made so many posts about this on reddit talking about this and all of it has been delete inmediately, so we must stop with this shit.\nPlease, this is not a shit post, for me this is a serius post about the HauseMaster actions in 2b2t, because we're all tired with this shit, and we can stop it, so I'm saring with you my opinion about HauseMaster, that I'm sure that so many people are agree and we must have a new Admin, I don't know who can be the new Admin, but I'm sure that there're people better than HauseMaster for have 2b2t.",
                 "So I have been thinking of a concept. “What if everyone got together and cleaned up the server.” In context: From the bedrock to the sky, not a grief in site, reset all the highways. Removed everything that was ever built or mined. Reset the spawn to look like you just spawned in for the very first time on a single player world.\nIf a spawn mason can be built using bots: Spawn Mason\nWhy can’t there be cleanup bots?\nMy opinion: The pros are, I think it would be super cool to watch 2B2T transform back to its original state it would bring new users to the server and I feel a lot of peace would be brought to the world.\nThe cons: I feel like it would take years to do even to do just a single chunk would take months. There is a piece of history threw each grief, to reset everything would be humiliating to the years this server has stayed alive.\nJust a topic for discussion!",
                 "No, I will not. This time is the last time I will ever do anything for you you absolute imbecille. Remember back on point dory? No, that got griefed before you even joined you absolute nomad. Yeah, you're a nomad. Literally worse than jadynplayzmc. Yeah you hear that!? You're so worse yo hablo español. Por qué? For no reason! You speak portugeise that's the reason you fitmc watching, playing monopoly until 3 in the morning, bobpop virgin dupe performing, absolute gnoblin of a constantiam player. Mark my word, and leave it.",
                 "I never actually played 2B2T, but I have heard stories of such server... I would never say that '' 2B2T SHOULD BE REMOVED '' or '' THE SERVER IS FILLED WITH HACKERS. '' even though that last part is sorta true, I don't mind. ( It does have no rules so... ) But I wish to discover the Wonders of this Server, like how it's still alive, how people continued it, The History and the master mind who made it happen... ( Yes I know FitMC covered it, but I wanted to go DEEPER into the story. ) Hell, Maybe one day a child may ask their Grandfather and tell him what he know about 2B2T, and as that child said it... The Grandfather smiled and say '' My Child... Let me tell you the story... Not about 2B2T, Not about the many wars... But the Story how I, Your grandfather used to be King... '' They get onto the computer and the grandfather showed the child photos of the server, and the child asked '' What was your minecraft username Grandpa? '' again the Grandfather smiled and said '' Cryobyte... Not known as the King of many... but the friend of many... ",
                 "Imagine losing so hard that you have to resort to creating obviously fake screenshots to desperately try and make us look bad.\nu can clearly tell it is scripted in a way to make VoCo seem as terrible as possible. If you know the VoCo Execs you also know this is not how we type. And, it says these fake messages were posted ''today'', despite trying to make this look like it took place before our last purge a month ago.\nThe dead giveaway is that Salamander just recently changed to his xmas hat pfp, which they still used even though they were trying to make these messages seem like an old screenshot. If the screenshot was taken before our last purge, Salamander's pfp would be his normal one. But if the screenshot was taken at a later date, it shouldn't show ''today''.\nMaybe try harder next time.",
                 "fuck off man you dont understand THIS GOD DAMN GAME IS ALL I HAVE\n AND YOU FUCKERS RUINED IT!\nFUCK YOU"]
        await ctx.send(f"{random.choice(pasta)}")

    @command(name="slap", aliases=["hit"])
    async def slap_member(self, ctx, member: Member, *, reason: Optional[str] = "for no reason"):
        await ctx.send(f"{ctx.author.display_name} slapped {member.mention} {reason}!")

    @slap_member.error
    async def slap_member_error(self, ctx, exc):
        if isinstance(exc, BadArgument):
            await ctx.send("I can't find that member.")

    @command(name="hello", aliases=["hi"])
    async def say_hello(self, ctx):
        await ctx.send(f"{choice(('Hello', 'Hi', 'Hey', 'Hiya'))} {ctx.author.mention}!")

    @command(name="fact")
    @cooldown(3, 60, BucketType.guild)
    async def animal_fact(self, ctx, animal: str):
        if (animal := animal.lower()) in ("dog", "cat", "panda", "fox", "bird", "koala"):
            fact_url = f"https://some-random-api.ml/facts/{animal}"
            image_url = f"https://some-random-api.ml/img/{'birb' if animal == 'bird' else animal}"

            async with request("GET", image_url, headers={}) as response:
                if response.status == 200:
                    data = await response.json()
                    image_link = data["link"]

                else:
                    image_link = None

            async with request("GET", fact_url, headers={}) as response:
                if response.status == 200:
                    data = await response.json()

                    embed = Embed(title=f"{animal.title()} fact",
                                  description=data["fact"],
                                  colour=ctx.author.colour)
                    if image_link is not None:
                        embed.set_author(name="Powered by some-random-api.ml",
                                              icon_url="https://cdn.discordapp.com/attachments/744916487801929811/745424638795972728/firefox_6Zw1KYZS2b.png")
                        embed.set_image(url=image_link)
                    await ctx.send(embed=embed)

                else:
                    await ctx.send(f"API returned a {response.status} status.")

        else:
            await ctx.send("No facts are available for that animal.")

def setup(client):
    client.add_cog(Fun(client))