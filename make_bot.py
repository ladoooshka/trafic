from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

token = '2090196710:AAF7Hg51203KoHfinVW495zXfX44EWrr82Y'
updater = Updater(TOKEN = token, use_contex = True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Добрый день! \n Спасибо, что воспользовались сервисом аналитики трафика. Для продолжения выберите период, за который хотите получить информацию.')

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()