from requests.models import parse_header_links
import discord
from discord.ext import commands
import configparser
import codecs
import asyncio
import aiohttp
import random
import requests
import datetime
import json
import os
import time
import secrets
import subprocess
import shutil
import base64 as b64
import googletrans
import string
from googletrans import Translator
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth



headers = {
  "user-agent": "botcommand (by roothefox on e621)"
}

minimum_int, maximum_int = 0, 100000

config = configparser.ConfigParser()

config.read('auth.ini')
e6User = config['AUTH']['e6User']
e6Key = config['AUTH']['e6Key']

client = commands.Bot(command_prefix='roo!', case_insensitive=True)

client.remove_command('help')


@client.event
async def on_ready():
	guild_count = 0

	for guild in client.guilds:
		print(f"- {guild.id} (name: {guild.name})")

		guild_count = guild_count + 1

		print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

compliments = [
'Your positivity is infectious.',
'You should be so proud of yourself.',
'You’re amazing!',
'You’re a true gift to the people in your life.',
'You’re an incredible person.',
'Your smile makes me smile.',
'Thank you for being such a great person.',
'You are such a good listener.',
'You have a remarkable sense of humor.',
'Thanks for being you!',
'You set a great example for everyone around you.',
'Your smile is contagious.',
'I bet you make babies smile.',
'You have the best laugh.',
'You light up the room.',
'You have a great sense of humor.'
'If cartoon bluebirds were real, a couple of themem would be sitting on your shoulders singing right now.',
'Youre like sunshine on a rainy day.'
]

snuggles = [
'https://tenor.com/view/cat-love-huge-hug-big-gif-11990658',
'https://tenor.com/view/peach-goma-new-and-sleep-gif-20279656',
'https://tenor.com/view/milk-and-mocha-milk-mocha-blanket-cuddle-blanket-gif-18522891'
]

