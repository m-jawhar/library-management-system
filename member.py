"""
Member class for the Library Management System
Represents a library member who can borrow books
"""

from datetime import datetime


class Member:
    """
    Represents a library member.

    Attributes:
        name (str): The name of the member
        member_id (str): Unique identifier for the member
        __borrowed_books (list): Private list of borrowed book ISBNs
        __registration_date (datetime): Private attribute for registration date
    """

    def __init__(self, name, member_id):
        """
        Initialize a new Member object.

        Args:
            name (str): The name of the member
            member_id (str): Unique identifier for the member
        """
        self.name = name
        self.member_id = member_id
        self.__borrowed_books = []  # Private attribute (encapsulation)
        self.__registration_date = datetime.now()

    # Getter methods (encapsulation)
    def get_borrowed_books(self):
        """
        Get a copy of the list of borrowed book ISBNs.
        Returns a copy to prevent external modification.
        """
        return self.__borrowed_books.copy()

    def get_registration_date(self):
        """Get the member's registration date."""
        return self.__registration_date

    def get_borrowed_count(self):
        """Get the number of books currently borrowed."""
        return len(self.__borrowed_books)

    # Methods to modify private attributes (controlled access)
    def borrow_book(self, isbn):
        """
        Add a book to the member's borrowed list.

        Args:
            isbn (str): The ISBN of the book being borrowed

        Returns:
            bool: True if successful, False if already borrowed
        """
        if isbn not in self.__borrowed_books:
            self.__borrowed_books.append(isbn)
            return True
        return False

    def return_book(self, isbn):
        """
        Remove a book from the member's borrowed list.

        Args:
            isbn (str): The ISBN of the book being returned

        Returns:
            bool: True if successful, False if book wasn't borrowed
        """
        if isbn in self.__borrowed_books:
            self.__borrowed_books.remove(isbn)
            return True
        return False

    def has_borrowed(self, isbn):
        """
        Check if the member has borrowed a specific book.

        Args:
            isbn (str): The ISBN to check

        Returns:
            bool: True if the member has borrowed this book
        """
        return isbn in self.__borrowed_books

    def get_info(self):
        """
        Get formatted information about the member.

        Returns:
            str: Formatted member information
        """
        books_count = len(self.__borrowed_books)
        reg_date = self.__registration_date.strftime("%Y-%m-%d")
        return (
            f"Name: {self.name}\n"
            f"Member ID: {self.member_id}\n"
            f"Registered: {reg_date}\n"
            f"Books Borrowed: {books_count}"
        )

    def to_dict(self):
        """
        Convert member data to dictionary for storage.

        Returns:
            dict: Member data as dictionary
        """
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.__borrowed_books.copy(),
            "registration_date": self.__registration_date.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a Member object from dictionary data.

        Args:
            data (dict): Dictionary containing member data

        Returns:
            Member: A new Member object
        """
        member = cls(data["name"], data["member_id"])
        member.__borrowed_books = data["borrowed_books"]
        member.__registration_date = datetime.fromisoformat(data["registration_date"])
        return member

    def __str__(self):
        """String representation of the member."""
        return f"{self.name} (ID: {self.member_id})"

    def __repr__(self):
        """Developer-friendly representation of the member."""
        return f"Member('{self.name}', '{self.member_id}')"
