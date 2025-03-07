class Library:
    def __init__(self):
        """Initialize the Library with an empty book list and a book counter."""
        self.books = []  # List to store book names
        self.no_of_books = 0  # Counter for total books

    def add_book(self, book_name):
        """Adds a book to the library and updates the count."""
        self.books.append(book_name)
        self.no_of_books += 1
        print(f'Book "{book_name}" added successfully!')

    def get_book_count(self):
        """Returns the total number of books in the library."""
        return self.no_of_books

    def list_books(self):
        """Displays all books in the library."""
        if self.no_of_books == 0:
            print("No books available in the library.")
        else:
            print("Books in the Library:")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book}")

# Example Usage
library = Library()

# Adding books
library.add_book("Python")
library.add_book("PHP")
library.add_book("JavaScript")

# Getting the total book count
print(f"Total Books: {library.get_book_count()}")

# Listing all books
library.list_books()