pokemon = [
'001	\#001	Bulbasaur	Grass	Poison',
'\#002	\#002	Ivysaur	Grass	Poison',
'\#003	\#003	Venusaur	Grass	Poison',
'\#004	\#004	Charmander	Fire',
'\#005	\#005	Charmeleon	Fire',
'\#006	\#006	Charizard	Fire	Flying',
'\#007	\#007	Squirtle	Water',
'\#008	\#008	Wartortle	Water',
'\#009	\#009	Blastoise	Water',
'\#010	\#010	Caterpie	Bug',
'\#011	\#011	Metapod	Bug',
'\#012	\#012	Butterfree	Bug	Flying',
'\#013	\#013	Weedle	Bug	Poison',
'\#014	\#014	Kakuna	Bug	Poison',
'\#015	\#015	Beedrill	Bug	Poison',
'\#016	\#016	Pidgey	Normal	Flying',
'\#017	\#017	Pidgeotto	Normal	Flying',
'\#018	\#018	Pidgeot	Normal	Flying',
'\#019	\#019	Rattata	Normal',
'\#019	Rattata	Dark	Normal',
'\#020	\#020	Raticate	Normal',
'\#020	Raticate	Dark	Normal',
'\#021	\#021	Spearow	Normal	Flying',
'\#022	\#022	Fearow	Normal	Flying',
'\#023	\#023	Ekans	Poison',
'\#024	\#024	Arbok	Poison',
'\#025	\#025	Pikachu	Electric',
'\#026	\#026	Raichu	Electric',
'\#026	Raichu	Electric	Psychic',
'\#027	\#027	Sandshrew	Ground',
'\#027	Sandshrew	Ice	Steel',
'\#028	\#028	Sandslash	Ground',
'\#028	Sandslash	Ice	Steel',
'\#029	\#029	Nidoran♀	Poison',
'\#030	\#030	Nidorina	Poison',
'\#031	\#031	Nidoqueen	Poison	Ground',
'\#032	\#032	Nidoran♂	Poison',
'\#033	\#033	Nidorino	Poison',
'\#034	\#034	Nidoking	Poison	Ground',
'\#035	\#035	Clefairy	Fairy',
'\#036	\#036	Clefable	Fairy',
'\#037	\#037	Vulpix	Fire',
'\#037	Vulpix	Ice',
'\#038	\#038	Ninetales	Fire',
'\#038	Ninetales	Ice	Fairy',
'\#039	\#039	Jigglypuff	Normal	Fairy',
'\#040	\#040	Wigglytuff	Normal	Fairy',
'\#041	\#041	Zubat	Poison	Flying',
'\#042	\#042	Golbat	Poison	Flying',
'\#043	\#043	Oddish	Grass	Poison',
'\#044	\#044	Gloom	Grass	Poison',
'\#045	\#045	Vileplume	Grass	Poison',
'\#046	\#046	Paras	Bug	Grass',
'\#047	\#047	Parasect	Bug	Grass',
'\#048	\#048	Venonat	Bug	Poison',
'\#049	\#049	Venomoth	Bug	Poison',
'\#051	\#051	Dugtrio	Ground',
'\#051	Dugtrio	Ground	Steel',
'\#052	\#052	Meowth	Normal',
'\#052	Meowth	Dark',
'\#052	Meowth	Steel',
'\#053	\#053	Persian	Normal',
'\#053	Persian	Dark',
'\#054	\#054	Psyduck	Water',
'\#055	\#055	Golduck	Water',
'\#056	\#056	Mankey	Fighting',
'\#057	\#057	Primeape	Fighting',
'\#058	\#058	Growlithe	Fire',
'\#059	\#059	Arcanine	Fire',
'\#060	\#060	Poliwag	Water',
'\#061	\#061	Poliwhirl	Water',
'\#062	\#062	Poliwrath	Water	Fighting',
'\#063	\#063	Abra	Psychic',
'\#064	\#064	Kadabra	Psychic',
'\#065	\#065	Alakazam	Psychic',
'\#066	\#066	Machop	Fighting',
'\#067	\#067	Machoke	Fighting',
'\#068	\#068	Machamp	Fighting',
'\#069	\#069	Bellsprout	Grass	Poison',
'\#070	\#070	Weepinbell	Grass	Poison',
'\#071	\#071	Victreebel	Grass	Poison',
'\#072	\#072	Tentacool	Tentacool	Water	Poison',
'\#073	\#073	Tentacruel	Water	Poison',
'\#074	\#074	Geodude	Rock	Ground',
'\#074	Geodude	Rock	Electric',
'\#075	\#075	Graveler	Rock	Ground',
'\#075	Graveler	Rock	Electric',
'\#076	\#076	Golem	Rock	Ground',
'\#076	Golem	Rock	Electric',
'\#077	\#077	Ponyta	Fire',
'\#078	\#078	Rapidash	Fire',
'\#078	Rapidash	Psychic	Fairy',
'\#079	\#079	Slowpoke	Water	Psychic',
'\#079	Slowpoke	Psychic',
'\#080	\#080	Slowbro	Water	Psychic',
'\#080	Slowbro	Poison	Psychic',
'\#081	\#081	Magnemite	Electric	Steel',
'\#082	\#082	Magneton	Electric	Steel',
'\#083	\#083	Farfetchd	Normal	Flying',
'\#083	Farfetchd	Fighting',
'\#084	\#084	Doduo	Normal	Flying',
'\#085	\#085	Dodrio	Normal	Flying',
'\#086	\#086	Seel	Water',
'\#087	\#087	Dewgong	Water	Ice',
'\#088	\#088	Grimer	Poison',
'\#088	Grimer	Poison	Dark',
'\#089	\#089	Muk	Poison',
'\#089	Muk	Poison	Dark',
'\#090	\#090	Shellder	Water',
'\#091	\#091	Cloyster	Water	Ice',
'\#092	\#092	Gastly	Ghost	Poison',
'\#093	\#093	Haunter	Ghost	Poison',
'\#094	\#094	Gengar	Ghost	Poison',
'\#095	\#095	Onix	Rock	Ground',
'\#096	\#096	Drowzee	Psychic',
'\#097	\#097	Hypno	Psychic',
'\#098	\#098	Krabby	Water',
'\#099	\#099	Kingler	Water',
'\#100	\#100	Voltorb	Electric',
'\#101	\#101	Electrode	Electric',
'\#102	\#102	Exeggcute	Grass	Psychic',
'\#103	\#103	Exeggutor	Grass	Psychic',
'\#103	Exeggutor	Grass	Dragon',
'\#104	\#104	Cubone	Ground',
'\#105	\#105	Marowak	Ground',
'\#105	Marowak	Fire	Ghost',
'\#106	\#106	Hitmonlee	Fighting',
'\#107	\#107	Hitmonchan	Fighting',
'\#108	\#108	Lickitung	Normal',
'\#109	\#109	Koffing	Poison',
'\#110	\#110	Weezing	Poison',
'\#110	Weezing	Poison	Fairy',
'\#111	\#111	Rhyhorn	Ground	Rock',
'\#112	\#112	Rhydon	Ground	Rock',
'\#113	\#113	Chansey	Normal',
'\#114	\#114	Tangela	Grass',
'\#115	\#115	Kangaskhan	Normal',
'\#116	\#116	Horsea	Water',
'\#117	\#117	Seadra	Water',
'\#118	\#118	Goldeen	Water',
'\#119	\#119	Seaking	Water',
'\#120	\#120	Staryu	Water',
'\#121	\#121	Starmie	Water	Psychic',
'\#122	\#122	Mr. Mime	Psychic	Fairy',
'\#122	Mr. Mime		Ice	Psychic',
'\#123	\#123	Scyther	Bug	Flying',
'\#124	\#124	Jynx	Ice	Psychic',
'\#125	\#125	Electabuzz	Electric',
'\#126	\#126	Magmar	Fire',
'\#127	\#127	Pinsir	Pinsir	Bug',
'\#128	\#128	Tauros	Tauros	Normal',
'\#129	\#129	Magikarp	Water',
'\#130	\#130	Gyarados	Water	Flying',
'\#131	\#131	Lapras	Water	Ice',
'\#132	\#132	Ditto	Normal',
'\#133	\#133	Eevee	Normal',
'\#134	\#134	Vaporeon	Water',
'\#135	\#135	Jolteon	Electric',
'\#136	\#136	Flareon	Fire',
'\#137	\#137	Porygon	Normal',
'\#138	\#138	Omanyte	Rock	Water',
'\#139	\#139	Omastar	Rock	Water',
'\#140	\#140	Kabuto	Rock	Water',
'\#141	\#141	Kabutops	Rock	Water',
'\#142	\#142	Aerodactyl	Rock	Flying',
'\#143	\#143	Snorlax	Normal',
'\#144	\#144	Articuno		Ice	Flying',
'\#144	Articuno		Psychic	Flying',
'\#145	\#145	Zapdos		Electric	Flying',
'\#145	Zapdos		Fighting	Flying',
'\#146	\#146	Moltres 	Fire	Flying',
'\#146	Moltres		Dark	Flying',
'\#147	\#147	Dratini		Dragon',
'\#148	\#148	Dragonair		Dragon',
'\#149	\#149	Dragonite		Dragon	Flying',
'\#150	\#150	Mewtwo		Psychic',
'\#151	\#151	Mew		Psychic'
]

