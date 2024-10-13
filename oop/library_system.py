class Book:

    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title)
        super().__init__(author)
        self.file_size = int(file_size)
    def __str__(self):
        return f"{self.title} by {self.author}, {self.file_size}"
    
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title)
        super().__init__(author)
        self.page_count = int(page_count)
    def __str__(self):
        return f"{self.title} by {self.author}, {self.page_count}"
    
class Library(Book):
    def __init__(self, books):
        self.books = []

    def add_book(self, book):
        if book is not in self.books:
            self.books.append(book)

    def list_books(self):
        if self.books:
            for item in self.books:
                print(item)
        else:
            print("The library is currently empty.")
            
    def __str__(self, title, author):
        return f"Book: {self.title} by {self.author}"
    
    def __str__(self, title, author, file_size):
        self.file_size = int(file_size)
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}"
    
    def __str__(self, title, author, page_count):
        self.page_count = int(page_count)
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

    def list_books(self):
        self.books()