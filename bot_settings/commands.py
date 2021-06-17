from setup import bot


@bot.command()
async def rofl(ctx):
    print('here')
    await ctx.send('/tts Завали ебало')


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg, tts=True)
