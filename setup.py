import discord
from discord import Intents
from discord.ext import commands

GAMES = {
    'Dota 2': '853200492914147338',
    'Counter-Strike: Global Offensive': '853202820949082143',
    'Minecraft': '853205810368479252',
    'Dead by Daylight': '853203999539724289',
    'wtf': '853205018215579648',
}

MAIN_CHANNELS = {
    '663347613076160513': '663347613076160513',
    '665699077614338048': '665699077614338048',
    '785181229871661087': '785181229871661087',
    '766718828008570921': '766718828008570921',
    '855157821988667432': '855157821988667432',
    '734001194493804614': '734001194493804614',

}

intents = Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)
client = discord.Client(guild_subscriptions=True)


