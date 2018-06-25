import discord

import asyncio
import time
import secrets

client = discord.Client()



@client.event
async def on_ready():
    print("BOIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")


@client.event
async def on_message(message):
    if message.content == "u too":
        embed = discord.Embed(title="I HAVE COOKIES", url=None, colour=0xfeabfe)
        embed.add_field(name="yey", value="yeey")
        await client.send_message(message.channel, embed=embed)

client.run(secrets.token)
