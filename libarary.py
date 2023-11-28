class Book:
    def __init__(self, title, author, isbn, number_of_pages, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.number_of_pages = number_of_pages
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}") 
        print(f"Author: {self.author} ") 
        print(f"ISBN: {self.isbn} ")
        print(f"Pages: {self.number_of_pages}") 
        print(f"Price: {self.price}")


class ReferenceBook(Book):
    def __init__(self, title, author, isbn, number_of_pages, price, reference_type):
        super().__init__(title, author, isbn, number_of_pages, price)
        self.reference_type = reference_type

    def display_details(self):
        super().display_details()
        print(f"reference book: {self.reference_type}")


class FictionBook(Book):
    def __init__(self, title, author, isbn, number_of_pages, price, genre):
        super().__init__(title, author, isbn, number_of_pages, price)
        self.genre = genre

    def display_details(self):
        super().display_details()
        print(f"genre of book: {self.genre}")


class Library:
    
    books = {}

    def add_book(self, book):
        self.books[book.title] = book

    def display_all_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books.values():
                book.display_details()
                print("\n")
        else:
            print("The library is empty.")
            

    def search_book_by_title(self, title):
        return self.books.get(title)

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f"Book have been removed from the library.")

    def print_all_books(self):

        for title in self.books:
            print("Available book in library: ")
            print(title)



reference_book_title = input("Enter the title of the reference book: ")
reference_book_author = input("Enter the author of the reference book: ")
reference_book_isbn = input("Enter the ISBN of the reference book: ")
reference_book_pages = int(input("Enter the number of pages of the reference book: "))
reference_book_price = float(input("Enter the price of the reference book: "))
reference_book_type = input("Enter the type of reference: ")

print("\n")

fiction_book_title = input("Enter the title of the fiction book: ")
fiction_book_author = input("Enter the author of the fiction book: ")
fiction_book_isbn = input("Enter the ISBN of the fiction book: ")
fiction_book_pages = int(input("Enter the number of pages of the fiction book: "))
fiction_book_price = float(input("Enter the price of the fiction book: "))
fiction_book_genre = input("Enter the genre of the fiction book: ")

reference_book = ReferenceBook(reference_book_title, reference_book_author, reference_book_isbn, reference_book_pages, reference_book_price, reference_book_type)
fiction_book = FictionBook(fiction_book_title, fiction_book_author, fiction_book_isbn, fiction_book_pages, fiction_book_price, fiction_book_genre)

library = Library()
library.add_book(reference_book)
library.add_book(fiction_book)

print("\n")

library.display_all_books()

print("\n")

title_to_search = input("Enter the title of the book to search for: ")
search_result = library.search_book_by_title(title_to_search)

print("\n")

if search_result:
    print("Details of search book: ")
    search_result.display_details()
else:
    print("\nBook not found.")

print("\n")


title_to_remove = input("Enter the title of the book to remove: ")
library.remove_book(title_to_remove)

print("\n")

library.print_all_books()