class Book:

    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title)
        super().__init__(author)
        self.file_size = int(file_size)
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}"
    
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title)
        super().__init__(author)
        self.page_count = int(page_count)
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
    
class Library(Book):
    def __init__(self, books):
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)

    def list_books(self):
        if self.books:
            for item in self.books:
                print(item)
        else:
            print("The library is currently empty.")