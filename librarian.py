"""
Librarian class for the Library Management System
Represents a librarian with administrative privileges
"""

from datetime import datetime


class Librarian:
    """
    Represents a librarian with administrative access.

    Attributes:
        name (str): The name of the librarian
        librarian_id (str): Unique identifier for the librarian
        __password (str): Private password for authentication
        __login_count (int): Private counter for login attempts
    """

    def __init__(self, name, librarian_id, password="admin123"):
        """
        Initialize a new Librarian object.

        Args:
            name (str): The name of the librarian
            librarian_id (str): Unique identifier for the librarian
            password (str): Password for authentication (default: "admin123")
        """
        self.name = name
        self.librarian_id = librarian_id
        self.__password = password  # Private attribute (encapsulation)
        self.__login_count = 0
        self.__last_login = None

    # Getter methods (encapsulation)
    def get_login_count(self):
        """Get the number of times this librarian has logged in."""
        return self.__login_count

    def get_last_login(self):
        """Get the date and time of the last login."""
        return self.__last_login

    # Authentication method
    def authenticate(self, password):
        """
        Verify the librarian's password.

        Args:
            password (str): The password to verify

        Returns:
            bool: True if password is correct, False otherwise
        """
        if self.__password == password:
            self.__login_count += 1
            self.__last_login = datetime.now()
            return True
        return False

    def change_password(self, old_password, new_password):
        """
        Change the librarian's password.

        Args:
            old_password (str): The current password
            new_password (str): The new password to set

        Returns:
            bool: True if password was changed successfully
        """
        if self.__password == old_password:
            self.__password = new_password
            return True
        return False

    # Administrative methods
    def add_book(self, library, book):
        """
        Add a book to the library (administrative function).

        Args:
            library: The Library object
            book: The Book object to add

        Returns:
            bool: True if book was added successfully
        """
        return library.add_book(book)

    def remove_book(self, library, isbn):
        """
        Remove a book from the library (administrative function).

        Args:
            library: The Library object
            isbn (str): The ISBN of the book to remove

        Returns:
            bool: True if book was removed successfully
        """
        return library.remove_book(isbn)

    def register_member(self, library, member):
        """
        Register a new member (administrative function).

        Args:
            library: The Library object
            member: The Member object to register

        Returns:
            bool: True if member was registered successfully
        """
        return library.register_member(member)

    def remove_member(self, library, member_id):
        """
        Remove a member from the library (administrative function).

        Args:
            library: The Library object
            member_id (str): The ID of the member to remove

        Returns:
            bool: True if member was removed successfully
        """
        return library.remove_member(member_id)

    def get_info(self):
        """
        Get formatted information about the librarian.

        Returns:
            str: Formatted librarian information
        """
        last_login = (
            self.__last_login.strftime("%Y-%m-%d %H:%M")
            if self.__last_login
            else "Never"
        )
        return (
            f"Name: {self.name}\n"
            f"Librarian ID: {self.librarian_id}\n"
            f"Login Count: {self.__login_count}\n"
            f"Last Login: {last_login}"
        )

    def to_dict(self):
        """
        Convert librarian data to dictionary for storage.

        Returns:
            dict: Librarian data as dictionary
        """
        return {
            "name": self.name,
            "librarian_id": self.librarian_id,
            "password": self.__password,
            "login_count": self.__login_count,
            "last_login": self.__last_login.isoformat() if self.__last_login else None,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a Librarian object from dictionary data.

        Args:
            data (dict): Dictionary containing librarian data

        Returns:
            Librarian: A new Librarian object
        """
        librarian = cls(data["name"], data["librarian_id"], data["password"])
        librarian.__login_count = data["login_count"]
        if data["last_login"]:
            librarian.__last_login = datetime.fromisoformat(data["last_login"])
        return librarian

    def __str__(self):
        """String representation of the librarian."""
        return f"Librarian {self.name} (ID: {self.librarian_id})"

    def __repr__(self):
        """Developer-friendly representation of the librarian."""
        return f"Librarian('{self.name}', '{self.librarian_id}')"
