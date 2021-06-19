from setup import bot, MAIN_CHANNELS, GAMES, client


@bot.event
async def on_ready():
    print('Bot is ready')


@bot.event
async def on_member_update(before, after):
    from helpers import populate_channels
    if any([after.voice is None, before.voice is None]):
        return

    if str(before.voice.channel.id) in populate_channels(bot, MAIN_CHANNELS).keys():
        return
    else:
        if after.activity in (ch := populate_channels(bot, GAMES)).keys():
            await after.move_to(ch[after.activity])
        else:
            await after.move_to(ch['wtf'])

        if after.activity is None:
            await after.move_to(populate_channels(bot, MAIN_CHANNELS)['855157821988667432'])

@bot.event
async def on_message(message):
    if message.author == client.user:
        return
    if any(x in message.content for x in ['Юра', 'юра', 'пракоп', 'прокоп']):
        await message.channel.send('іди нахуй')
