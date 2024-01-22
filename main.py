import discord
from discord.ext import commands
import youtube_dl

intents = discord.Intents.default()
intents.all()

# Create a bot instance with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

#Declaring variables
tracked_servers = set()

async def join_channel(ctx):
    channel = ctx.author.voice.channel
    return await channel.connect()


#Discord bot startup
@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    print('Connected to servers:')
    for guild in bot.guilds:
        tracked_servers.add(guild.id)
        print(guild.name)


@bot.command(name='play')
async def play(ctx, url):
    voice_channel = ctx.guild.voice_client
    if not voice_channel.is_connected():     
        voice_channel = await join_channel(ctx)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']

    voice_channel.play(discord.FFmpegPCMAudio(url2), after=lambda e: print('done', e))



bot.run('heheheheheh')