import discord
from discord.ext import commands

class MinecraftCog(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(name="minecraft")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def minecraft(self, ctx):
        await ctx.send("https://tenor.com/view/minecraft-gif-9643254")
        await ctx.send("https://tenor.com/view/minecraft-sonic-minecraft-sonic-sonic3d-sonic3d-blast-gif-19349494")

def setup(client):
    client.add_cog(MinecraftCog(client))