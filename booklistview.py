from telegram import InlineKeyboardMarkup, InlineKeyboardButton

PAGE_LENGTH = 5 

class ListView(object):
    def __init__(self, books, page = 0):
        self._books = books
        self._page = page

    def __str__(self):
        preface = f'мы нашли {len(self._books)} книжек в библиотеке чата:\n'
        return preface + '\n'.join(map(str, self._books[self._page*PAGE_LENGTH:self.pages()*PAGE_LENGTH]))

    def pages(self):
        return len(self._books) + 1 // 5

    @property
    def keyboard(self):
        button_list = [InlineKeyboardButton(i, callback_data=i) for i in range(self.pages())]
        return InlineKeyboardMarkup([button_list])
