def populate_channels(bot, data):
    key_list = list(data.keys())
    val_list = list(data.values())

    for v_channel in bot.guilds[0].voice_channels:
        if (ch_id := str(v_channel.id)) in val_list:
            pos = val_list.index(ch_id)
            key = key_list[pos]
            data[key] = v_channel
    return data


