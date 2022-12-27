from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from spy import *
from fractions import Fraction

def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Привет, {update.effective_user.first_name}! Посчитаем?\nНе знаешь, что делать? Введи /help')

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text('Сложение: /sum_help\nВычитание: /sub_help\nУмножение: /mult_help\nДеление: /div_help')

def help_sum_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text('Сложение:\nдля простых чисел: /sum число_1 число_2\nдля комплексных чисел: /сsum число_1 число_2 (числа вводи в формате a+bj)\nдля рациональных чисел: /fsum число_1 число_2 (числа вводи в формате a/b)')
def help_sub_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text('Вычитание:\nдля простых чисел: /sub число_1 число_2\nдля комплексных чисел: /сsub число_1 число_2 (числа вводи в формате a+bj)\nдля рациональных чисел: /fsub число_1 число_2 (числа вводи в формате a/b)')
def help_mult_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text('Умножение:\nдля простых чисел: /mult число_1 число_2\nдля комплексных чисел: /сmult число_1 число_2 (числа вводи в формате a+bj)\nдля рациональных чисел: /fmult число_1 число_2 (числа вводи в формате a/b)')
def help_div_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text('Деление:\nдля простых чисел: /div число_1 число_2\nдля комплексных чисел: /сdiv число_1 число_2 (числа вводи в формате a+bj)\nдля рациональных чисел: /fdiv число_1 число_2 (числа вводи в формате a/b)')


def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')

def sub_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} - {y} = {x-y}')
def mult_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} * {y} = {x*y}')
def div_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    if y != 0:
        update.message.reply_text(f'{x} / {y} = {x/y}')
    else:
        update.message.reply_text('На 0 делить нельзя! Попробуй еще раз!')

def complex_sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')

def complex_sub_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} - {y} = {x-y}')
def complex_mult_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = complex(items[1])
    y = complex(items[2])
    update.message.reply_text(f'{x} * {y} = {x*y}')
def complex_div_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = complex(items[1])
    y = complex(items[2])
    if y != 0:
        update.message.reply_text(f'{x} / {y} = {x / y}')
    else:
        update.message.reply_text('На 0 делить нельзя! Попробуй еще раз!')
def fractions_sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = Fraction(items[1])
    y = Fraction(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')
def fractions_sub_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = Fraction(items[1])
    y = Fraction(items[2])
    update.message.reply_text(f'{x} - {y} = {x-y}')
def fractions_mult_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = Fraction(items[1])
    y = Fraction(items[2])
    update.message.reply_text(f'{x} * {y} = {x*y}')
def fractions_div_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = Fraction(items[1])
    y = Fraction(items[2])
    if y != 0:
        update.message.reply_text(f'{x} / {y} = {x / y}')
    else:
        update.message.reply_text('На 0 делить нельзя! Попробуй еще раз!')

