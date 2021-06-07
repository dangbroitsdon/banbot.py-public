import os
from discord.ext import commands
from pymongo import MongoClient

mongo_uri = "(mongourl)" # mongo url goes here, remove parenthesis
cluster = MongoClient(mongo_uri)
db = cluster["(db name)"] # db name goes here, remove parenthesis
collection = db["(collection name)"] # collection name goes here, remove parenthesis
client = commands.Bot(command_prefix= '.')

@client.command()
async def load(ctx, extension):
    id = ctx.message.author.id
    if id == 301102975500419073:
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} is loaded!')
    elif id != 301102975500419073:
        await ctx.send(f'Sorry but you cannot use this command.')

@client.command()
async def unload(ctx, extension):
    id = ctx.message.author.id
    if id == 301102975500419073:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} is unloaded!')
    elif id != 301102975500419073:
        await ctx.send(f'Sorry but you cannot use this command.')

@client.command()
async def reload(ctx, extension):
    id = ctx.message.author.id
    if id == 301102975500419073:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} is reloaded!')
    elif id != 301102975500419073:
        await ctx.send(f'Sorry but you cannot use this command.')

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        client.load_extension(f"cogs.{name}")

client.run("(bot token)") # bot token goes here, remove parenthesis