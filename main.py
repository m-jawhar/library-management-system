"""
Main Application for Library Management System
Command-line interface for interacting with the library
"""

import os
import sys
from library import Library
from book import Book
from member import Member
from librarian import Librarian
from data_manager import DataManager


class LibraryApp:
    """
    Main application class for the Library Management System.
    Provides a command-line interface for users.
    """

    def __init__(self):
        """Initialize the application."""
        self.library = Library("City Public Library")
        self.data_manager = DataManager()
        self.current_librarian = None
        self.load_data()

    def load_data(self):
        """Load existing data from files."""
        books, members, librarians = self.data_manager.load_all(self.library)

        # Create a default librarian if none exist
        if librarians == 0:
            default_librarian = Librarian("Admin", "LIB001", "admin123")
            self.library.add_librarian(default_librarian)
            print("Created default librarian (ID: LIB001, Password: admin123)")

    def save_data(self):
        """Save current data to files."""
        if self.data_manager.save_all(self.library):
            print("✓ Data saved successfully")
        else:
            print("✗ Error saving data")

    def clear_screen(self):
        """Clear the terminal screen."""
        os.system("cls" if os.name == "nt" else "clear")

    def pause(self):
        """Pause and wait for user input."""
        input("\nPress Enter to continue...")

    def display_header(self, title):
        """Display a formatted header."""
        print("\n" + "=" * 60)
        print(f"  {title}")
        print("=" * 60)

    def main_menu(self):
        """Display and handle the main menu."""
        while True:
            self.clear_screen()
            self.display_header(f"Welcome to {self.library.name}")

            print("\n1. Member Services")
            print("2. Librarian Login")
            print("3. View Library Statistics")
            print("4. Exit")

            choice = input("\nEnter your choice (1-4): ").strip()

            if choice == "1":
                self.member_menu()
            elif choice == "2":
                self.librarian_login()
            elif choice == "3":
                self.view_statistics()
            elif choice == "4":
                self.save_data()
                print("\nThank you for using the Library Management System!")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")
                self.pause()

    def member_menu(self):
        """Display and handle the member services menu."""
        while True:
            self.clear_screen()
            self.display_header("Member Services")

            print("\n1. Register New Member")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. Search Books")
            print("5. View Available Books")
            print("6. View My Borrowed Books")
            print("7. Back to Main Menu")

            choice = input("\nEnter your choice (1-7): ").strip()

            if choice == "1":
                self.register_member()
            elif choice == "2":
                self.borrow_book()
            elif choice == "3":
                self.return_book()
            elif choice == "4":
                self.search_books()
            elif choice == "5":
                self.view_available_books()
            elif choice == "6":
                self.view_member_books()
            elif choice == "7":
                break
            else:
                print("Invalid choice. Please try again.")
                self.pause()

    def register_member(self):
        """Register a new member."""
        self.clear_screen()
        self.display_header("Register New Member")

        name = input("\nEnter your name: ").strip()
        if not name:
            print("Name cannot be empty.")
            self.pause()
            return

        member_id = input("Choose a member ID: ").strip()
        if not member_id:
            print("Member ID cannot be empty.")
            self.pause()
            return

        member = Member(name, member_id)
        if self.library.register_member(member):
            print(f"\n✓ Member registered successfully!")
            print(f"Welcome, {name}! Your member ID is: {member_id}")
            self.save_data()
        else:
            print("\n✗ Member ID already exists. Please choose a different ID.")

        self.pause()

    def borrow_book(self):
        """Process a book borrowing request."""
        self.clear_screen()
        self.display_header("Borrow Book")

        member_id = input("\nEnter your member ID: ").strip()
        member = self.library.find_member(member_id)

        if not member:
            print("✗ Member not found. Please register first.")
            self.pause()
            return

        isbn = input("Enter the ISBN of the book you want to borrow: ").strip()

        success, message = self.library.borrow_book(member_id, isbn)

        if success:
            print(f"\n✓ {message}")
            self.save_data()
        else:
            print(f"\n✗ {message}")

        self.pause()

    def return_book(self):
        """Process a book return."""
        self.clear_screen()
        self.display_header("Return Book")

        member_id = input("\nEnter your member ID: ").strip()
        member = self.library.find_member(member_id)

        if not member:
            print("✗ Member not found.")
            self.pause()
            return

        # Show borrowed books
        borrowed = member.get_borrowed_books()
        if not borrowed:
            print("You have no borrowed books.")
            self.pause()
            return

        print("\nYour borrowed books:")
        for isbn in borrowed:
            book = self.library.find_book_by_isbn(isbn)
            if book:
                print(f"  - {book.title} (ISBN: {isbn})")

        isbn = input("\nEnter the ISBN of the book you want to return: ").strip()

        success, message = self.library.return_book(member_id, isbn)

        if success:
            print(f"\n✓ {message}")
            self.save_data()
        else:
            print(f"\n✗ {message}")

        self.pause()

    def search_books(self):
        """Search for books by title or author."""
        self.clear_screen()
        self.display_header("Search Books")

        print("\n1. Search by Title")
        print("2. Search by Author")
        print("3. Search by ISBN")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            title = input("Enter book title: ").strip()
            books = self.library.find_books_by_title(title)
            self.display_book_list(books, f"Books matching '{title}'")
        elif choice == "2":
            author = input("Enter author name: ").strip()
            books = self.library.find_books_by_author(author)
            self.display_book_list(books, f"Books by '{author}'")
        elif choice == "3":
            isbn = input("Enter ISBN: ").strip()
            book = self.library.find_book_by_isbn(isbn)
            if book:
                print("\n" + book.get_info())
            else:
                print("\n✗ Book not found.")
        else:
            print("Invalid choice.")

        self.pause()

    def view_available_books(self):
        """Display all available books."""
        self.clear_screen()
        self.display_header("Available Books")

        books = self.library.get_available_books()
        self.display_book_list(books, "Available Books")
        self.pause()

    def view_member_books(self):
        """Display books borrowed by a member."""
        self.clear_screen()
        self.display_header("My Borrowed Books")

        member_id = input("\nEnter your member ID: ").strip()
        member = self.library.find_member(member_id)

        if not member:
            print("✗ Member not found.")
            self.pause()
            return

        borrowed = member.get_borrowed_books()
        if not borrowed:
            print("\nYou have no borrowed books.")
        else:
            print(f"\nBooks borrowed by {member.name}:")
            for isbn in borrowed:
                book = self.library.find_book_by_isbn(isbn)
                if book:
                    print(f"\n{book.get_info()}")

        self.pause()

    def display_book_list(self, books, title):
        """Display a list of books."""
        print(f"\n{title}:")

        if not books:
            print("  No books found.")
        else:
            for i, book in enumerate(books, 1):
                status = "Available" if book.is_available() else "Borrowed"
                print(f"\n{i}. {book.title}")
                print(f"   Author: {book.author}")
                print(f"   ISBN: {book.isbn}")
                print(f"   Status: {status}")

    def librarian_login(self):
        """Handle librarian authentication."""
        self.clear_screen()
        self.display_header("Librarian Login")

        lib_id = input("\nEnter Librarian ID: ").strip()
        password = input("Enter Password: ").strip()

        librarian = self.library.find_librarian(lib_id)

        if librarian and librarian.authenticate(password):
            self.current_librarian = librarian
            print(f"\n✓ Welcome, {librarian.name}!")
            self.save_data()
            self.pause()
            self.librarian_menu()
        else:
            print("\n✗ Invalid credentials.")
            self.pause()

    def librarian_menu(self):
        """Display and handle the librarian menu."""
        while True:
            self.clear_screen()
            self.display_header(f"Librarian: {self.current_librarian.name}")

            print("\n1. Add New Book")
            print("2. Remove Book")
            print("3. View All Books")
            print("4. View All Members")
            print("5. Remove Member")
            print("6. View Borrowed Books")
            print("7. Change Password")
            print("8. Logout")

            choice = input("\nEnter your choice (1-8): ").strip()

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.view_all_books()
            elif choice == "4":
                self.view_all_members()
            elif choice == "5":
                self.remove_member()
            elif choice == "6":
                self.view_borrowed_books()
            elif choice == "7":
                self.change_password()
            elif choice == "8":
                self.current_librarian = None
                break
            else:
                print("Invalid choice. Please try again.")
                self.pause()

    def add_book(self):
        """Add a new book to the library."""
        self.clear_screen()
        self.display_header("Add New Book")

        title = input("\nEnter book title: ").strip()
        author = input("Enter author name: ").strip()
        isbn = input("Enter ISBN: ").strip()

        if not title or not author or not isbn:
            print("\n✗ All fields are required.")
            self.pause()
            return

        book = Book(title, author, isbn)
        if self.current_librarian.add_book(self.library, book):
            print(f"\n✓ Book '{title}' added successfully!")
            self.save_data()
        else:
            print("\n✗ Book with this ISBN already exists.")

        self.pause()

    def remove_book(self):
        """Remove a book from the library."""
        self.clear_screen()
        self.display_header("Remove Book")

        isbn = input("\nEnter the ISBN of the book to remove: ").strip()

        book = self.library.find_book_by_isbn(isbn)
        if book:
            print(f"\nBook: {book.title} by {book.author}")
            confirm = (
                input("Are you sure you want to remove this book? (yes/no): ")
                .strip()
                .lower()
            )

            if confirm == "yes":
                if self.current_librarian.remove_book(self.library, isbn):
                    print("\n✓ Book removed successfully!")
                    self.save_data()
                else:
                    print("\n✗ Cannot remove book. It may be currently borrowed.")
            else:
                print("\nBook removal cancelled.")
        else:
            print("\n✗ Book not found.")

        self.pause()

    def view_all_books(self):
        """Display all books in the library."""
        self.clear_screen()
        self.display_header("All Books in Library")

        books = self.library.get_all_books()
        self.display_book_list(books, "All Books")
        self.pause()

    def view_all_members(self):
        """Display all registered members."""
        self.clear_screen()
        self.display_header("All Registered Members")

        members = self.library.get_all_members()

        if not members:
            print("\nNo members registered.")
        else:
            for i, member in enumerate(members, 1):
                print(f"\n{i}. {member.get_info()}")

        self.pause()

    def remove_member(self):
        """Remove a member from the library."""
        self.clear_screen()
        self.display_header("Remove Member")

        member_id = input("\nEnter the member ID to remove: ").strip()

        member = self.library.find_member(member_id)
        if member:
            print(f"\nMember: {member.name} (ID: {member_id})")
            print(f"Borrowed books: {member.get_borrowed_count()}")

            if member.get_borrowed_count() > 0:
                print("\n✗ Cannot remove member with borrowed books.")
            else:
                confirm = (
                    input("Are you sure you want to remove this member? (yes/no): ")
                    .strip()
                    .lower()
                )

                if confirm == "yes":
                    if self.current_librarian.remove_member(self.library, member_id):
                        print("\n✓ Member removed successfully!")
                        self.save_data()
                else:
                    print("\nMember removal cancelled.")
        else:
            print("\n✗ Member not found.")

        self.pause()

    def view_borrowed_books(self):
        """Display all currently borrowed books."""
        self.clear_screen()
        self.display_header("Currently Borrowed Books")

        books = self.library.get_borrowed_books()

        if not books:
            print("\nNo books are currently borrowed.")
        else:
            for i, book in enumerate(books, 1):
                print(f"\n{i}. {book.get_info()}")

        self.pause()

    def change_password(self):
        """Change librarian password."""
        self.clear_screen()
        self.display_header("Change Password")

        old_password = input("\nEnter current password: ").strip()
        new_password = input("Enter new password: ").strip()
        confirm_password = input("Confirm new password: ").strip()

        if new_password != confirm_password:
            print("\n✗ Passwords do not match.")
        elif self.current_librarian.change_password(old_password, new_password):
            print("\n✓ Password changed successfully!")
            self.save_data()
        else:
            print("\n✗ Current password is incorrect.")

        self.pause()

    def view_statistics(self):
        """Display library statistics."""
        self.clear_screen()
        self.display_header("Library Statistics")

        stats = self.library.get_statistics()

        print(f"\n{'Total Books:':<25} {stats['total_books']}")
        print(f"{'Available Books:':<25} {stats['available_books']}")
        print(f"{'Borrowed Books:':<25} {stats['borrowed_books']}")
        print(f"{'Total Members:':<25} {stats['total_members']}")

        self.pause()

    def run(self):
        """Start the application."""
        try:
            self.main_menu()
        except KeyboardInterrupt:
            print("\n\nApplication interrupted. Saving data...")
            self.save_data()
            print("Goodbye!")
            sys.exit(0)


def main():
    """Main entry point for the application."""
    app = LibraryApp()
    app.run()


if __name__ == "__main__":
    main()
