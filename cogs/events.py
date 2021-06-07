import discord
from discord.ext import commands

class EventsCog(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("BANBOT is ready for BANNING!")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            if round(error.retry_after/60) == 0:
                await ctx.send(f'This command is on a cooldown, you can use it in ~{round(error.retry_after)} seconds!')
            elif round(error.retry_after) == 1:
                await ctx.send(f'This command is on a cooldown, you can use it in ~{round(error.retry_after)} second!')
            elif round(error.retry_after/60) != 0 and not 60:
                await ctx.send(f'This command is on a cooldown, you can use it in ~{round(error.retry_after/60)} minutes!')
            elif round(error.retry_after/60) == 1:
                await ctx.send(f'This command is on a cooldown, you can use it in ~{round(error.retry_after/60)} minute!')
            elif round(error.retry_after/60) == 60:
                await ctx.send(f'This command is on a cooldown, you can use it in ~1 hour!')
            elif round(error.retry_after/60/60) != 1:
                await ctx.send(f'This command is on a cooldown, you can use it in ~{round(error.retry_after/60/60)} hours!')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.channels, name='this-should-just-be-joins')
        await channel.send('https://i.kym-cdn.com/entries/icons/original/000/035/175/cheesed-.jpg')

def setup(client):
    client.add_cog(EventsCog(client))