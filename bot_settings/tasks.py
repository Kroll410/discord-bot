from asyncio import sleep
from random import randint

import discord
from discord.ext import tasks

from setup import bot


@tasks.loop(minutes=45)
async def mytask():
    from discord import FFmpegPCMAudio
    try:
        # text_channel = bot.get_channel(854474908293529610)
        # await text_channel.send('я еблан')
        for channel in bot.get_all_channels():
            if isinstance(channel, discord.VoiceChannel):
                if len(channel.members) >= 1:
                    x = await channel.connect()
                    x.play(
                        source=FFmpegPCMAudio(executable='ffmpeg', source=f'mp3/{randint(1, 4)}.mp3'),
                    )
                    while x.is_playing():
                        await sleep(1)
                    await x.disconnect()

    except (IndexError, AttributeError) as error:
        print(error)
        return

mytask.start()
