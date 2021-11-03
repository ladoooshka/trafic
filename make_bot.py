from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def start(update, context):
    update.message.reply_text('Добрый день! \n Спасибо, что воспользовались сервисом аналитики трафика. Для продолжения выберите период, за который хотите получить информацию.')

def help(update, context):
    update.message.reply_text('Мы можем предоставить Вам информацию о движении трафика в учреждении.')

def error(update, context):
    update.message.reply_text('К сожалению, мы не можем предоставить Вам информацию.')

def text_1(update, context):
    text_received = update.message.text
    update.message.reply_text('Введите название организации, по которой необходима аналитика.')

def text_2(update, context):
    text_received = update.message.text
    update.message.reply_text('Введите ip-адреса, о которых хотите получить информацию.')
    
def main():
    TOKEN = '2090196710:AAF7Hg51203KoHfinVW495zXfX44EWrr82Y'

    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    
    if #here could be phone number dict. If number client there is in dict:

        dispatcher.add_handler(MessageHandler(Filters.text, text_1))
        dispatcher.add_handler(MessageHandler(Filters.text, text_2))
    
    else:
        dispatcher.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
