import discord

perm = 0

async def ex(args, message, client, cmdin):
    print("triggered")
    commands = {

        "help": "Help command, what do you expect?",
        "Tree": "Grows a tree in your non extistant brain",
        "Fuck": "Makes the channel nsfw"

    }
    embed = discord.Embed(title="I HAVE COOKIES", url=None, colour=0xfeabfe)

    helpstring = ["LIST OF COMMANDS\n"]

    for a, b in commands.items():
        akj = a + ": "
        helpstring.append(akj)
        helpstring.append(b)

    embed.add_field(name="yey", value='\n'.join(helpstring ))
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/1200px-Cat03.jpg")
    await client.send_message(message.channel, embed=embed)
