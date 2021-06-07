import discord
from discord.ext import commands
from bot import collection, client

class BanCog(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command(name="ban")
    @commands.cooldown(3, 3600, commands.BucketType.user)
    async def ban(self, ctx, member: discord.Member):
        banName = member.display_name
        banId = member.id
        authorId = ctx.message.author.id
        botId = client.user.id
        query = {"_id": banId}
        User = collection.find_one(query)
        if banId == authorId:
            await ctx.send("Sorry but you cannot ban yourself.")
        elif banId != authorId:
            if banId == botId:
                await ctx.send("Sorry but you cannot ban BanBot")
            elif banId != botId:
                if User:
                    collection.update_one(query, {"$inc": {"bans": 1}})
                    await ctx.send(f"<@{banId}> has been banned!")
                elif not User:
                    query2 = {"_id": banId, "name": banName, "bans": 1}
                    collection.insert_one(query2)
                    await ctx.send(f"<@{banId}> has been banned!")

def setup(client):
    client.add_cog(BanCog(client))