import discord
from discord import Intents
from discord.ext import commands

GAMES = {
    'Dota 2': 'Жопа 2🌈🍆',
    'Counter-Strike: Global Offensive': '╔ КС #1🔫',
    'Minecraft': 'Майн🟩🟫',
    'Dead by Daylight': 'ДБД🏃🪓',
    'wtf': 'Нейтралка🎮🪑',
    'talk_and_play_channel': 'Freeplay & talk 👾🙌'
}

MAIN_CHANNELS = {
    'БАЛДЬОЖ🍺👬🌚': 'БАЛДЬОЖ🍺👬🌚',
    'АЙЕМДІБІ ☔☕🎬': 'АЙЕМДІБІ ☔☕🎬',
    'ЙОБАНИЙ НУЛП📕🗿': 'ЙОБАНИЙ НУЛП📕🗿',
    'ЖМЖ 🚹❗': 'ЖМЖ 🚹❗',
    'Стримы🟣📺': 'Стримы🟣📺',
    'Freeplay & talk 👾🙌': 'Freeplay & talk 👾🙌',

}

intents = Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)
client = discord.Client(guild_subscriptions=True)


