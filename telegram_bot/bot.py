import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram_bot.settings as settings


logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context):
    print('Start is called')
    update.message.reply_text('Hello, user! You are called command /start')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    bot = Updater(settings.API_KEY)

    dp = bot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot is started')

    bot.start_polling()
    bot.idle()


if __name__ == '__main__':
    main()
