import asyncio
import random

import discord
from discord.ext import tasks

from helpers.sounds import create_concat_sound, delete_concat_sound
from setup import bot


async def pidor_check():
    await bot.wait_until_ready()
    await asyncio.sleep(18000)

    from discord import FFmpegPCMAudio
    while True:
        for channel in bot.get_all_channels():
            if isinstance(channel, discord.VoiceChannel):
                if len(channel.members) >= 1:
                    user_name = random.choice([x.name for x in channel.members if not x.bot])
                    path = create_concat_sound(user_name)
                    x = await channel.connect()
                    x.play(
                        source=FFmpegPCMAudio(executable='ffmpeg', source=f'{path}')
                    )

                    while x.is_playing():
                        await asyncio.sleep(1)
                    await x.disconnect()
                    await asyncio.sleep(1)

        await asyncio.sleep(18000)
        delete_concat_sound()