hugs = [
'https://i.imgur.com/GuADSLm.gif',
'https://i.imgur.com/XEs1SWQ.gif',
'https://i.imgur.com/gSGeZJF.gif',
'https://i.imgur.com/EatYxy1.gif',
'https://i.imgur.com/VgP2ONn.gif',
'https://i.imgur.com/snm8S1B.gif',
'https://i.imgur.com/IoSM9JM.gif',
'https://i.imgur.com/XfFacw5.gif',
'https://i.imgur.com/34Ldmbz.gif',
'https://i.imgur.com/bL9iuEI.gif',
'https://i.imgur.com/RPYNm9o.gif',
'https://i.imgur.com/hgXcoiU.gif',
'https://i.imgur.com/hA9ZNoR.gif',
'https://i.imgur.com/iKPs2AJ.gif',
'https://i.imgur.com/t8Ghkkm.gif',
'https://i.imgur.com/TYkINci.gif',
'https://i.imgur.com/kNHDZBI.gif',
'https://i.imgur.com/YWodUk2.gif'
]


kisslist = [
'https://cdn.discordapp.com/attachments/778958142847451158/803660119518216253/HopefulFabulousKouprey-size_restricted.gif',
'https://cdn.discordapp.com/attachments/778958142847451158/803660117416869988/1562542794.recurrent_exilefox-couples-animated-icons.gif',
'https://cdn.discordapp.com/attachments/778958142847451158/803660116255703040/tenor.gif',
'https://cdn.discordapp.com/attachments/778958142847451158/803660115872841728/WVSwvm6.gif',
'https://cdn.discordapp.com/attachments/778958142847451158/803660110651195412/e34e31123f8f35d5c771a2d6a70bef52.gif',
'https://cdn.discordapp.com/attachments/778958142847451158/803660104917450793/anime-kiss-m.gif',
'https://cdn.discordapp.com/attachments/778958142847451158/803660099682959370/tenor_1.gif'
]

