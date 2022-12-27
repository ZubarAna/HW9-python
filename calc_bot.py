import os

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from fractions import Fraction
from bot_commands import *
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('tg_token')
updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum_help', help_sum_command))
updater.dispatcher.add_handler(CommandHandler('sub_help', help_sub_command))
updater.dispatcher.add_handler(CommandHandler('mult_help', help_mult_command))
updater.dispatcher.add_handler(CommandHandler('div_help', help_div_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('sub', sub_command))
updater.dispatcher.add_handler(CommandHandler('mult', mult_command))
updater.dispatcher.add_handler(CommandHandler('div', div_command))
updater.dispatcher.add_handler(CommandHandler('csum', complex_sum_command))
updater.dispatcher.add_handler(CommandHandler('csub', complex_sub_command))
updater.dispatcher.add_handler(CommandHandler('cmult', complex_mult_command))
updater.dispatcher.add_handler(CommandHandler('cdiv', complex_div_command))
updater.dispatcher.add_handler(CommandHandler('fsum', fractions_sum_command))
updater.dispatcher.add_handler(CommandHandler('fsub', fractions_sub_command))
updater.dispatcher.add_handler(CommandHandler('fmult', fractions_mult_command))
updater.dispatcher.add_handler(CommandHandler('fdiv', fractions_div_command))


print('server start')
updater.start_polling()
updater.idle()
