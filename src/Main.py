#########################################################
#                                               _       #
#  ___  ___  _   _ _ __ ___ ___    ___ ___   __| | ___  #
# / __|/ _ \| | | | '__/ __/ _ \  / __/ _ \ / _` |/ _ \ #
# \__ \ (_) | |_| | | | (_|  __/ | (_| (_) | (_| |  __/ #
# |___/\___/ \__,_|_|  \___\___|  \___\___/ \__,_|\___| #
#                                                       #
#########################################################

import discord
from discord.ext import commands, tasks

#REPLACE vars.py FILE WITH DECLARED VARS IN main()
from vars import TOKEN, ADMIN, EMBED_DEF

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
    bot.remove_command('help')

    BREADTIME = datetime.time(15,33) 

    @bot.event
    async def on_connect():
       print('bot connected!')
       logger.info('BOT CONNECTED TO SERVER')

    @bot.event
    async def on_disconnect():
        print('bot disconnected!')
        logger.info('BOT DISCONNECTED FROM SERVER')

    @bot.command()
    async def when(ctx, arg):
        if arg=='breadtime':
            if BREADTIME.hour > 12:
                await ctx.send('breadtime is {}:{} PM every day!'.format(BREADTIME.hour - 12, BREADTIME.minute))
            else:
                await ctx.send('breadtime is {}:{} AM every day!'.format(BREADTIME.hour, BREADTIME.minute))

    @bot.command()
    async def test(ctx):
        await ctx.send('this is the test function I hate it')

    @bot.command()
    async def bread(ctx):
        await ctx.send('why do we live in this world just to suffer. here :bread:')

    @bot.command()
    async def help(ctx, arg=''):
        if arg =='':
            await ctx.send(embed=EMBED_DEF)
    
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
