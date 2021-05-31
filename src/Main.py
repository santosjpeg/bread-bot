import discord
from discord.ext import commands, tasks

from vars import INSERT_TOKEN

def main():
    bot = commands.Bot(command_prefix='.')

    @bot.command()
    async def test(ctx):
        await ctx.send('ah shit im back')
    
    bot.run(INSERT_TOKEN)

if __name__ == '__main__':
    main()
