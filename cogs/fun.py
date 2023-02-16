import discord
from discord.ext import commands
import secrets
import base64 as b64
import random
import time
import string
import json
import configparser
import requests
import re
from bs4 import BeautifulSoup

def scram(content):
    contentL = list(content)
    random.shuffle(contentL)
    content = ''.join(contentL)
    return content

def fake_token():
    token = secrets.token_urlsafe(66)
    while sum(x == '_' for x in token) < 3:
        token = secrets.token_urlsafe(66)
    token = token.replace('_', '.')
    return token

with open('lists.json', 'r') as f:
  json_data = json.load(f)

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    with open('lists.json', 'r') as f:
      json_data = json.load(f)

    @commands.slash_command(name= 'amibored')
    async def amibored(self, context):
        shit = [
        'yes',
        'no'
        ]

        choose = secrets.choice(shit)

        await context.respond(choose)

    @commands.slash_command(name='b64e', pass_context=True)
    async def b64e(self, context):
        msg = context.message.content[9:]
        b64msg = b64.b64encode(msg.encode())
        encodeEmbed = discord.Embed(title='Base64 Encoder')
        encodeEmbed.add_field(name='Original message:', value=msg, inline=False)
        encodeEmbed.add_field(name='Encoded message:', value=b64msg.decode(), inline=False)
        await context.respond(embed=encodeEmbed)

    @commands.slash_command(name='b64d', pass_context=True)
    async def b64e(self, context):
        b64msg = context.message.content[9:]
        msg = b64.b64decode(b64msg.encode())
        encodeEmbed = discord.Embed(title='Base64 Decoder')
        encodeEmbed.add_field(name='Encoded message:', value=b64msg, inline=False)
        encodeEmbed.add_field(name='Original message:', value=msg.decode(), inline=False)
        await context.respond(embed=encodeEmbed)

    @commands.slash_command(name='rps')
    async def rps(self, context, *, message=None):
        rpsss = secrets.choice(json_data("rpss"))
        msg = 'rock', 'paper', 'scissors'
        if message == None:
            await context.respond('please choose either rock, paper or scissors')
        else:
            if message.lower() == "rock":
                rock = discord.Embed(name='rock, papaer, scissors')
                rock.add_field(name='you', value=f'{message}')
                rock.add_field(name='VS', value='VS')
                rock.add_field(name='opponent', value=f'{rpsss}')

                await context.respond(embed = rock)
                
                time.sleep(1)

                if rpsss == "rock":
                    await context.respond("tie")
                elif rpsss == "paper":
                    await context.respond("you lost!")
                elif rpsss == "scissors":
                    await context.respond("you won!")

            if message.lower() == 'paper':
                paper = discord.Embed(name='rock, papaer, scissors')
                paper.add_field(name='you', value=f'{message}')                
                paper.add_field(name='VS', value='VS')
                paper.add_field(name='opponent', value=f'{rpsss}')

                await context.respond(embed = paper)

                time.sleep(1)

                if rpsss == "paper":
                    await context.respond("tie")
                elif rpsss == "scissors":
                    await context.respond("you lost!")
                elif rpsss == "rock":
                    await context.respond("you won!")

            if message.lower() == 'scissors':
                scissors = discord.Embed(name='rock, papaer, scissors')
                scissors.add_field(name='you', value=f'{message}')
                scissors.add_field(name='VS', value='VS')
                scissors.add_field(name='opponent', value=f'{rpsss}')

                await context.respond(embed = scissors)

                time.sleep(1)

                if rpsss == "scissors":
                    await context.respond("tie")
                elif rpsss == "rock":
                    await context.respond("you lost!")
                elif rpsss == "paper":
                    await context.respond("you won!")

    @commands.slash_command(name='gen', pass_context=True)
    async def gen(self, context):

        mailend = secrets.choice(json_data("emails"))

        username = ''.join(random.sample(string.ascii_lowercase,16))
        email = username + mailend
        password = ''.join(random.sample(string.ascii_letters,8))
        embeds = discord.Embed(name='account geterator')
        embeds.add_field(name=f'{email}', value=f'{password}')
        
        await context.respond(embed = embeds)

    @commands.slash_command(name='scramble', pass_context=True)
    async def scramble(self, context):
        ctn = context.message.content[13:]
        newMsg = scram(ctn)
        scramEmbed = discord.Embed(title='Scrambler')
        scramEmbed.add_field(name='Original : ', value=ctn)
        scramEmbed.add_field(name='Scrambled : ', value=newMsg)
        await context.respond(embed=scramEmbed)
    
    @commands.slash_command(name='hack')
    async def hack(self, context, member:discord.Member):
        
        if member == None:
            await context.respond('please mention someone to hack')
        else:
            msg = await context.respond('starting hack, please stand by')
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
            mailend = secrets.choice(json_data("emails"))

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

    @commands.slash_command(name='rn2')
    async def rn2(self, context, number1=None, number2=None):
        if number1 is None or number2 is None:
            await context.respond("you need 2 numbers for this command to work")
        else:
            if number1.isdigit() and number2.isdigit():
                number1 = int(number1)
                number2 = int(number2)
                if number2 < number1:
                    e = random.randint(number2, number1)
                    await context.respond(f'seeing as {number2} is lower than {number1}, i have switched them around for you\nRandom number chosen: {e}')
                else:
                    a = random.randint(number1, number2)
                    await context.respond(f"Random number chosen: {a}")
            else:
                await context.respond("Lower and upper bound must be integers.")

    @commands.slash_command(name='rn', pass_context=True)
    async def rn (self, context):
        await context.respond(random.randint(1, 1000))

    @commands.slash_command(name="cute", pass_context = True)
    async def cuteCheck(self, context, member: discord.Member):
        cute = random.randint(0, 100)
        await context.respond(f'{member.name} is {cute}% cute.')

    @commands.slash_command(name='cringe', pass_context=True)
    async def cringe (self, context):
        await context.respond('fortnite') 

    @commands.slash_command(name= 'randompokemon', pass_context=True)
    async def randompokemon(self, context):
        pokemoon = secrets.choice(json_data["pokemon"])
        await context.respond(pokemoon)

    @commands.slash_command(name= 'kill', pass_context=True)
    async def kill(self, context, person=None):
        if person == None:
            await context.respond('at least mention someone so i can then disappoint you')
        else:
            await context.respond('yeah... no')

    @commands.slash_command(name='compliment', pass_context=True)
    async def compliment(self, context):
        await context.respond('loading compliment')
        await edit(content='loading compliment.')
        await botMsg.edit(content='loading compliment..')
        await botMsg.edit(content='loading compliment...')
        await botMsg.edit(content='loading compliment')
        await botMsg.edit(content='loading compliment.')
        await botMsg.edit(content='loading compliment..')
        comp = secrets.choice(json_data("compliments"))
        await botMsg.edit(content=comp)

    @commands.slash_command(name='dog')
    async def dog(self, context):
        barko = secrets.choice(bark)
        await context.respond(barko)

    @commands.slash_command(name="gay")
    async def gay(self, context, member: discord.Member):
        choice = random.randint(0,100)
        embed = discord.Embed(title="Gay meter")
        embed.add_field(name=f"{context.author} is", value=f"{choice}% gay")

        await context.respond(embed=embed)

    @commands.slash_command(name="scp")
    async def scp(self, context, message=None):
        scp_number = re.search('\d+', message).group()

        # Retrieve the SCP article from the wiki
        response = requests.get(f'http://www.scp-wiki.net/scp-{scp_number}')
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1').text
        description = soup.find('div', {'id': 'page-content'}).text.strip()[:1930] + f'... Source: http://www.scp-wiki.net/scp-{scp_number}'

        # Send the SCP information to the user
        await context.respond(f'SCP-{scp_number}: {title}\n\n{description}')

def setup(client):
    client.add_cog(fun(client))