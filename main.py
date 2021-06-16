import discord
from discord import Intents
from discord.ext import commands
import os

GAMES = {
    'Dota 2': 'Жопа 2🌈🍆',
    'Counter-Strike: Global Offensive': '╔ КС #1🔫',
    'Minecraft': 'Майн🟩🟫',
    'Dead by Daylight': 'ДБД🏃🪓',
    'wtf': 'Нейтралка🎮🪑',
    'talk_channel': 'Пиздёж🎭🚬'
}

MAIN_CHANNELS = {
    'БАЛДЬОЖ🍺👬🌚': 'БАЛДЬОЖ🍺👬🌚',
    'АЙЕМДІБІ ☔☕🎬': 'АЙЕМДІБІ ☔☕🎬',
    'ЙОБАНИЙ НУЛП📕🗿': 'ЙОБАНИЙ НУЛП📕🗿',
    'ЖМЖ 🚹❗': 'ЖМЖ 🚹❗',

}

intents = Intents.all()
bot = commands.Bot(command_prefix='-', intents=intents)


@bot.event
async def on_member_update(before, after):
    from population import populate_channels
    if any([after.voice is None, before.voice is None]):
        return

    main_channels = populate_channels(bot, MAIN_CHANNELS)
    if main_channels.get(after.activity.name) or \
            main_channels.get(before.activity.name):
        return

    game = after.activity

    if game is None:
        await after.move_to(GAMES['talk_channel'])
    else:
        channel = populate_channels(bot, data=GAMES).get(after.activity.name, GAMES['wtf'])
        await after.move_to(channel)


@bot.command()
async def rofl(ctx):
    print(dir(ctx))
    await ctx.send('Завали ебало')


client = discord.Client(guild_subscriptions=True)


@client.event
async def on_ready():
    print('Bot is ready')


@client.event
async def on_message(message):
    print(message)
    if message.author == client.user:
        return

    if str(message.content).startswith('test'):
        await message.channel.send('пошёл нахуй')


print("Server Running")
bot.run(os.environ.get('DISCORD_BOT_TOKEN'))
