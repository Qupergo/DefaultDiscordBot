from keep_alive import keep_alive
import aiohttp
import os
import time
import random
import asyncio
import json
from discord import Game
from discord.ext.commands import Bot
currentOne = ""
DISCORD_MESSAGE_PREFIX = "+"

client = Bot(command_prefix=DISCORD_MESSAGE_PREFIX)

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

#eight_ball
@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

#reverse
@client.command(name='reverse',
                description="Reverses what you write.",
                brief="Reverses what you write.",
                aliases=['re', 'rev', 'reve'],
                pass_context=False)
async def reverse(*args):
	await client.say(' '.join(args)[::-1])

#bitcoin
@client.command(name='bitcoin',
                description="Displays the current price of bitcoin.",
                brief="Displays current bitcoin price.",
                aliases=['bit', 'bitc'])
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])


#randcolor
@client.command(name='randcolor',
                description="Writes a random color.",
                brief="Writes a random color.",
                aliases=['rc', 'randc', 'randcolour'])
async def randcolor():
	colors = ["Red", 'Orange', 'Yellow', 'Green', 'Cyan', 'Blue', 'Indigo', 'Violet', 'Purple', 'Magenta', 'Pink', 'Brown', 'White', 'Gray', 'Black', 'Turquoise']
	await client.say(random.choice(colors))

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)