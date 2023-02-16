import discord
from discord.ext import commands

class basic(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name = 'invite', pass_context=True)
    async def invite (self, context):
            join = discord.Embed(name='join')
            join.add_field(name='click below to invite the bot\nIm in ' + str(len(self.client.guilds)) + ' servers', value='[invite](https://discord.com/api/oauth2/authorize?client_id=675609879083483136&permissions=8&scope=bot%20applications.commands)')
            join.set_image(url= 'https://cdn.discordapp.com/avatars/675609879083483136/9169e12dc1e32c509a495bb93f1624e9.webp?size=1024')

            await context.respond(embed = join)

    @commands.slash_command(name= 'servers', pass_context=True)
    async def servers(self, context):
        await context.respond("I'm in " + str(len(self.client.guilds)) + " servers")

    @commands.slash_command(name='ping', brief='pong', description='simple pong lol', pass_context=True)
    async def ping(self, context):
        await context.respond("Pong!")

    @commands.slash_command(name='avatar', pass_context = True)
    async def avatar(self, context, member: discord.Member=None, size = 4096):
        if member is None:
            user = context.author
            url = user.avatar_url
            await context.respond(url)
        else:
            url = member.avatar_url
            await context.respond(url)

    @commands.slash_command(name='user_count', pass_context = True)
    async def memberCount(self, context):
        guild = context.author.guild
        usercount = guild.member_count
        await context.respond("members: " + str(usercount))

    @commands.slash_command(name='vyrix')
    async def vyrix(self, context):
        yesh = discord.Embed(name='Vyrix')
        yesh.add_field(name='invite my besties bot Vyrix', value='[Click here](https://discord.com/api/oauth2/authorize?client_id=802660359760248833&permissions=201452550&scope=bot)')
        yesh.set_image(url = 'https://cdn.discordapp.com/avatars/802660359760248833/a15e939454d242882149384744b927a7.webp?size=1024')

        await context.respond(embed = yesh)

    @commands.slash_command(name='info', pass_context=True)
    async def info(self, context):
        emb = discord.Embed(name='Information')
        emb.add_field(name='this bot was proudly brought to you by:', value='<@274270850830696448>')
        emb.add_field(name="if you don't have access to slash commands", value='[reinvite me here](https://discord.com/api/oauth2/authorize?client_id=675609879083483136&permissions=8&scope=bot%20applications.commands)')
        await context.respond(embed = emb)

    @commands.slash_command(name="profile")
    async def profile(self, context, member: discord.Member = None):
        if member == None:
            link = context.author.avatar
            created_at = context.author.created_at.strftime("%b %d, %Y, %T")
            joined_at = context.author.joined_at.strftime("%b %d, %Y, %T")

            embed = discord.Embed(title=f"{context.author}'s profile", description="")
            embed.add_field(name="Username:", value=f"{context.author}")
            embed.add_field(name="User id:", value=f"{context.author.id}")   
            embed.add_field(name="Creation date:", value=f"{created_at}")
            embed.add_field(name="Join Date:", value=f"{joined_at}")
            embed.set_thumbnail(url=link)
            embed.set_footer(icon_url=context.author.avatar, text=f"requested by {context.author}")

            await context.respond(embed=embed)
        else:
            linkmention = member.avatar
            created_mention = member.created_at.strftime("%b %d, %Y, %T")
            joined_mention = member.joined_at.strftime("%b %d, %Y, %T")
        
            embed = discord.Embed(title=f"{member.display_name}'s profile", description="")
            embed.add_field(name="Username:", value=f"{member.display_name}")
            embed.add_field(name="User id:", value=f"{member.id}")   
            embed.add_field(name="Creation date:", value=f"{created_mention}")
            embed.add_field(name="Join Date:", value=f"{joined_mention}")
            embed.set_thumbnail(url=linkmention)
            embed.set_footer(icon_url=context.author.avatar, text=f"requested by {context.author}")

            await context.respond(embed=embed)

    @commands.slash_command(name='vote', pass_context=True)
    async def vote(self, context):
        voting = discord.Embed(title='vote')
        voting.add_field(name='vote for our bot at:', value='https://top.gg/bot/675609879083483136\nor https://discordbotlist.com/bots/roo-bot')

        await context.respond(embed = voting)

def setup(client):
    client.add_cog(basic(client))