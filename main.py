import discord
import asyncio

#Discord bot settings
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents,activity=discord.Game(name='Escape from Tarkov'))

#Declaring variables
tracked_servers = set()


#Discord bot startup
@client.event
async def on_ready():
    pingCounter = 0
    print('Logged in as {0.user}'.format(client))
    print('Connected to servers:')
    for guild in client.guilds:
        tracked_servers.add(guild.id)
        print(guild.name)


 #Bot recieves message
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return


client.run('--- YOUR TOKEN HERE ---')