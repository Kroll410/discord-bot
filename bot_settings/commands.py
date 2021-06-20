import asyncio
import random

from discord.ext import commands as comm

from setup import bot, MAIN_CHANNELS, GAMES, FREE_CHANNELS, client, YURA_PHRAZES


class Fun(comm.Cog):
    def __init__(self, _bot):
        self.bot = _bot
        self._last_member = None

    @comm.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    @comm.command()
    @comm.has_role('СВЕРХРАЗУМ')
    async def humiliate(self, ctx, user_name):
        user = [x for x in ctx.guild.members if x.name == user_name][0]
        start_ch = user.voice.channel

        for i in range(7):
            v_ch = random.choice(ctx.guild.voice_channels)
            await user.move_to(v_ch)

            t_ch = random.choice(ctx.guild.text_channels)
            message = await t_ch.send(f'<@!{user.id}>')
            await message.delete()

            await asyncio.sleep(0.1)

        else:
            await user.move_to(start_ch)

    @humiliate.error
    async def humiliate_error(self, ctx, error):
        if isinstance(error, comm.CheckFailure):
            await ctx.send('соси :)')

    @comm.command()
    async def reload(self, ctx):
        self.bot.unload_extension('commands.py')
        self.bot.load_extension('commands.py')
        await ctx.send('заєбісь')


class Events(comm.Cog):

    def __init__(self, _bot):
        self.bot = _bot

    @comm.Cog.listener('on_member_update')
    async def on_member_update(self, before, after):
        from helpers import populate_channels
        if any([after.voice is None, before.voice is None]):
            return

        if str(before.voice.channel.id) in populate_channels(bot, MAIN_CHANNELS).keys():
            return
        else:
            user_activity = after.activity
            if user_activity in (ch := populate_channels(bot, GAMES)).keys():
                action = after.move_to(ch[after.activity])
            elif user_activity is None:
                action = after.move_to(populate_channels(bot, FREE_CHANNELS)['763136430745583677'])
            else:
                action = after.move_to(ch['wtf'])

            await action

    @comm.Cog.listener('on_message')
    async def on_message(self, message):
        if message.author == client.user:
            return
        if any(x in message.content for x in ['Юра', 'юра', 'пракоп', 'прокоп']):
            answer = random.choice(YURA_PHRAZES)
            if message.author.name == 'sasaddd':
                answer = random.choice([answer, YURA_PHRAZES[-1]])
            await message.channel.send(answer)


@bot.event
async def on_ready():
    print('Bot is ready')


bot.add_cog(Fun(bot))
bot.add_cog(Events(bot))
