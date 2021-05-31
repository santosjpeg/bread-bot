########################################################
#                                              _       #
# ___  ___  _   _ _ __ ___ ___    ___ ___   __| | ___  #
#/ __|/ _ \| | | | '__/ __/ _ \  / __/ _ \ / _` |/ _ \ #
#\__ \ (_) | |_| | | | (_|  __/ | (_| (_) | (_| |  __/ #
#|___/\___/ \__,_|_|  \___\___|  \___\___/ \__,_|\___| #
#                                                      #
########################################################

import discord
from discord.ext import commands, tasks

#REPLACE vars.py FILE WITH DECLARED VARS IN main()
from vars import INSERT_TOKEN, INSERT_ADMIN

#misc libraries
import logging 

import datetime
from datetime import datetime as dt

def main():
    #SETTING UP LOGGER
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='main.log',encoding='utf-8',mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

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
