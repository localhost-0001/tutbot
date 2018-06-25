import discord
import config

from commands import help, fuckyoutoo

commands = {

    "help" : help,
    "h" : help,
    "love" : fuckyoutoo,

    "help" : help

}


async def handle(message, client):

    if message.content.lower().startswith(config.prefix):

        cmdin = message.content[len(config.prefix):].split(" ")[0].lower()
        args = message.content.split(" ")[1:]

        if commands.__contains__(cmdin):

            cmd = commands[cmdin]

            await cmd.ex(args, message, client, cmdin)
