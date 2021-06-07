import discord
from discord.ext import commands
from bot import collection, client

class BanCountCog(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(name="bancount")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def bancount(self, ctx, member: discord.Member):
        banName = member.display_name
        banId = member.id
        authorId = ctx.message.author.id
        botId = client.user.id
        query = {"_id": banId}
        User = collection.find_one(query)
        banCount = User["bans"]
        if banId == authorId:
            await ctx.channel.send("Sorry but BanBot has no bans, so you cannot see them.")
        elif banId != authorId:
            if banId == botId:
                await ctx.channel.send("Sorry but BanBot cannot be banned, so it has no bans.")
            elif banId != botId:
                if User:
                    if authorId == banId:
                        if banCount == 1:
                            await ctx.channel.send(f"You have {banCount} ban!")
                        elif banCount != 1 or banCount == 0:
                            await ctx.channel.send(f"You have {banCount} bans!")
                    elif authorId != banId:
                        if banCount == 1:
                            await ctx.channel.send(f"{banName} has {banCount} ban!")
                        elif banCount != 1 or banCount == 0:
                            await ctx.channel.send(f"{banName} has {banCount} bans!")
                if not User:
                    query2 = {"_id": banId, "name": banName, "bans": 0}
                    collection.insert_one(query2)
                    await ctx.channel.send(f"You have {banCount} bans!")

def setup(client):
    client.add_cog(BanCountCog(client))