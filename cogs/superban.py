import discord
from discord.ext import commands
from bot import collection, client

class SuperBanCog(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command(name="superban")
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def superban(self, ctx, member: discord.Member):
        banName = member.display_name
        banId = member.id
        authorId = ctx.message.author.id
        botId = client.user.id
        query = {"_id": banId}
        User = collection.find_one(query)
        print(authorId)
        print(banId)
        if banId == authorId:
            await ctx.channel.send("Sorry but you cannot superban yourself.")
        elif banId != authorId:
            if banId == botId:
                await ctx.channel.send("Sorry but you cannot superban BanBot.")
            elif banId != botId:
                if User:
                    collection.update_one(query, {"$inc": {"bans": 5}})
                    await ctx.channel.send(f"<@{banId}> has been banned 5 times!")
                elif not User:
                    query2 = {"_id": banId, "name": banName, "bans": 5}
                    collection.insert_one(query2)
                    await ctx.channel.send(f"<@{banId}> has been banned 5 times!")

def setup(bot):
    bot.add_cog(SuperBanCog(bot))