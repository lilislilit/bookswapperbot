#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Bot which facilitates book exchange in chats
# This program is dedicated to the public domain under the CC0 license.

import logging
import strings
from book import Book
from telegram.ext import Updater, CommandHandler, Filters
from telegram import ParseMode

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

book_list = []  # TODO persistance


def start(bot, update):
    update.message.reply_text(
        strings.START_TEXT)


def help(bot, update):
    update.message.reply_text(
        strings.HELP_TEXT)


def addbook(bot, update, args):
    book = Book(name=' '.join(args), owner=update.message.from_user)
    book.labels = ["Algo", "Design"]
    book.description = "Sample Description Sample Description Sample Description Sample Description Sample Description"
    book_list.append(book)


def booklist(bot, update):
    book_list_str = '\n'.join(map(str, book_list))
    logger.info(book_list_str)
    bot.send_message(chat_id=update.message.chat_id, text=book_list_str, parse_mode=ParseMode.HTML)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    updater = Updater("")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    # TODO implement conversation handlers
    dp.add_handler(CommandHandler("addbook", addbook, pass_args=True))
    dp.add_handler(CommandHandler("list", booklist))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
