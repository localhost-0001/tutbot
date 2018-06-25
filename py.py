import discord

import asyncio
import time
import secrets
import handler

client = discord.Client()

from commands import help

@client.event
async def on_ready():
    print("BOIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")


@client.event
async def on_message(message):

    await handler.handle(message, client)

client.run(secrets.token)
