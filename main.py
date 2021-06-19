import os
from setup import bot
from bot_settings.tasks import pidor_check

from bot_settings import *

os.environ['DISCORD_BOT_TOKEN'] = 'ODU0NDU5Mzg3ODUzOTMwNTA2.YMkPUQ.RvflISdovPh8QlvynX23eVzCTRo'
bot.loop.create_task(pidor_check())
bot.run(os.environ.get('DISCORD_BOT_TOKEN'))

