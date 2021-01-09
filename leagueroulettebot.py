# leagueroulettebot tells you whether or not to play league based on a random number it generates

import random
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$League?'):
        if (random.randint(1,10) % 2) == 0:
            await message.channel.send('don\'t play League')
        else:
            await message.channel.send('unfortunately you have to play League')

    
client.run('Nzk2NTIyMDE1Mjc1NDgzMjE2.X_ZI7w.xZ-JllwyYDJM5utZP187Wl_03Ps')
