#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Bot which facilitates book exchange in chats
# This program is dedicated to the public domain under the CC0 license.

import logging
import strings
from book import Book
from addcommandhandler import AddCommandHandler
from book_db import BookRepository
from telegram.ext import Updater, CommandHandler, Filters
from telegram import ParseMode

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
  # TODO persistance
repo = BookRepository()

def start(bot, update):
    update.message.reply_text(
        strings.START_TEXT)

def help(bot, update):
    update.message.reply_text(
        strings.HELP_TEXT)

def booklist(bot, update):
    book_list_str = '\n'.join(map(str, repo.get_all()))
    logger.info(book_list_str)
    bot.send_message(chat_id=update.message.chat_id, text=book_list_str, parse_mode=ParseMode.HTML)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    conversation = AddCommandHandler(repo)
    updater = Updater("")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(conversation.handler())
    dp.add_handler(CommandHandler("list", booklist))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
