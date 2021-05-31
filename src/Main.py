import discord
from discord.ext import commands, tasks

import logging

from vars import INSERT_TOKEN

def main():
    #SETTING UP LOGGER
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='main.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

    #INIT BOT
    bot = commands.Bot(command_prefix='.')

    @bot.command()
    async def test(ctx):
        await ctx.send('ah shit im back')
    
    bot.run(INSERT_TOKEN)

if __name__ == '__main__':
    main()