baguette = [
'yes',
'no',
'maybe',
'probably',
'i mean, idk',
'SyStEm ErRoR tRy AgAiN',
'wont tell ya',
'sure of it',
'i dont think so',
'most likely',
'probably not bud',
'idk'
]

slaps = [
'https://i.imgur.com/fm49srQ.gif',
'https://i.imgur.com/o2SJYUS.gif',
'https://i.imgur.com/oOCq3Bt.gif'
]

pats = [
'https://i.imgur.com/UWbKpx8.gif',
'https://i.imgur.com/2lacG7l.gif',
'https://i.imgur.com/4ssddEQ.gif',
'https://i.imgur.com/2k0MFIr.gif',
'https://i.imgur.com/nPr3s5D.mp4',
'https://i.imgur.com/LUypjw3.gif',
'https://i.imgur.com/F3cjr3n.gif'
]

boops = [
'https://i.imgur.com/tjko37n.gif',
'https://i.imgur.com/y6JJrpB.gif',
'https://i.imgur.com/kpM9KXa.mp4',
'https://d.facdn.net/art/troutsworth/1488278723/1426280866.troutsworth_boop2.gif'
]

rpss = [
'rock',
'paper',
'scissors'
]

@client.event
async def on_message(message):
	if message.content.lower() == "hello":
		await message.channel.send("hey dirtbag")

	await client.process_commands(message)

@client.event
async def on_member_join(member):
    with open("logs.txt", "a") as logsFile:
        logsFile.write("\n[{}] {} just joined the server".format(datetime.datetime.now(), 
                                                                 member.name))

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))
        await ctx.message.delete()

@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

@client.command(name='ping', pass_context=True)
async def ping(context):
    str(context.message.author), (context.message.channel.name)
    await context.message.channel.send("Pong!")

@client.command(name='kick', pass_context = True)
@commands.has_permissions(kick_members = True)
async def kick(context, member: discord.Member, reason=None):
    str(context.message.author), (context.message.channel.name)
    await member.kick(reason=reason)
    await context.send('User ' + member.display_name + ' has been kicked.')

@client.command(name='ban', pass_context = True)
@commands.has_permissions(kick_members = True, ban_members = True)
async def ban(context, member: discord.Member, *, reason=None):
    str(context.message.author), (context.message.channel.name)
    await member.ban(reason=reason)
    await context.send('User ' + member.display_name + ' has been banned.')

@client.command(name='avatar', pass_context = True)
async def avatar(context, member: discord.Member=None, size = 4096):
    str(context.message.author), (context.message.channel.name)
    if member is None:
        user = context.message.author
        url = user.avatar_url
        await context.message.channel.send(url)
    else:
        url = member.avatar_url
        await context.message.channel.send(url)

@client.command(name='change_nick', pass_context = True)
async def change_nick(context, member: discord.Member, nickname=None):
    str(context.message.author), (context.message.channel.name)
    currentNick = member.nick
    newNick = nickname
    if newNick == None:
        await context.message.channel.send("Operation aborted.")
    else:
        await member.edit(nick=newNick)

@client.command(name='user_count', pass_context = True)
async def memberCount(context):
    str(context.message.author), (context.message.channel.name)
    guild = context.message.author.guild
    usercount = guild.member_count
    await context.message.channel.send("members: " + str(usercount))

@client.command(name='rn', pass_context=True)
async def rn (context):
    str(context.message.author), (context.message.channel.name)
    await context.message.channel.send(random.randint(1, 1000))

@client.command(name= 'hug', pass_context = True)
async def hug (context, member: discord.Member):
    str(context.message.author), (context.message.channel.name)
    huggles = discord.Embed(title='huggies')
    huggles.add_field(name= f'{context.message.author} hugged', value=f'{member.name}')

    random_link = secrets.choice(hugs)

    huggles.set_image(url= random_link)
    await context.message.channel.send(embed = huggles)

