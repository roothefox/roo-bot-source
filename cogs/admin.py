from discord.ext import commands
import discord

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases= ['purge','delete'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=None): # Set default value as None
        if amount == None:
            await ctx.channel.purge(limit=1000000)
        else:
            try:
                int(amount)
            except: # Error handler
                await ctx.send('Please enter a valid integer as amount.')
            else:
                await ctx.channel.purge(limit=amount)

    @commands.command(name='kick', pass_context = True)
    @commands.has_permissions(kick_members = True)
    async def kick(self, context, member: discord.Member, reason=None):
        str(context.message.author), (context.message.channel.name)
        await member.kick(reason=reason)
        await context.send('User ' + member.display_name + ' has been kicked.')

    @commands.command(name='ban', pass_context = True)
    @commands.has_permissions(kick_members = True, ban_members = True)
    async def ban(self, context, member: discord.Member, *, reason=None):
        str(context.message.author), (context.message.channel.name)
        await member.ban(reason=reason)
        await context.send('User ' + member.display_name + ' has been banned.')

    @commands.command(name='change_nick', pass_context = True)
    async def change_nick(self, context, member: discord.Member, nickname=None):
        str(context.message.author), (context.message.channel.name)
        currentNick = member.nick
        newNick = nickname
        if newNick == None:
            await context.send("Operation aborted.")
        else:
            await member.edit(nick=newNick)

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def clean(self, ctx, limit: int):
            await ctx.channel.purge(limit=limit)
            await ctx.send('Cleared by {}'.format(ctx.author.mention))
            await ctx.message.delete()

def setup(client):
    client.add_cog(Admin(client))