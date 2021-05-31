import discord
from discord.ext import commands, tasks

from vars import INSERT_TOKEN, INSERT_ADMIN

def main():
    bot = commands.Bot(command_prefix='.')
    
    @bot.event
    async def on_connect():
       print('bot connected!')

    @bot.event
    async def on_disconnect():
        print('bot disconnected!')

    @bot.command()
    async def test(ctx):
        await ctx.send('ah shit im back')

    @bot.command()
    async def admin(ctx, arg):
        if ctx.author == INSERT_ADMIN or arg == 'disconnect':
            await bot.close()

    
    bot.run(INSERT_TOKEN)

if __name__ == '__main__':
    main()
