import discord
from discord import Intents
from discord.ext import commands
import config

GAMES = {
    'Dota 2': 'Жопа 2🌈🍆',
    'Counter-Strike: Global Offensive': '╔ КС #1🔫',
    'Minecraft': 'Майн🟩🟫',
    'Dead by Daylight': 'ДБД🏃🪓',
    'wtf': 'Нейтралка🎮🪑'
}

client = discord.Client(guild_subscriptions=True)


@client.event
async def on_ready():
    print('Bot is ready')


@client.event
async def on_message(message):
    print(message)
    if message.author == client.user:
        return

    if str(message.content).startswith('$hello'):
        await message.channel.send('Hello!')


intents = Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_member_update(before, after):
    from population import populate
    if any([after.activity is None, after.voice is None, before.voice is None]):
        return

    channel = populate(bot, data=GAMES).get(after.activity.name, GAMES['wtf'])
    if channel:
        await after.move_to(channel)
    else:
        await after.move_to('test')


print("Server Running")
bot.run(config.Config.TOKEN)
