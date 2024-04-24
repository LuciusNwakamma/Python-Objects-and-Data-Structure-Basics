# This is a program that manages a library with various functionalities. This program cover various data
# structures like lists, sets, and classes for representing books, users, and the library itself.


# Define a class for books
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f'{self.title} by {self.author}'


# Create a class for managing the library
class Library:
    def __init__(self):
        self.books = []
        self.users = set()

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def register_user(self, user):
        self.users.add(user)

    def display_books(self):
        print("Library Catalog: ")
        for book in self.books:
            print(book)

    def display_users(self):
        print("Registered Users: ")
        for user in self.users:
            print(user)


# Create a class for representing users
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"


# Create a library object
library = Library()

# Create books

book1 = Book("Think and Grow Rich", "Napoleon Hill", "978-1-78844-102-5")
book2 = Book("The Richest Man in Babylon", "George S. Clason", "9781628614725")
book3 = Book("The Psychology of Money", "Morgan Housel", "9780857197689")

# Add books to library

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display books in  library
library.display_books()

# Create users
user1 = User("Melinda", "melinda@example.com")
user2 = User("Paschal", "paschal@example.com")

# Register users
library.register_user(user1)
library.register_user(user2)

# Display registered users
library.display_users()

# Remove a book from the library
library.remove_book(book2)

# Display books in library after removal
library.display_books()