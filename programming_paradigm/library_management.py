# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title      # Public attribute: book title
        self.author = author    # Public attribute: book author
        self._is_checked_out = False  # Private attribute: availability (checked out or not)

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
        else:
            return f"'{self.title}' is already checked out."

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
        else:
            return f"'{self.title}' was not checked out."

    def is_available(self):
        """Check if the book is available (not checked out)."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    return f"Checked out '{title}'"
                else:
                    return f"'{title}' is already checked out."
        return f"'{title}' not found in the library."

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    return f"Returned '{title}'"
                else:
                    return f"'{title}' was not checked out."
        return f"'{title}' not found in the library."

    def list_available_books(self):
        """List all available (not checked out) books."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            return "\n".join([f"{book.title} by {book.author}" for book in available_books])
        else:
            return "No books available."
