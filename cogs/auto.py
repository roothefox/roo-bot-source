import discord
from discord.ext import commands, tasks
import pytz
from datetime import datetime

class auto(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.datetask.start()


    @commands.Cog.listener()
    async def on_ready(self):
        print("Roo Bot is in " + str(len(self.client.guilds)) + " servers")


    @commands.Cog.listener()
    async def on_message(self, message):
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game("in " + str(len(self.client.guilds)) + " servers, owner: roo fox#0001"))
        if message.content.lower() == "hello":
            await message.channel.send("hey dirtbag")
        elif message.content.lower() == "meg":
            await message.channel.send("hey dirtbag")
        elif message.content.lower() == "axelle":
            await message.channel.send("clean your room!")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if member.guild.id == 1027477476928139284:
            channel = self.client.get_channel(1027510209519812669)

            embed = discord.Embed(title=f"Welcome {member.display_name}", description="Hope you enjoy your stay here!!")
            embed.set_image(url=member.avatar_url)

            await channel.send(embed=embed)

    @tasks.loop(seconds=86400)
    async def datetask(self):
        tz = pytz.timezone('Europe/Berlin')
        berlin_current_datetime = datetime.now(tz)
        await self.client.wait_until_ready()
        channel = self.client.get_channel(895690695573123153)
        await channel.send(f"current date {berlin_current_datetime}")

    @tasks.loop(seconds=86400)
    async def send_used_commands(self):
        length_of_list = len(x)
        await self.client.wait_until_ready()
        channel = self.client.get_channel(857340253542678531)
        await channel.send(f"commands used in last 24h: {length_of_list}")
        x.clear()

def setup(client):
    client.add_cog(auto(client))