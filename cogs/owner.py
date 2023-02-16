import discord
from discord.ext import commands

class owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='cstatus', pass_context=True)
    async def updateCStatus(self, context):
        str(context.message.author), (context.message.channel.name)
        if context.message.author.id == 274270850830696448:
            original_status = self.client.guilds[0].get_member(self.client.user.id).status
            status = context.message.content[12:]
            if status == 'reset':
                await self.client.change_presence(status=original_status, activity=discord.Game('Living in Spain without the a'))
                await context.send('Status successfully reset')
            else:
                await self.client.change_presence(status=original_status, activity=discord.Game(str(status)))
        else:
            await context.send('no')

    @commands.command(name='ostatus', pass_context=True)
    async def updateOStatus(self, context):
        str(context.message.author), (context.message.channel.name)
        if context.message.author.id == 274270850830696448:
            original_status = self.client.guilds[0].get_member(self.client.user.id).activity
            status = context.message.content[12:]
            if status == 'dnd':
                await self.client.change_presence(status=discord.Status.do_not_disturb, activity=original_status)
            elif status == 'idle':
                await self.client.change_presence(status=discord.Status.idle, activity=original_status)
            elif status == 'off':
                await self.client.change_presence(status=discord.Status.invisible, activity=original_status)
            elif status == 'on':
                await self.client.change_presence(status=discord.Status.online, activity=original_status)
            elif status == 'mb':
                await self.client.change_presence(status=discord.Status.online, activity=original_status)
        else:
            await context.send('no')

    @commands.command()
    async def rename(self, context, name):
        if context.message.author.id == 274270850830696448:
            await self.client.user.edit(username=name)
        else:
            await context.send('no')

def setup(client):
    client.add_cog(owner(client))