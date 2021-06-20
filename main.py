import os
from bot_settings.tasks import pidor_check

from bot_settings.commands import *
from setup import bot

bot.loop.create_task(pidor_check())
bot.run(os.environ.get('DISCORD_BOT_TOKEN'))
