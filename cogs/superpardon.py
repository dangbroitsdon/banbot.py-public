import discord
from discord.ext import commands
from bot import collection, client

class SuperPardonCog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name="superpardon")
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def superpardon(self, ctx, member: discord.Member):
        banName = member.display_name
        banId = member.id
        authorId = ctx.message.author.id
        botId = client.user.id
        query = {"_id": banId}
        User = collection.find_one(query)
        if banId == authorId:
            await ctx.channel.send("Sorry but you cannot superpardon yourself.")
        elif banId != authorId:
            if banId == botId:
                await ctx.channel.send("Sorry but you cannot superpardon BanBot.")
            elif banId != botId:
                if User:
                    collection.update_one(query, {"$inc": {"bans": -5}})
                    await ctx.channel.send(f"<@{banId}> has been pardoned 5 times!")
                elif not User:
                    query2 = {"_id": banId, "name": banName, "bans": -5}
                    collection.insert_one(query2)
                    await ctx.channel.send(f"<@{banId}> has been pardoned 5 times!")

def setup(client):
    client.add_cog(SuperPardonCog(client))