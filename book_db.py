class BookRepository(object):
    def __init__(self):
        self._books = []
    
    def add(self, book):
        self._books.append(book)

    def get_all(self):
        return self._books
    