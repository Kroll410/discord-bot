import os
from bot_settings.tasks import pidor_check

os.environ['DISCORD_BOT_TOKEN'] = 'ODU0NDU5Mzg3ODUzOTMwNTA2.YMkPUQ.RlPS_guawxAZFRN9Y2eDlM9QbEQ'

from bot_settings.commands import *
from setup import bot

bot.loop.create_task(pidor_check())
bot.run(os.environ.get('DISCORD_BOT_TOKEN'))
