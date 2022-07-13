from requests.models import parse_header_links
import discord
from discord.ext import commands
import configparser
import codecs
import asyncio
import aiohttp
import random
import googletrans
import requests
import datetime
import json
import os
import time
import secrets
import subprocess
import shutil
import base64 as b64
import string
from discord.ext import commands, tasks
from discord.utils import get
from discord import FFmpegPCMAudio
from googletrans import Translator
from discord import TextChannel
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option
import pytz
from datetime import datetime

headers = {
  "user-agent": "botcommand (by roothefox on e621)"
}

minimum_int, maximum_int = 0, 100000

config = configparser.ConfigParser()

config.read('auth.ini')
e6User = config['AUTH']['e6User']
e6Key = config['AUTH']['e6Key']
headersE6 = {'user-agent': f'e621-post-bot (by {e6User} on e621)'}

client = commands.Bot(command_prefix=['roo!', 'r!', 'r.'], case_insensitive=True)
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    print("Roo Bot is in " + str(len(client.guilds)) + " servers")

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
'https://i.imgur.com/wOmoeF8.gif',
'https://i.imgur.com/p2Jt2P5.gif',
'https://i.imgur.com/nrdYNtL.gif',
'https://i.imgur.com/BPLqSJC.gif',
'https://i.imgur.com/ntqYLGl.gif',
'https://i.imgur.com/UMm95sV.gif'

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

