import strings
from book import (GiveMode, Book)
from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
from book_db import BookRepository

NAME, AUTHOR, DESCRIPTION, LABELS, GIVEAWAY = range(5)

GIVE_MODES = {
        "Дать на время":GiveMode.RENT, 
        "Обменять":GiveMode.SWAP,
        "Подарить":GiveMode.GIVEAWAY
}

class AddCommandHandler(object):
    def __init__(self, book_repo):
       self._book = None
       self._book_repo = book_repo
   
    def start(self, bot, update):
        update.message.reply_text(strings.ADD_BOOK_NAME_TEXT)
        return NAME

    def name(self, bot, update):
        self._book = Book(update.message.text.title(), update.message.from_user)
        update.message.reply_text(strings.ADD_BOOK_AUTHOR_TEXT)
        return AUTHOR

    def author(self, bot, update):
        self._book.author = update.message.text.title()
        update.message.reply_text(strings.ADD_BOOK_DESCRIPTION_TEXT)
        return DESCRIPTION

    def description(self, bot, update):
        self._book.description = update.message.text
        update.message.reply_text(strings.ADD_BOOK_LABELS_TEXT)
        return LABELS

    def labels(self, bot, update):
        self._book.labels = update.message.text.split(' ')
        reply_keyboard = [['Дать на время', 'Обменять', 'Подарить']]
        update.message.reply_text(
        strings.ADD_BOOK_GIVEAWAY_TEXT,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        return GIVEAWAY

    def giveaway(self, bot, update):
        self._book.giveaway = GIVE_MODES[update.message.text]
        update.message.reply_text("Tnx")
        self._book_repo.add(self._book)
        return ConversationHandler.END

    def cancel(self, bot, update):
        user = update.message.from_user
        update.message.reply_text(strings.ADD_BOOK_CANCEL_TEXT,
                              reply_markup=ReplyKeyboardRemove())

        return ConversationHandler.END

    def handler(self):
        return ConversationHandler(
        entry_points=[CommandHandler('addbook', self.start)],

        states={
            NAME: [MessageHandler(Filters.text, self.name)],

            AUTHOR: [MessageHandler(Filters.text, self.author)],

            DESCRIPTION: [MessageHandler(Filters.text, self.description)],

            LABELS: [MessageHandler(Filters.text, self.labels)],
            
            GIVEAWAY: [MessageHandler(Filters.text, self.giveaway)],
        },

        fallbacks=[CommandHandler('cancel', self.cancel)]
        )