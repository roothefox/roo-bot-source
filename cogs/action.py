import discord
from discord.ext import commands
import secrets
import json
import random
from discord import is_nsfw

with open('lists.json', 'r') as f:
  json_data = json.load(f)

class action(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name= 'kiss', pass_context = True)
    async def kiss (self, context, member: discord.Member):
        kissles = discord.Embed(title='did you just kissy?')
        kissles.add_field(name= f'{context.author} kissed', value=f'{member.name}') 
        kissles.add_field(name="", value="[Join support server to report issues](https://discord.gg/ADGYsQAUg5)")
        randomlink = secrets.choice(json_data["kisses"])

        kissles.set_image(url= randomlink)
        await context.respond(embed = kissles)

    @commands.slash_command(name= 'hug', pass_context = True)
    async def hug (self, context, member: discord.Member):
        huggles = discord.Embed(title='huggies')
        author = context.author
        huggles.add_field(name= f'{author} hugged', value=f'{member.name}')

        random_link = secrets.choice(json_data["hugs"])

        huggles.set_image(url= random_link)
        await context.respond(embed = huggles)

    @commands.slash_command(name= 'slap', pass_context= True)
    async def slap(context, member: discord.Member):
        slapples = discord.Embed(title= 'why slap?')
        slapples = slapples.add_field (name= f'{context.author} slapped', value=f'{member.name}')

        slapers = secrets.choice(json_data["slaps"])

        slapples = slapples.set_image(url= slapers)
        await context.respond(embed = slapples)

    @commands.slash_command(name= 'pat', pass_context=True)
    async def pat(context, member: discord.Member):
        patties = discord.Embed(title= 'awww you gib pats!!!')
        patties = patties.add_field(name= f'{context.author} gave some pats to', value=f'{member.name}')

        paters = secrets.choice(json_data["pats"])

        patties = patties.set_image(url= paters)

        await context.respond(embed = patties)

    @commands.slash_command(name= 'boop', pass_context=True)
    async def boop(context, member: discord.Member):
        boopers = discord.Embed(title= 'hehehe get booped')
        boopers = boopers.add_field(name=  f'{context.author} booped', value=f'{member.name}')

        boopy = secrets.choice(json_data["boops"])
        boopers = boopers.set_image(url= boopy)

        await context.respond(embed = boopers)

    @commands.slash_command(name='fuck')
    @is_nsfw()
    async def fuck(self, context, mention: discord.Member=None, message=None):

        if mention == None:
            await context.respond('please mention someone to fuck')
        elif message == None:
            await context.respond('please choose between gay, lesbian or straight')
        else:
            if message == 'gay':
                gae = discord.Embed(title='you naughty', description='')
                gae.add_field(name=f'{context.author} fucked', value =f'{mention.name}')
                gaylink = secrets.choice(json_data["gay"])
                gae.set_image(url = gaylink)

                await context.respond(embed = gae)
            elif message == 'straight':
                stra = discord.Embed(title='you naughty', description='')
                stra.add_field(name=f'{context.author} fucked', value =f'{mention.name}')
                straightlink = secrets.choice(json_data["straight"])
                stra.set_image(url = straightlink)

                await context.respond(embed =stra)                
            elif message == 'lesbian':
                lesb = discord.Embed(title='you naughty', description='')
                lesb.add_field(name=f'{context.author} fucked', value =f'{mention.name}')
                lesblink = secrets.choice(json_data["lesbian"])
                lesb.set_image(url = lesblink)

                await context.respond(embed = lesb)   

    @commands.slash_command(name= 'snuggle', pass_context = True)
    async def snuggle (context, member: discord.Member):
        snuggies = discord.Embed(title='snuggies')
        snuggies.add_field(name= f'{context.author} snuggled', value=f'{member.name}')

        random_link = secrets.choice(json_data["snuggles"])

        snuggies.set_image(url= random_link)
        await context.respond(embed = snuggies)

    @commands.slash_command(name= 'ship', pass_context=True)
    async def ship(self, context, member: discord.Member=None):
        num = random.randint(0, 100)
        

        if member == None:
            await context.respond("please mention someone so i can find out how much you fit with the other") 
        else:
            ship = discord.Embed(title='love percentage')
            if num <= 10 and num >= 0:
                ship.add_field(name= 'command author', value= f'{context.author}')
                ship.add_field(name=f'{num}%', value='♥♡♡♡♡♡♡♡♡♡')
                ship.add_field(name='mentioned user', value=f'{member.name}')
                await context.respond(embed = ship)
            elif num <= 20 and num >= 11:
                ship.add_field(name= 'command author', value= f'{context.author}')
                ship.add_field(name=f'{num}%', value='♥♥♡♡♡♡♡♡♡♡')
                ship.add_field(name='mentioned user', value=f'{member.name}')
                await context.respond(embed = ship)
            elif num <= 30 and num >= 21:
                ship.add_field(name= 'command author', value= f'{context.author}')
                ship.add_field(name=f'{num}%', value='♥♥♥♡♡♡♡♡♡♡')
                ship.add_field(name='mentioned user', value=f'{member.name}')
                await context.respond(embed = ship)
            elif num <= 40 and num >= 31:
                ship.add_field(name= 'command author', value= f'{context.author}')
                ship.add_field(name=f'{num}%', value='♥♥♥♥♡♡♡♡♡♡')
                ship.add_field(name='mentioned user', value=f'{member.name}')
                await context.respond(embed = ship)
            elif num <= 50 and num >= 41:
                ship.add_field(name= 'command author', value= f'{context.author}')
                ship.add_field(name=f'{num}%', value='♥♥♥♥♥♡♡♡♡♡')
                ship.add_field(name='mentioned user', value=f'{member.name}')
                await context.respond(embed = ship)
            elif num <= 60 and num >= 51:
                ship.add_field(name= 'command author', value= f'{context.author}')
                ship.add_field(name=f'{num}%', value='♥♥♥♥♥♥♡♡♡♡')
                ship.add_field(name='mentioned user', value=f'{member.name}')
                await context.respond(embed = ship)
            elif num <= 70 and num >= 61:
                ship.add_field(name= 'command author', value= f'{context.author}')
                ship.add_field(name=f'{num}%', value='♥♥♥♥♥♥♥♡♡♡')
                ship.add_field(name='mentioned user', value=f'{member.name}')
                await context.respond(embed = ship)
            elif num <= 80 and num >= 71:
                ship.add_field(name= 'command author', value= f'{context.author}')
                ship.add_field(name=f'{num}%', value='♥♥♥♥♥♥♥♥♡♡')
                ship.add_field(name='mentioned user', value=f'{member.name}')
                await context.respond(embed = ship)
            elif num <= 90 and num >= 81:
                ship.add_field(name= 'command author', value= f'{context.author}')
                ship.add_field(name=f'{num}%', value='♥♥♥♥♥♥♥♥♥♡')
                ship.add_field(name='mentioned user', value=f'{member.name}')
                await context.respond(embed = ship)
            elif num <= 1000 and num >= 91:
                ship.add_field(name= 'command author', value= f'{context.author}')
                ship.add_field(name=f'{num}%', value='♥♥♥♥♥♥♥♥♥♥')
                ship.add_field(name='mentioned user', value=f'{member.name}')
                await context.respond(embed = ship)
            else:
                await context.respond(f'test {num}')

def setup(client):
    client.add_cog(action(client))
