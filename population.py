def populate(bot, data):
    key_list = list(data.keys())
    val_list = list(data.values())

    for v_channel in bot.guilds[0].voice_channels:
        if (name := v_channel.name) in val_list:
            pos = val_list.index(name)
            game = key_list[pos]
            data[game] = v_channel

    return data