@client.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@client.command(name= 'kiss', pass_context = True)
async def kiss (context, member: discord.Member):
    str(context.message.author), (context.message.channel.name)
    kissles = discord.Embed(title='did you just kissy?')
    kissles.add_field(name= f'{context.message.author} kissed', value=f'{member.name}')

    randomlink = secrets.choice(kisslist)

    kissles.set_image(url= randomlink)
    await context.message.channel.send(embed = kissles)

@client.command(name="cute", pass_context = True)
async def cuteCheck(context, member: discord.Member):
    str(context.message.author), (context.message.channel.name)
    cute = random.randint(0, 100)
    await context.message.channel.send(f'{member.name} is {cute}% cute.')

@client.command(name="post", pass_context = True)
async def post(context, postID=None):
    str(context.message.author), (context.message.channel.name) 
    if postID == None:
        await context.message.channel.send('Please make sure you specify a post ID!')
    elif postID == 'random':
        rq = requests.get(f'https://e621.net/posts/random.json?', headers=headers, auth=('roothefox', f'{e6Key}'))
        rqJSON = rq.json()
    else:
        rq = requests.get(f'https://e621.net/posts/{postID}.json', headers=headers, auth=('roothefox', f'{e6Key}'))
        rqJSON = rq.json()

        keyerror = False
        postid = rqJSON['post']['id']

        try:
            score = rqJSON['post']['score']['total']
        except KeyError:
            keyerror = True
        
        if keyerror:
            await context.message.channel.send('Invalid ID!')
        
        else:
            artist = rqJSON['post']['tags']['artist']
            url = rqJSON['post']['sample']['url']

            if url == None:
                await context.message.channel.send('This post was deleted from e6.')
            else:
                if rqJSON['post']['rating'] == 'e' and (context.channel.is_nsfw()) == False:
                    await context.message.channel.send('Explicit images are not allowed here.')
                    
                elif rqJSON['post']['rating'] == 'e' and (context.channel.is_nsfw()) == True:
                    postEmbed = discord.Embed(title=f'e621 | Post: {postid} | Score: {score} | Artist: {artist[0]}')
                    postEmbed = postEmbed.set_image(url=url)

                    try:
                        await context.message.channel.send(embed=postEmbed)
                    except discord.errors.HTTPException:
                        await context.message.channel.send("400 Bad Request!")

                elif rqJSON['post']['rating'] == 's':
                    postEmbed = discord.Embed(title=f'e621 | Post: {postid} | Score: {score} | Artist:{artist[0]}')
                    postEmbed = postEmbed.set_image(url=url)

                    try:
                        await context.message.channel.send(embed=postEmbed)
                    except discord.errors.HTTPException:
                        await context.message.channel.send("400 Bad Request!")

@client.command(name= "eightball", pass_context=True)
async def eightball(context, text=None):
    str(context.message.author), (context.message.channel.name)
    if text == None:
        await context.message.channel.send('please provide a message so i can give you an answer UwU')
    else:
        randomthing = secrets.choice(baguette)
        await context.message.channel.send(randomthing)

@client.command(name='cringe', pass_context=True)
async def cringe (context):
    str(context.message.author), (context.message.channel.name)
    await context.message.channel.send('fortnite') 

@client.command(name= 'randompokemon', pass_context=True)
async def randompokemon(context):
    str(context.message.author), (context.message.channel.name)
    pokemoon = secrets.choice(pokemon)
    await context.message.channel.send(pokemoon)

@client.command(name = 'invite', pass_context=True)
async def invite (context):
        join = discord.Embed(name='join')
        join.add_field(name='click below to invite the bot\nIm in ' + str(len(client.guilds)) + ' servers', value='[invite](https://discord.com/api/oauth2/authorize?client_id=675609879083483136&permissions=0&scope=bot)')
        join.set_image(url= 'https://cdn.discordapp.com/avatars/675609879083483136/7b1342f2946db02d9d0f23a0819e0091.webp?size=1024')

        await context.message.channel.send(embed = join)

@client.command(name = 'help',pass_context=True)
async def help(context):
    str(context.message.author), (context.message.channel.name)
    helps = discord.Embed(title='bot command information')
    helps = helps.add_field(name= 'what can i help you with today?', value= 'basic commands = roo!helpbasic\naction commands = roo!helpaction\nmoderation commands = roo!helpmod\nrandom commands = roo!helprandom')

    await context.message.channel.send(embed = helps)

