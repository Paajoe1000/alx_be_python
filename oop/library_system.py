class Book:

    def __init__(self,title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.__class__.__name__}: {self.title} by {self.author}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}: {self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int) -> None:
        super().__init__(title, author)
        self.file_size = file_size
    def __str__(self):
        return f"{super().__str__()}, File Size: {self.file_size}KB"
    def __repr__(self):
        return f"{super().__str__()}, File Size: {self.file_size}KB"
    
class PrintBook(Book):
    def __init__(self, title, author, page_count: int) -> None:
        super().__init__(title, author)
        self.page_count = page_count
    def __str__(self):
        return f"{super().__str__()}, Page Count: {self.page_count}"
    def __repr__(self):
         return f"{super().__str__()}, Page Count: {self.page_count}"
    
class Library:
    def __init__(self, name_of_library: str = "") -> None:
        self.name = name_of_library
        self.books = []

    def add_book(self, book: Book) -> None:
        if book not in self.books:
            self.books.append(book)

    def list_books(self) -> None:
        if self.books:
            for item in self.books:
                print(item)
        else:
            print("The library is currently empty.")