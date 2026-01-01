"""
Book class for the Library Management System
Demonstrates encapsulation and object-oriented design
"""

from datetime import datetime


class Book:
    """
    Represents a book in the library system.

    Attributes:
        title (str): The title of the book
        author (str): The author of the book
        isbn (str): The ISBN number (unique identifier)
        __available (bool): Private attribute for availability status
        __borrowed_by (str): Private attribute for member ID who borrowed the book
        __borrow_date (datetime): Private attribute for borrow date
    """

    def __init__(self, title, author, isbn):
        """
        Initialize a new Book object.

        Args:
            title (str): The title of the book
            author (str): The author of the book
            isbn (str): The ISBN number
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__available = True  # Private attribute (encapsulation)
        self.__borrowed_by = None
        self.__borrow_date = None

    # Getter methods (encapsulation)
    def is_available(self):
        """Check if the book is available for borrowing."""
        return self.__available

    def get_borrowed_by(self):
        """Get the member ID who borrowed this book."""
        return self.__borrowed_by

    def get_borrow_date(self):
        """Get the date when the book was borrowed."""
        return self.__borrow_date

    # Methods to modify private attributes (controlled access)
    def borrow(self, member_id):
        """
        Borrow the book if it's available.

        Args:
            member_id (str): The ID of the member borrowing the book

        Returns:
            bool: True if borrowing was successful, False otherwise
        """
        if self.__available:
            self.__available = False
            self.__borrowed_by = member_id
            self.__borrow_date = datetime.now()
            return True
        return False

    def return_book(self):
        """
        Return the book to the library.

        Returns:
            bool: True if return was successful, False otherwise
        """
        if not self.__available:
            self.__available = True
            self.__borrowed_by = None
            self.__borrow_date = None
            return True
        return False

    def get_info(self):
        """
        Get formatted information about the book.

        Returns:
            str: Formatted book information
        """
        status = (
            "Available" if self.__available else f"Borrowed by {self.__borrowed_by}"
        )
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nStatus: {status}"

    def to_dict(self):
        """
        Convert book data to dictionary for storage.

        Returns:
            dict: Book data as dictionary
        """
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.__available,
            "borrowed_by": self.__borrowed_by,
            "borrow_date": (
                self.__borrow_date.isoformat() if self.__borrow_date else None
            ),
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a Book object from dictionary data.

        Args:
            data (dict): Dictionary containing book data

        Returns:
            Book: A new Book object
        """
        book = cls(data["title"], data["author"], data["isbn"])
        book.__available = data["available"]
        book.__borrowed_by = data["borrowed_by"]
        if data["borrow_date"]:
            book.__borrow_date = datetime.fromisoformat(data["borrow_date"])
        return book

    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

    def __repr__(self):
        """Developer-friendly representation of the book."""
        return f"Book('{self.title}', '{self.author}', '{self.isbn}')"
