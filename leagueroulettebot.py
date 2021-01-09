# leagueroulettebot tells you whether or not to play League based on a coin flip, if it's 0 you don't play, if it's 1 you do play. 

import random
import discord

client = discord.Client()

# establishes connection and tells you if you're connected 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # you can change $League? to whatever message you want. When $League? or any other custom message is typed into your Discord chat the bot will automatically reply. 
    if message.content.startswith('$League?'):
        if (random.randint(0,1)) == 0:                 
            await message.channel.send('don\'t play League')
        else:
            await message.channel.send('unfortunately you have to play League')

    
client.run('BOT TOKEN GOES HERE')
