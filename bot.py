import os
from discord.ext import commands
from pymongo import MongoClient

mongo_uri = "(mongourl)" # mongo url goes here, remove parenthesis
cluster = MongoClient(mongo_uri)
db = cluster["(db name)"] # db name goes here, remove parenthesis
collection = db["(collection name)"] # collection name goes here, remove parenthesis
client = commands.Bot(command_prefix= '.')
# remove the id and replace it with yours, it was just a simple owner checking system i used.
@client.command()
async def load(ctx, extension):
    id = str(ctx.message.author.id)
    if id == "your id":
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} is loaded!')
    elif id != "your id":
        await ctx.send(f'Sorry but you cannot use this command.')

@client.command()
async def unload(ctx, extension):
    id = str(ctx.message.author.id)
    if id == "your id":
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} is unloaded!')
    elif id != "your id":
        await ctx.send(f'Sorry but you cannot use this command.')

@client.command()
async def reload(ctx, extension):
    id = str(ctx.message.author.id)
    if id == "your id":
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} is reloaded!')
    elif id != "your id":
        await ctx.send(f'Sorry but you cannot use this command.')

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        client.load_extension(f"cogs.{name}")

client.run("(bot token)") # bot token goes here, remove parenthesis