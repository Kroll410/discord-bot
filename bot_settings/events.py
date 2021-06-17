from setup import bot, MAIN_CHANNELS, GAMES, client


@bot.event
async def on_ready():
    print('Bot is ready')


@bot.event
async def on_member_update(before, after):
    from helpers import populate_channels
    if any([after.voice is None, before.voice is None]):
        return

    channel = after.voice.channel
    if channel in populate_channels(bot, MAIN_CHANNELS).values():
        return

    game = after.activity
    if game is None:
        await after.move_to(GAMES['talk_and_play_channel'])
    else:
        channel = populate_channels(bot, data=GAMES).get(after.activity.name, GAMES['wtf'])
        await after.move_to(channel)


@bot.event
async def on_message(message):
    if message.author == client.user:
        return

    if str(message.content).startswith('test'):
        await message.channel.send('пошёл нахуй')