emails = [
'@gmail.com',
'@yahoo.com',
'@outlook.com'
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

gay = [
'https://static1.e621.net/data/14/1e/141ee5ac627e36254976a2aa8b67f421.gif',
'https://static1.e621.net/data/f9/9d/f99d58cf4dfbc773d2c425ccc2573449.gif',
'https://static1.e621.net/data/77/dd/77dd5f1d334c881ad21fbd007f22a859.gif',
'https://static1.e621.net/data/9f/a1/9fa1f35bf0f4596cc2660d71a10835ff.gif',
'https://static1.e621.net/data/d2/34/d23494e8aac90efb67a2fecb0bae7afc.gif',
'https://static1.e621.net/data/b7/24/b72487950476054cdb68db27f50bf0dc.gif',
'https://static1.e621.net/data/5d/9d/5d9d03ca4b68671b943fd24039dd58b6.gif',
'https://static1.e621.net/data/43/b4/43b4ac6433d110a4a61fa38db45e32ed.gif',
'https://static1.e621.net/data/6b/70/6b70d187f6add9a79dc690d178b26e16.gif',
'https://static1.e621.net/data/64/3e/643e5ad779fa801e07d70881bbaccad8.gif'
]

straight = [
'https://static1.e621.net/data/de/4d/de4ded88c66afd31e55ba918f8737143.gif',
'https://static1.e621.net/data/55/b3/55b3e1023c25b0f63839b99001580579.gif',
'https://static1.e621.net/data/f7/dc/f7dce7f239cf56f405081172ecac10ca.gif',
'https://static1.e621.net/data/6b/df/6bdf27e9e208629476d94cb5a2fe1476.gif',
'https://static1.e621.net/data/bc/93/bc93f5d40ed465ddaf99d3a958bf57cc.gif',
'https://static1.e621.net/data/4a/bd/4abdacfcda99337911887ed26d5a67a3.gif',
'https://static1.e621.net/data/e4/d9/e4d9d2d3c6eaa9e87f818f50c44e9a93.gif',
'https://static1.e621.net/data/64/1a/641acf2c63ed729527594da161fa8ee0.gif',
'https://static1.e621.net/data/aa/fc/aafc68e6bac81d7265328783df536705.gif'
]

lesbian = [
'https://static1.e621.net/data/36/d1/36d1aec3b183f3cff4e4c4c06c97f121.png',
'https://static1.e621.net/data/b7/c7/b7c74421cfdd5dec3e76e0c5e758715e.gif',
'https://static1.e621.net/data/b3/85/b3850f7cf7433bd213c6252b45d92e10.gif',
'https://static1.e621.net/data/4b/b3/4bb3f60f8f22352ca8995bbb98f98163.gif',
'https://static1.e621.net/data/06/f7/06f79f963dbc79b39a7635f3bb40b8c3.gif',
'https://static1.e621.net/data/40/0c/400cb1eb06a31d7e48a9a7fd361aa8ef.gif',
'https://static1.e621.net/data/b1/00/b1001bdf2b3bd862aeacb9204b51161d.gif',
'https://static1.e621.net/data/dd/d8/ddd86a777e5361b4bffc51e7082fe522.gif',
'https://static1.e621.net/data/a5/c8/a5c8bb47a3578ae673ebd25bf9e7779a.gif',
'https://static1.e621.net/data/82/ea/82ea237d59942e9adf0e7bf704e5251d.gif'
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
'https://static1.e926.net/data/b0/a8/b0a82db8bfc9e34f8339f358926862b1.gif',
'https://static1.e926.net/data/a1/2f/a12fc527519cfa211d8cf0f624e43e4f.gif',
'https://static1.e926.net/data/e6/75/e67586575f6dfd2b7e89c1fbf269684b.gif',
'https://static1.e926.net/data/c4/e0/c4e0e8a236fb3ef68ce1df34fedb766f.gif',
'https://static1.e926.net/data/0f/33/0f33d470edfa6d19e982455fb9f8c48e.gif',
'https://static1.e926.net/data/fe/a7/fea79c2ffeb6a3e47024bfa76539c82d.gif',
'https://static1.e926.net/data/cb/a3/cba363c4a6abdd6641350911f82761f2.gif'
]

rpss = [
'rock',
'paper',
'scissors'
]

@client.event
async def on_message(message):
    await client.change_presence(status=discord.Status.online, activity=discord.Game("in " + str(len(client.guilds)) + " servers, owner: roo fox#0001"))
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

@client.command(name='ping', brief='pong', description='simple pong lol', pass_context=True)
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

blacklisted_tags = [
    "gore",
    "scat",
    "watersports",
    "fart",
    "fart_fetish",
    "fart_cloud",
    "vore",
    "diaper",
    "peeing"
]

def is_valid(tags, ID=False):
    if "cub" in tags or "young" in tags:
        if ID:
            cubEmbed = discord.Embed(title='Command termination.', colour=redColour)
            cubEmbed.add_field(name='Post contains cub tag.', value='Cub is a prohibited tag, this cannot be overridden.')
            return False, cubEmbed
        else:
            return False
    elif any(x in tags for x in blacklisted_tags):
        if ID:
            cubEmbed = discord.Embed(title='Command termination.', colour=redColour)
            cubEmbed.add_field(name='Post contains a blacklisted tag.', value='Default blacklist cannot be overridden.')
            return False, cubEmbed
        return False
    else:
        if ID:
            return True, ""
        return True

@client.command(name="post", pass_context = True)
async def post(context, postID=None):
    senderMsg = context.message
    _is_artist = False
    _isvalid = True
    if postID == None:
        await context.message.channel.send('Please make sure you specify a query! This may be an artist name, post ID, or just a tag, you can chain tags together. For example: canine+male')
    elif postID == 'random':
        rq = requests.get(f'https://e621.net/posts/random.json?', headers=headersE6, auth=(e6User, f'{e6Key}'))
        if rq.status_code == 404:
            pass
        else:
            while not is_valid(rq.json()['post']['tags']['general']):
                rq = requests.get(f'https://e621.net/posts/random.json?', headers=headersE6, auth=(e6User, f'{e6Key}'))
                time.sleep(1)
    elif str(postID).isdigit():
        rq = requests.get(f'https://e621.net/posts/{postID}.json', headers=headersE6, auth=(e6User, f'{e6Key}'))
        if rq.status_code == 404:
            pass
        else:
            isvalid, embed = is_valid(rq.json()['post']['tags']['general'], ID=True)
            if not isvalid:
                _isvalid = False
                await senderMsg.delete()
                await context.message.channel.send(embed=embed)
    else:
        attempted_tags = postID.split('+')
        if any(x in blacklisted_tags for x in attempted_tags):
            await senderMsg.delete()
            BlacklistEmbed = discord.Embed(title='Command termination.', colour=redColour)
            BlacklistEmbed.add_field(name='Post contains a blacklisted tag.', value='Default blacklist cannot be overridden.')
            await context.message.channel.send(embed=BlacklistEmbed)
        else:
            postID = postID.replace(':', '%3A')
            rq = requests.get(f'https://e621.net/posts.json?tags={postID}+order%3Arandom+limit%3A1', headers=headersE6, auth=(e6User, f'{e6Key}'))
            if rq.status_code == 404:
                pass
            else:
                while not is_valid(rq.json()['posts'][0]['tags']['general']):
                    rq = requests.get(f'https://e621.net/posts.json?tags={postID}+order%3Arandom+limit%3A1', headers=headersE6, auth=(e6User, f'{e6Key}'))
                    time.sleep(1)
                _is_artist = True
    if rq.status_code == 200:
        rqJSON = rq.json()

        if _is_artist:
            url = rqJSON['posts'][0]['file']['url']
            md5sum = rqJSON['posts'][0]['file']['md5']
            post = rqJSON['posts'][0]['sample']['url']
            tags = rqJSON['posts'][0]['tags']['general']
            postid = rqJSON['posts'][0]['id']
            artist = rqJSON['posts'][0]['tags']['artist']
            rating = rqJSON['posts'][0]['rating']
            res = f"{rqJSON['posts'][0]['file']['width']}x{rqJSON['posts'][0]['file']['height']}"
        else:
            url = rqJSON['post']['file']['url']
            md5sum = rqJSON['post']['file']['md5']
            post = rqJSON['post']['sample']['url']
            tags = rqJSON['post']['tags']['general']
            postid = rqJSON['post']['id']
            artist = rqJSON['post']['tags']['artist']
            rating = rqJSON['post']['rating']
            res = f"{rqJSON['post']['file']['width']}x{rqJSON['post']['file']['height']}"
        
        if _isvalid:
            ratings = {
                'q': 'Questionable',
                'e': 'Explicit',
                's': 'Safe'
            }
            keyerror = False

            _final_rating = ratings[rating]

            try:
                if _is_artist:
                    score = rqJSON['posts'][0]['score']['total']
                else:
                    score = rqJSON['post']['score']['total']
            except KeyError:
                keyerror = True
            
            if keyerror:
                await context.message.channel.send('Invalid ID!')

            if len(artist) > 1:
                artist = ", ".join(artist)
            elif len(artist) == 1:
                artist = artist[0]
            else:
                artist = 'Not specified.'

            if url == None:
                await context.message.channel.send('This post was deleted from e6.')
            else:
                open_content = f'Open content ({res} {url.split(".")[-1].upper()})'

                if rating == 'e' and not context.channel.is_nsfw():
                    await context.message.channel.send(context, 'Explicit images are not allowed here.')
                    
                elif rating == 'e' or rating == 'q' and context.channel.is_nsfw():
                    postEmbed = discord.Embed(title=f'{open_content}', url=f'{url}')
                    postEmbed.add_field(name='Post stats: ', value=f'Rating: {_final_rating} | Post: {postid} | Score: {score} | Artist(s): {artist}', inline=False)
                    postEmbed = postEmbed.set_image(url=post)

                elif rating == 's':
                    postEmbed = discord.Embed(title=f'{open_content}', url=f'{url}')
                    postEmbed.add_field(name='Post stats: ', value=f'Rating: {_final_rating} | Post: {postid} | Score: {score} | Artist(s): {artist}', inline=False)
                    postEmbed = postEmbed.set_image(url=post)

                postEmbed.set_footer(text=f'MD5sum: {md5sum}')

                try:
                    await context.message.channel.send(embed=postEmbed)
                except discord.errors.HTTPException:
                    await context.message.channel.send("400 Bad Request!")
    
    else:
        await context.message.channel.send(f'Status code {rq.status_code} recieved!')

@slash.slash(name="eightball",
            description="ask a question and i'll answer it")
async def _eightball(context: SlashContext, text=None):
    if text == None:
        await context.send('please provide a message so i can give you an answer UwU')
    else:
        randomthing = secrets.choice(baguette)
        embed = discord.Embed(title='eightball')
        embed.add_field(name='question:', value=f'{text}')
        embed.add_field(name='answer:', value=f'{randomthing}')

        await context.send(embed = embed)

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
        join.add_field(name='click below to invite the bot\nIm in ' + str(len(client.guilds)) + ' servers', value='[invite](https://discord.com/api/oauth2/authorize?client_id=675609879083483136&permissions=8&scope=bot%20applications.commands)')
        join.set_image(url= 'https://cdn.discordapp.com/avatars/675609879083483136/9169e12dc1e32c509a495bb93f1624e9.webp?size=1024')

        await context.message.channel.send(embed = join)

oop = random.randint(1, 1000)

@client.command(name= 'kill', pass_context=True)
async def kill(context, person=None):
    str(context.message.author), (context.message.channel.name)
    if person == None:
        await context.message.channel.send('at least mention someone so i can then disappoint you')
    else:
        await context.message.channel.send('yeah... no')

@client.command(name= 'amibored')
async def amibored(context):
    shit = [
    'yes',
    'no'
    ]

    choose = secrets.choice(shit)

    await context.message.channel.send(choose)

@client.command(name= 'slap', pass_context= True)
async def slap(context, member: discord.Member):
    str(context.message.author), (context.message.channel.name)
    slapples = discord.Embed(title= 'why slap?')
    slapples = slapples.add_field (name= f'{context.message.author} slapped', value=f'{member.name}')

    slapers = secrets.choice(slaps)

    slapples = slapples.set_image(url= slapers)
    await context.message.channel.send(embed = slapples)

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
        elif status == 'mb':
            await client.change_presence(status=discord.Status.online, activity=original_status)
    else:
        await context.message.channel.send('no')

@client.command()
async def rename(context, name):
    if context.message.author.id == 274270850830696448:
        await client.user.edit(username=name)
    else:
        await context.message.channel.send('no')

@client.command(name= 'ship', pass_context=True)
async def ship(context, member: discord.Member=None):
    num = random.randint(0, 100)
    

    if member == None:
        await context.message.channel.send("please mention someone so i can find out how much you fit with the other") 
    else:
        ship = discord.Embed(title='love percentage')
        if num <= 10 and num >= 0:
            ship.add_field(name= 'command author', value= f'{context.message.author}')
            ship.add_field(name=f'{num}%', value='♥♡♡♡♡♡♡♡♡♡')
            ship.add_field(name='mentioned user', value=f'{member.name}')
            await context.message.channel.send(embed = ship)
        elif num <= 20 and num >= 11:
            ship.add_field(name= 'command author', value= f'{context.message.author}')
            ship.add_field(name=f'{num}%', value='♥♥♡♡♡♡♡♡♡♡')
            ship.add_field(name='mentioned user', value=f'{member.name}')
            await context.message.channel.send(embed = ship)
        elif num <= 30 and num >= 21:
            ship.add_field(name= 'command author', value= f'{context.message.author}')
            ship.add_field(name=f'{num}%', value='♥♥♥♡♡♡♡♡♡♡')
            ship.add_field(name='mentioned user', value=f'{member.name}')
            await context.message.channel.send(embed = ship)
        elif num <= 40 and num >= 31:
            ship.add_field(name= 'command author', value= f'{context.message.author}')
            ship.add_field(name=f'{num}%', value='♥♥♥♥♡♡♡♡♡♡')
            ship.add_field(name='mentioned user', value=f'{member.name}')
            await context.message.channel.send(embed = ship)
        elif num <= 50 and num >= 41:
            ship.add_field(name= 'command author', value= f'{context.message.author}')
            ship.add_field(name=f'{num}%', value='♥♥♥♥♥♡♡♡♡♡')
            ship.add_field(name='mentioned user', value=f'{member.name}')
            await context.message.channel.send(embed = ship)
        elif num <= 60 and num >= 51:
            ship.add_field(name= 'command author', value= f'{context.message.author}')
            ship.add_field(name=f'{num}%', value='♥♥♥♥♥♥♡♡♡♡')
            ship.add_field(name='mentioned user', value=f'{member.name}')
            await context.message.channel.send(embed = ship)
        elif num <= 70 and num >= 61:
            ship.add_field(name= 'command author', value= f'{context.message.author}')
            ship.add_field(name=f'{num}%', value='♥♥♥♥♥♥♥♡♡♡')
            ship.add_field(name='mentioned user', value=f'{member.name}')
            await context.message.channel.send(embed = ship)
        elif num <= 80 and num >= 71:
            ship.add_field(name= 'command author', value= f'{context.message.author}')
            ship.add_field(name=f'{num}%', value='♥♥♥♥♥♥♥♥♡♡')
            ship.add_field(name='mentioned user', value=f'{member.name}')
            await context.message.channel.send(embed = ship)
        elif num <= 90 and num >= 81:
            ship.add_field(name= 'command author', value= f'{context.message.author}')
            ship.add_field(name=f'{num}%', value='♥♥♥♥♥♥♥♥♥♡')
            ship.add_field(name='mentioned user', value=f'{member.name}')
            await context.message.channel.send(embed = ship)
        elif num <= 1000 and num >= 91:
            ship.add_field(name= 'command author', value= f'{context.message.author}')
            ship.add_field(name=f'{num}%', value='♥♥♥♥♥♥♥♥♥♥')
            ship.add_field(name='mentioned user', value=f'{member.name}')
            await context.message.channel.send(embed = ship)
        else:
            await context.message.channel.send(f'test {num}')

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

    mailend = secrets.choice(emails)

    username = ''.join(random.sample(string.ascii_lowercase,16))
    email = username + mailend
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
    ctn = context.message.content[13:]
    newMsg = scram(ctn)
    scramEmbed = discord.Embed(title='Scrambler')
    scramEmbed.add_field(name='Original : ', value=ctn)
    scramEmbed.add_field(name='Scrambled : ', value=newMsg)
    await context.message.channel.send(embed=scramEmbed)

@client.command(name='vote', pass_context=True)
async def vote(context):
    voting = discord.Embed(title='vote')
    voting.add_field(name='vote for our bot at:', value='https://top.gg/bot/675609879083483136\nor https://discordbotlist.com/bots/roo-bot')

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

@client.command(name='info', pass_context=True)
async def info(context):
    emb = discord.Embed(name='Information')
    emb.add_field(name='this bot was proudly brought to you by:', value='roo fox#0001')
    emb.add_field(name="if you don't have access to slash commands", value='[reinvite me here](https://discord.com/api/oauth2/authorize?client_id=675609879083483136&permissions=8&scope=bot%20applications.commands)')
    await context.message.channel.send(embed = emb)


@client.command(aliases= ['purge','delete'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=None): # Set default value as None
    if amount == None:
        await ctx.channel.purge(limit=1000000)
    else:
        try:
            int(amount)
        except: # Error handler
            await ctx.send('Please enter a valid integer as amount.')
        else:
            await ctx.channel.purge(limit=amount)

@client.command(name='fuck')
async def fuck(context, mention: discord.Member=None, message=None):
    
    if (context.channel.is_nsfw()) == False:
        await context.message.channel.send('nsfw command, may not be used outside of nsfw area')
    elif (context.channel.is_nsfw()) == True:
        if mention == None:
            await context.message.channel.send('please mention someone to fuck')
        elif message == None:
            await context.message.channel.send('please choose between gay, lesbian or straight')
        else:
            if message == 'gay':
                gae = discord.Embed(title='you naughty', description='')
                gae.add_field(name=f'{context.message.author} fucked', value =f'{mention.name}')
                gaylink = secrets.choice(gay)
                gae.set_image(url = gaylink)

                await context.message.channel.send(embed = gae)
            elif message == 'straight':
                stra = discord.Embed(title='you naughty', description='')
                stra.add_field(name=f'{context.message.author} fucked', value =f'{mention.name}')
                straightlink = secrets.choice(straight)
                stra.set_image(url = straightlink)

                await context.message.channel.send(embed =stra)                
            elif message == 'lesbian':
                lesb = discord.Embed(title='you naughty', description='')
                lesb.add_field(name=f'{context.message.author} fucked', value =f'{mention.name}')
                lesblink = secrets.choice(lesbian)
                lesb.set_image(url = lesblink)

                await context.message.channel.send(embed = lesb)     
def fake_token():
    token = secrets.token_urlsafe(66)
    while sum(x == '_' for x in token) < 3:
        token = secrets.token_urlsafe(66)
    token = token.replace('_', '.')
    return token

@client.command(name='hack')
async def hack(context, member:discord.Member):
    
    if member == None:
        await context.message.channel.send('please mention someone to hack')
    else:
        msg = await context.message.channel.send('starting hack, please stand by')
        time.sleep(3)
        await msg.edit(content=f'hacking {member.name}')
        time.sleep(3)
        await msg.edit(content=f'gathering token for {member.name}\n:black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:')
        time.sleep(1)
        await msg.edit(content=f'gathering token for {member.name}\n:white_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:')
        time.sleep(1)
        await msg.edit(content=f'gathering token for {member.name}\n:white_large_square::white_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:')
        time.sleep(1)
        await msg.edit(content=f'gathering token for {member.name}\n:white_large_square::white_large_square::white_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:')
        time.sleep(1)
        await msg.edit(content=f'gathering token for {member.name}\n:white_large_square::white_large_square::white_large_square::white_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:')
        time.sleep(1)
        await msg.edit(content=f'gathering token for {member.name}\n:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::black_large_square::black_large_square::black_large_square::black_large_square::black_large_square:')
        time.sleep(1)
        await msg.edit(content=f'gathering token for {member.name}\n:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::black_large_square::black_large_square::black_large_square::black_large_square:')
        time.sleep(1)
        await msg.edit(content=f'gathering token for {member.name}\n:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::black_large_square::black_large_square::black_large_square:')
        time.sleep(1)
        await msg.edit(content=f'gathering token for {member.name}\n:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::black_large_square::black_large_square:')
        time.sleep(1)
        await msg.edit(content=f'gathering token for {member.name}\n:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::black_large_square:')
        time.sleep(1)
        await msg.edit(content=f'gathering token for {member.name}\n:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square:')
        time.sleep(1)
        tken = discord.Embed(title='token:', description=fake_token())

        await msg.edit(content='gathered token:')
        await msg.edit(embed = tken)

        time.sleep(1)
        await msg.edit(content='hacking password')
        time.sleep(0.5)
        await msg.edit(content='hacking password.')
        time.sleep(0.5)
        await msg.edit(content='hacking password..')
        time.sleep(0.5)
        await msg.edit(content='hacking password...')
        time.sleep(0.5)
        await msg.edit(content='hacking password')
        time.sleep(0.5)
        await msg.edit(content='hacking password.')
        time.sleep(0.5)
        password = ''.join(random.sample(string.ascii_letters,8))
        tken.add_field(name='password:', value=f'{password}')

        await msg.edit(embed = tken)
        time.sleep(1)
        await msg.edit(content = 'gathering email, please stand by.')
        time.sleep(1)
        await msg.edit(content = 'gathering email, please stand by..')
        time.sleep(1)
        await msg.edit(content = 'gathering email, please stand by...')
        time.sleep(1)
        await msg.edit(content = 'gathering email, please stand by')
        time.sleep(1)
        await msg.edit(content = 'gathering email, please stand by.')
        time.sleep(1)
        await msg.edit(content = 'gathering email, please stand by..')
        time.sleep(1)
        await msg.edit(content = 'gathering email, please stand by...')
        time.sleep(1)
        await msg.edit(content = 'gathering email, please stand by')
        time.sleep(1)
        await msg.edit(content = 'gathering email, please stand by.')
        time.sleep(1)
        mailend = secrets.choice(emails)

        username = ''.join(random.sample(string.ascii_lowercase,16))
        email = username + mailend

        tken.add_field(name='email address:', value=f'{email}')

        await msg.edit(embed = tken)
        time.sleep(1)
        await msg.edit(content='lastly, gathering ip address')
        time.sleep(1)
        await msg.edit(content='lastly, gathering ip address.')
        time.sleep(1)
        await msg.edit(content='lastly, gathering ip address..')
        time.sleep(1)
        await msg.edit(content='lastly, gathering ip address...')
        time.sleep(1)
        await msg.edit(content='lastly, gathering ip address')
        time.sleep(1)
        await msg.edit(content='lastly, gathering ip address.')
        time.sleep(1)
        await msg.edit(content='lastly, gathering ip address..')
        time.sleep(1)
        await msg.edit(content='lastly, gathering ip address...')
        time.sleep(1)
        num1 = random.randint(1, 255)
        num2 = random.randint(1, 255)
        num3 = random.randint(1, 255)
        num4 = random.randint(1, 255)

        tken.add_field(name='ip address:', value=f'{num1}.{num2}.{num3}.{num4}')

        await msg.edit(embed = tken)
        await msg.edit(content = 'hack done!')

@client.command(name='rn2')
async def rn2(context, number1=None, number2=None):
    if number1 is None or number2 is None:
        await context.message.channel.send("you need 2 numbers for this command to work")
    else:
        if number1.isdigit() and number2.isdigit():
            number1 = int(number1)
            number2 = int(number2)
            if number2 < number1:
                e = random.randint(number2, number1)
                await context.message.channel.send(f'seeing as {number2} is lower than {number1}, i have switched them around for you\nRandom number chosen: {e}')
            else:
                a = random.randint(number1, number2)
                await context.message.channel.send(f"Random number chosen: {a}")
        else:
            await context.message.channel.send("Lower and upper bound must be integers.")

@tasks.loop(seconds=86400)
async def datetask():
    tz = pytz.timezone('Europe/Berlin')
    berlin_current_datetime = datetime.now(tz)
    await client.wait_until_ready()
    channel = client.get_channel(895690695573123153)
    await channel.send(f"current date {berlin_current_datetime}")

datetask.start()

config.read('auth.ini')
token = config['AUTH']['token']

(client.run(token))