@client.command(name= 'helpbasic', pass_context=True)
async def helpbasic (context):
    str(context.message.author), (context.message.channel.name)
    basichelp = discord.Embed(title= 'basic commands list')
    basichelp = basichelp.add_field(name= 'here are some basic commands', value= 'roo!help = Help command\nroo!invite = sends an invite link\nroo!user_count = allows you to see the amount of users are in your server\nroo!avatar = sends a picture of your/mentioned users awatar\nroo!post = sends a post from e621 with a specific post id(NSFW content only in NSFW channels)\nroo!cute = tells you how cute a mentioned user is\nroo!eightball = simply an 8ball command lol', inline=False)

    await context.message.channel.send(embed = basichelp)

@client.command(name= 'helpmod', pass_context=True)
async def helpmod(context):
    str(context.message.author), (context.message.channel.name)
    modhelp = discord.Embed(title= 'moderation commands list')
    modhelp = modhelp.add_field(name= 'here are some moderation commands', value= 'roo!ban = allows you to ban a mentioned user\nroo!change_nick = allows you to change your/someones nickname\nroo!kick = allows you to kick a mentioned user\nmore moderation commands coming soon', inline=False)

    await context.message.channel.send(embed = modhelp)

@client.command(name= 'helpaction', pass_context=True)
async def helpaction (context):
    str(context.message.author), (context.message.channel.name)
    actionhelp = discord.Embed(title= 'action commands list')
    actionhelp = actionhelp.add_field(name= 'here are some action commands', value= 'roo!hug = allows you to hug a mentioned user\nroo!kiss = allows you to kiss a mentioned user\nroo!kill = ig kill someone lol..\nroo!slap = slap... someone for probably no reason at all\nmore action commands like pat coming soon', inline=False)

    await context.message.channel.send(embed = actionhelp)

@client.command(name= 'helprandom', pass_context=True)
async def helprandom(context):
    str(context.message.author), (context.message.channel.name)
    randomhelp = discord.Embed(title= 'random commands list')
    randomhelp = randomhelp.add_field(name= 'here is a list of random commands', value= 'roo!randompokemon = sends a random gen 1 pokemon with a bit of information\nroo!rn = gives you a random number from 1 to 1000', inline=False)

    await context.message.channel.send(embed = randomhelp)

@client.command(name= 'kill', pass_context=True)
async def kill(context, person=None):
    str(context.message.author), (context.message.channel.name)
    if person == None:
        await context.message.channel.send('at least mention someone so i can then disappoint you')
    else:
        await context.message.channel.send('yeah... no')

@client.command(name= 'amibored')
async def amibored(context):
    str(context.message.author), (context.message.channel.name)
    await context.message.channel.send('yes')



@client.command(name= 'slap', pass_context= True)
async def slap(context, member: discord.Member):
    str(context.message.author), (context.message.channel.name)
    slapples = discord.Embed(title= 'why slap?')
    slapples = slapples.add_field (name= f'{context.message.author} slapped', value=f'{member.name}')

    slapers = secrets.choice(slaps)

    slapples = slapples.set_image(url= slapers)
    await context.message.channel.send(embed = slapples)

@client.command(name= 'joinserver', pass_context=True)
async def joinserver(context):
    str(context.message.author), (context.message.channel.name)
    await context.message.channel.send('join the official roo cafe server https://discord.gg/WEpnkCJuxJ')

@client.command(name= 'pat', pass_context=True)
async def pat(context, member: discord.Member):
    str(context.message.author), (context.message.channel.name)
    patties = discord.Embed(title= 'awww you gib pats!!!')
    patties = patties.add_field(name= f'{context.message.author} gave some pats to', value=f'{member.name}')

    paters = secrets.choice(pats)

    patties = patties.set_image(url= paters)

    await context.message.channel.send(embed = patties)

@client.command(name= 'boop', pass_context=True)
async def boop(context, member: discord.Member):
    str(context.message.author), (context.message.channel.name)
    boopers = discord.Embed(title= 'hehehe get booped')
    boopers = boopers.add_field(name=  f'{context.message.author} booped', value=f'{member.name}')

    boopy = secrets.choice(boops)
    boopers = boopers.set_image(url= boopy)

    await context.message.channel.send(embed = boopers)

