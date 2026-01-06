"""
Data Persistence Module for Library Management System
Handles saving and loading data to/from text files
"""

import json
import os
from book import Book
from member import Member
from librarian import Librarian


class DataManager:
    """
    Manages data persistence for the library system.
    Saves and loads data to/from JSON files.
    """

    def __init__(self, data_directory="data"):
        """
        Initialize the DataManager.

        Args:
            data_directory (str): Directory where data files will be stored
        """
        self.data_directory = data_directory
        self.books_file = os.path.join(data_directory, "books.json")
        self.members_file = os.path.join(data_directory, "members.json")
        self.librarians_file = os.path.join(data_directory, "librarians.json")

        # Create data directory if it doesn't exist
        if not os.path.exists(data_directory):
            os.makedirs(data_directory)

    def save_books(self, books):
        """
        Save all books to a JSON file.

        Args:
            books (dict): Dictionary of Book objects (ISBN -> Book)

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            books_data = {isbn: book.to_dict() for isbn, book in books.items()}
            with open(self.books_file, "w") as f:
                json.dump(books_data, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving books: {e}")
            return False

    def load_books(self):
        """
        Load all books from the JSON file.

        Returns:
            dict: Dictionary of Book objects (ISBN -> Book), empty if file doesn't exist
        """
        if not os.path.exists(self.books_file):
            return {}

        try:
            with open(self.books_file, "r") as f:
                books_data = json.load(f)

            books = {}
            for isbn, data in books_data.items():
                books[isbn] = Book.from_dict(data)
            return books
        except Exception as e:
            print(f"Error loading books: {e}")
            return {}

    def save_members(self, members):
        """
        Save all members to a JSON file.

        Args:
            members (dict): Dictionary of Member objects (member_id -> Member)

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            members_data = {
                member_id: member.to_dict() for member_id, member in members.items()
            }
            with open(self.members_file, "w") as f:
                json.dump(members_data, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving members: {e}")
            return False

    def load_members(self):
        """
        Load all members from the JSON file.

        Returns:
            dict: Dictionary of Member objects (member_id -> Member), empty if file doesn't exist
        """
        if not os.path.exists(self.members_file):
            return {}

        try:
            with open(self.members_file, "r") as f:
                members_data = json.load(f)

            members = {}
            for member_id, data in members_data.items():
                members[member_id] = Member.from_dict(data)
            return members
        except Exception as e:
            print(f"Error loading members: {e}")
            return {}

    def save_librarians(self, librarians):
        """
        Save all librarians to a JSON file.

        Args:
            librarians (dict): Dictionary of Librarian objects (librarian_id -> Librarian)

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            librarians_data = {
                lib_id: librarian.to_dict() for lib_id, librarian in librarians.items()
            }
            with open(self.librarians_file, "w") as f:
                json.dump(librarians_data, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving librarians: {e}")
            return False

    def load_librarians(self):
        """
        Load all librarians from the JSON file.

        Returns:
            dict: Dictionary of Librarian objects (librarian_id -> Librarian),
                  empty if file doesn't exist
        """
        if not os.path.exists(self.librarians_file):
            return {}

        try:
            with open(self.librarians_file, "r") as f:
                librarians_data = json.load(f)

            librarians = {}
            for lib_id, data in librarians_data.items():
                librarians[lib_id] = Librarian.from_dict(data)
            return librarians
        except Exception as e:
            print(f"Error loading librarians: {e}")
            return {}

    def save_all(self, library):
        """
        Save all library data (books, members, librarians).

        Args:
            library (Library): The Library object to save

        Returns:
            bool: True if all saves were successful
        """
        # Access private attributes through public methods or a special method
        books = {book.isbn: book for book in library.get_all_books()}
        members = {member.member_id: member for member in library.get_all_members()}
        librarians = {lib.librarian_id: lib for lib in library.get_all_librarians()}

        books_saved = self.save_books(books)
        members_saved = self.save_members(members)
        librarians_saved = self.save_librarians(librarians)

        return books_saved and members_saved and librarians_saved

    def load_all(self, library):
        """
        Load all library data (books, members, librarians) into the Library object.

        Args:
            library (Library): The Library object to load data into

        Returns:
            tuple: (books_loaded: int, members_loaded: int, librarians_loaded: int)
        """
        # Load books
        books = self.load_books()
        books_count = 0
        for book in books.values():
            if library.add_book(book):
                books_count += 1

        # Load members
        members = self.load_members()
        members_count = 0
        for member in members.values():
            if library.register_member(member):
                members_count += 1

        # Load librarians
        librarians = self.load_librarians()
        librarians_count = 0
        for librarian in librarians.values():
            if library.add_librarian(librarian):
                librarians_count += 1

        return books_count, members_count, librarians_count
