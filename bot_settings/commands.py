from discord.ext import commands

from setup import bot


# test
class Greetings(commands.Cog):

    @commands.command(pass_context=True)
    async def test(self, ctx, arg):
        print('here')
        await bot.say(arg)

    @commands.command(pass_context=True)
    async def cmd(self, ctx):
        await ctx.send('gavno')


bot.add_cog(Greetings())