@client.command(name= 'servers', pass_context=True)
async def servers(context):
    await context.message.channel.send("I'm in " + str(len(client.guilds)) + " servers")

@client.command(aliases=['tr'])
async def translate(context, lang_to, *args):
    str(context.message.author), (context.message.channel.name)
    lang_to = lang_to.lower()
    if lang_to not in googletrans.LANGUAGES and lang_to not in googletrans.LANGCODES:
        raise commands.BadArgument("Invalid language to translate text to")

    text = ' '.join(args)
    translator = googletrans.Translator()
    text_translated = translator.translate(text, dest=lang_to).text
    await context.send(text_translated)

@client.command(name='b64e', pass_context=True)
async def b64e(context):
    str(context.message.author), (context.message.channel.name)
    msg = context.message.content[9:]
    b64msg = b64.b64encode(msg.encode())
    encodeEmbed = discord.Embed(title='Base64 Encoder')
    encodeEmbed.add_field(name='Original message:', value=msg, inline=False)
    encodeEmbed.add_field(name='Encoded message:', value=b64msg.decode(), inline=False)
    await context.message.channel.send(embed=encodeEmbed)

@client.command(name='b64d', pass_context=True)
async def b64e(context):
    str(context.message.author), (context.message.channel.name)
    b64msg = context.message.content[9:]
    msg = b64.b64decode(b64msg.encode())
    encodeEmbed = discord.Embed(title='Base64 Decoder')
    encodeEmbed.add_field(name='Encoded message:', value=b64msg, inline=False)
    encodeEmbed.add_field(name='Original message:', value=msg.decode(), inline=False)
    await context.message.channel.send(embed=encodeEmbed)

@client.command(name='cstatus', pass_context=True)
async def updateCStatus(context):
    str(context.message.author), (context.message.channel.name)
    if context.message.author.id == 274270850830696448:
        original_status = client.guilds[0].get_member(client.user.id).status
        status = context.message.content[12:]
        if status == 'reset':
            await client.change_presence(status=original_status, activity=discord.Game('Living in Spain without the a'))
            await context.message.channel.send('Status successfully reset')
        else:
            await client.change_presence(status=original_status, activity=discord.Game(str(status)))
    else:
        await context.message.channel.send('no')

@client.command(name='ostatus', pass_context=True)
async def updateOStatus(context):
    str(context.message.author), (context.message.channel.name)
    if context.message.author.id == 274270850830696448:
        original_status = client.guilds[0].get_member(client.user.id).activity
        status = context.message.content[12:]
        if status == 'dnd':
            await client.change_presence(status=discord.Status.do_not_disturb, activity=original_status)
        elif status == 'idle':
            await client.change_presence(status=discord.Status.idle, activity=original_status)
        elif status == 'off':
            await client.change_presence(status=discord.Status.invisible, activity=original_status)
        elif status == 'on':
            await client.change_presence(status=discord.Status.online, activity=original_status)
    else:
        await context.message.channel.send('no')

@client.command()
async def rename(context, name):
   str(context.message.author), (context.message.channel.name)
   await client.user.edit(username=name)

@client.command(name= 'ship', pass_context=True)
async def ship(context, member: discord.Member=None):
    num = random.randint(0, 100)

    if member == None:
        await context.message.channel.send("please mention someone so i can find out how much you fit with the other") 
    else:
        ship = discord.Embed(title='love percentage')
        ship.add_field(name= 'command author', value= f'{context.message.author}')
        ship.add_field(name=':RooHug:', value=f'{num}%')
        ship.add_field(name='mentioned user', value=f'{member.name}')

        await context.message.channel.send(embed = ship)

