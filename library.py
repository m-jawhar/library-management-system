"""
Library class for the Library Management System
Central class that manages all books, members, and operations
"""

from book import Book
from member import Member
from librarian import Librarian


class Library:
    """
    Represents the library system that manages books and members.

    Attributes:
        name (str): The name of the library
        __books (dict): Private dictionary of books (ISBN -> Book object)
        __members (dict): Private dictionary of members (member_id -> Member object)
        __librarians (dict): Private dictionary of librarians (librarian_id -> Librarian object)
    """

    def __init__(self, name="City Library"):
        """
        Initialize a new Library object.

        Args:
            name (str): The name of the library
        """
        self.name = name
        self.__books = {}  # Private attribute (encapsulation)
        self.__members = {}  # Private attribute (encapsulation)
        self.__librarians = {}  # Private attribute (encapsulation)

    # Book management methods
    def add_book(self, book):
        """
        Add a book to the library.

        Args:
            book (Book): The Book object to add

        Returns:
            bool: True if book was added, False if ISBN already exists
        """
        if book.isbn not in self.__books:
            self.__books[book.isbn] = book
            return True
        return False

    def remove_book(self, isbn):
        """
        Remove a book from the library.

        Args:
            isbn (str): The ISBN of the book to remove

        Returns:
            bool: True if book was removed, False if not found or currently borrowed
        """
        if isbn in self.__books:
            book = self.__books[isbn]
            if book.is_available():
                del self.__books[isbn]
                return True
        return False

    def find_book_by_isbn(self, isbn):
        """
        Find a book by its ISBN.

        Args:
            isbn (str): The ISBN to search for

        Returns:
            Book: The Book object if found, None otherwise
        """
        return self.__books.get(isbn)

    def find_books_by_title(self, title):
        """
        Find books by title (partial match, case-insensitive).

        Args:
            title (str): The title to search for

        Returns:
            list: List of Book objects matching the title
        """
        title_lower = title.lower()
        return [
            book for book in self.__books.values() if title_lower in book.title.lower()
        ]

    def find_books_by_author(self, author):
        """
        Find books by author (partial match, case-insensitive).

        Args:
            author (str): The author to search for

        Returns:
            list: List of Book objects by the author
        """
        author_lower = author.lower()
        return [
            book
            for book in self.__books.values()
            if author_lower in book.author.lower()
        ]

    def get_all_books(self):
        """
        Get all books in the library.

        Returns:
            list: List of all Book objects
        """
        return list(self.__books.values())

    def get_available_books(self):
        """
        Get all available books in the library.

        Returns:
            list: List of available Book objects
        """
        return [book for book in self.__books.values() if book.is_available()]

    def get_borrowed_books(self):
        """
        Get all borrowed books in the library.

        Returns:
            list: List of borrowed Book objects
        """
        return [book for book in self.__books.values() if not book.is_available()]

    # Member management methods
    def register_member(self, member):
        """
        Register a new member.

        Args:
            member (Member): The Member object to register

        Returns:
            bool: True if member was registered, False if ID already exists
        """
        if member.member_id not in self.__members:
            self.__members[member.member_id] = member
            return True
        return False

    def remove_member(self, member_id):
        """
        Remove a member from the library.

        Args:
            member_id (str): The ID of the member to remove

        Returns:
            bool: True if member was removed, False if not found or has borrowed books
        """
        if member_id in self.__members:
            member = self.__members[member_id]
            if member.get_borrowed_count() == 0:
                del self.__members[member_id]
                return True
        return False

    def find_member(self, member_id):
        """
        Find a member by their ID.

        Args:
            member_id (str): The member ID to search for

        Returns:
            Member: The Member object if found, None otherwise
        """
        return self.__members.get(member_id)

    def get_all_members(self):
        """
        Get all registered members.

        Returns:
            list: List of all Member objects
        """
        return list(self.__members.values())

    # Librarian management methods
    def add_librarian(self, librarian):
        """
        Add a librarian to the system.

        Args:
            librarian (Librarian): The Librarian object to add

        Returns:
            bool: True if librarian was added, False if ID already exists
        """
        if librarian.librarian_id not in self.__librarians:
            self.__librarians[librarian.librarian_id] = librarian
            return True
        return False

    def find_librarian(self, librarian_id):
        """
        Find a librarian by their ID.

        Args:
            librarian_id (str): The librarian ID to search for

        Returns:
            Librarian: The Librarian object if found, None otherwise
        """
        return self.__librarians.get(librarian_id)

    def get_all_librarians(self):
        """
        Get all librarians.

        Returns:
            list: List of all Librarian objects
        """
        return list(self.__librarians.values())

    # Borrowing and returning operations
    def borrow_book(self, member_id, isbn):
        """
        Process a book borrowing transaction.

        Args:
            member_id (str): The ID of the member borrowing the book
            isbn (str): The ISBN of the book to borrow

        Returns:
            tuple: (success: bool, message: str)
        """
        member = self.find_member(member_id)
        if not member:
            return False, "Member not found"

        book = self.find_book_by_isbn(isbn)
        if not book:
            return False, "Book not found"

        if not book.is_available():
            return False, "Book is not available"

        if book.borrow(member_id) and member.borrow_book(isbn):
            return True, f"Book '{book.title}' borrowed successfully"

        return False, "Failed to borrow book"

    def return_book(self, member_id, isbn):
        """
        Process a book return transaction.

        Args:
            member_id (str): The ID of the member returning the book
            isbn (str): The ISBN of the book to return

        Returns:
            tuple: (success: bool, message: str)
        """
        member = self.find_member(member_id)
        if not member:
            return False, "Member not found"

        book = self.find_book_by_isbn(isbn)
        if not book:
            return False, "Book not found"

        if not member.has_borrowed(isbn):
            return False, "Member has not borrowed this book"

        if book.return_book() and member.return_book(isbn):
            return True, f"Book '{book.title}' returned successfully"

        return False, "Failed to return book"

    # Statistics methods
    def get_statistics(self):
        """
        Get library statistics.

        Returns:
            dict: Dictionary containing various statistics
        """
        total_books = len(self.__books)
        available_books = len(self.get_available_books())
        borrowed_books = len(self.get_borrowed_books())
        total_members = len(self.__members)

        return {
            "total_books": total_books,
            "available_books": available_books,
            "borrowed_books": borrowed_books,
            "total_members": total_members,
        }

    def __str__(self):
        """String representation of the library."""
        stats = self.get_statistics()
        return (
            f"{self.name}\n"
            f"Books: {stats['total_books']} (Available: {stats['available_books']}, "
            f"Borrowed: {stats['borrowed_books']})\n"
            f"Members: {stats['total_members']}"
        )

    def __repr__(self):
        """Developer-friendly representation of the library."""
        return f"Library('{self.name}')"