@client.command(name='rps')
async def rps(context, *, message=None):
    rpsss = secrets.choice(rpss)
    msg = 'rock', 'paper', 'scissors'
    if message == None:
        await context.message.channel.send('please choose either rock, paper or scissors')
    else:
        if message.lower() == "rock":
            rock = discord.Embed(name='rock, papaer, scissors')
            rock.add_field(name='you', value=f'{message}')
            rock.add_field(name='VS', value='VS')
            rock.add_field(name='opponent', value=f'{rpsss}')

            await context.send(embed = rock)
            
            time.sleep(1)

            if rpsss == "rock":
                await context.message.channel.send("tie")
            elif rpsss == "paper":
                await context.message.channel.send("you lost!")
            elif rpsss == "scissors":
                await context.message.channel.send("you won!")

        if message.lower() == 'paper':
            paper = discord.Embed(name='rock, papaer, scissors')
            paper.add_field(name='you', value=f'{message}')                
            paper.add_field(name='VS', value='VS')
            paper.add_field(name='opponent', value=f'{rpsss}')

            await context.send(embed = paper)

            time.sleep(1)

            if rpsss == "paper":
                await context.message.channel.send("tie")
            elif rpsss == "scissors":
                await context.message.channel.send("you lost!")
            elif rpsss == "rock":
                await context.message.channel.send("you won!")

        if message.lower() == 'scissors':
            scissors = discord.Embed(name='rock, papaer, scissors')
            scissors.add_field(name='you', value=f'{message}')
            scissors.add_field(name='VS', value='VS')
            scissors.add_field(name='opponent', value=f'{rpsss}')

            await context.send(embed = scissors)

            time.sleep(1)

            if rpsss == "scissors":
                await context.message.channel.send("tie")
            elif rpsss == "rock":
                await context.message.channel.send("you lost!")
            elif rpsss == "paper":
                await context.message.channel.send("you won!")

@client.command(name='gen', pass_context=True)
async def gen(context):

    
    username = ''.join(random.sample(string.ascii_lowercase,16))
    email = username + '@yahoo.com'
    password = ''.join(random.sample(string.ascii_letters,8))
    embeds = discord.Embed(name='account geterator')
    embeds.add_field(name=f'{email}', value=f'{password}')
    
    await context.message.channel.send(embed = embeds)

def scram(content):
    contentL = list(content)
    random.shuffle(contentL)
    content = ''.join(contentL)
    return content

@client.command(name='scramble', pass_context=True)
async def scramble(context):
    ctn = context.message.content[14:]
    newMsg = scram(ctn)
    scramEmbed = discord.Embed(title='Scrambler')
    scramEmbed.add_field(name='Original : ', value=ctn)
    scramEmbed.add_field(name='Scrambled : ', value=newMsg)
    await context.message.channel.send(embed=scramEmbed)

@client.command(name='vote', pass_context=True)
async def vote(context):
    voting = discord.Embed(title='vote')
    voting.add_field(name='vote for our bot at:', value='https://top.gg/bot/675609879083483136\nor https://discordbotlist.com/bots/roo-bot')
    voting.add_field(name='vote for the server at:', value='https://discords.com/servers/776094838511894568')

    await context.message.channel.send(embed = voting)

@client.command(name='compliment', pass_context=True)
async def compliment(context):
    botMsg = await context.message.channel.send('loading compliment')
    await botMsg.edit(content='loading compliment.')
    await botMsg.edit(content='loading compliment..')
    await botMsg.edit(content='loading compliment...')
    await botMsg.edit(content='loading compliment')
    await botMsg.edit(content='loading compliment.')
    await botMsg.edit(content='loading compliment..')
    comp = secrets.choice(compliments)
    await botMsg.edit(content=comp)

bark = [
'woof',
'woof woof',
]

@client.command(name='dog')
async def dog(context):
    barko = secrets.choice(bark)
    await context.message.channel.send(barko)

@client.command(name='vyrix')
async def vyrix(context):
    yesh = discord.Embed(name='Vyrix')
    yesh.add_field(name='invite my besties bot Vyrix', value='[Click here](https://discord.com/api/oauth2/authorize?client_id=802660359760248833&permissions=201452550&scope=bot)')
    yesh.set_image(url = 'https://cdn.discordapp.com/avatars/802660359760248833/a15e939454d242882149384744b927a7.webp?size=1024')

    await context.message.channel.send(embed = yesh)

@client.command(name= 'snuggle', pass_context = True)
async def snuggle (context, member: discord.Member):
    str(context.message.author), (context.message.channel.name)
    snuggies = discord.Embed(title='snuggies')
    snuggies.add_field(name= f'{context.message.author} snuggled', value=f'{member.name}')

    random_link = secrets.choice(snuggles)

    snuggies.set_image(url= random_link)
    await context.message.channel.send(embed = snuggies)



config.read('auth.ini')
token = config['AUTH']['token']

(client.run(token))