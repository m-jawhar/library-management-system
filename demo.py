"""
Demo script to showcase the Library Management System
Creates sample data and demonstrates key features
"""

from library import Library
from book import Book
from member import Member
from librarian import Librarian
from data_manager import DataManager


def demo():
    """Run a demonstration of the library system."""

    print("=" * 60)
    print("  Library Management System - Demo")
    print("=" * 60)

    # Create library instance
    library = Library("Demo City Library")
    print(f"\n✓ Created library: {library.name}")

    # Add some books
    print("\n--- Adding Books ---")
    books = [
        Book("1984", "George Orwell", "978-0451524935"),
        Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084"),
        Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565"),
        Book("Pride and Prejudice", "Jane Austen", "978-0141439518"),
        Book("The Catcher in the Rye", "J.D. Salinger", "978-0316769174"),
    ]

    for book in books:
        library.add_book(book)
        print(f"  Added: {book.title} by {book.author}")

    # Register members
    print("\n--- Registering Members ---")
    members = [
        Member("Alice Johnson", "M001"),
        Member("Bob Smith", "M002"),
        Member("Carol White", "M003"),
    ]

    for member in members:
        library.register_member(member)
        print(f"  Registered: {member.name} (ID: {member.member_id})")

    # Add a librarian
    print("\n--- Adding Librarian ---")
    librarian = Librarian("John Admin", "LIB001", "admin123")
    library.add_librarian(librarian)
    print(f"  Added: {librarian.name} (ID: {librarian.librarian_id})")

    # Demonstrate borrowing
    print("\n--- Borrowing Books ---")
    success, msg = library.borrow_book("M001", "978-0451524935")
    print(f"  {msg}")

    success, msg = library.borrow_book("M002", "978-0061120084")
    print(f"  {msg}")

    success, msg = library.borrow_book("M001", "978-0743273565")
    print(f"  {msg}")

    # Show library statistics
    print("\n--- Library Statistics ---")
    stats = library.get_statistics()
    print(f"  Total Books: {stats['total_books']}")
    print(f"  Available Books: {stats['available_books']}")
    print(f"  Borrowed Books: {stats['borrowed_books']}")
    print(f"  Total Members: {stats['total_members']}")

    # Show available books
    print("\n--- Available Books ---")
    available = library.get_available_books()
    for book in available:
        print(f"  - {book.title} by {book.author}")

    # Show borrowed books
    print("\n--- Currently Borrowed Books ---")
    borrowed = library.get_borrowed_books()
    for book in borrowed:
        print(f"  - {book.title} (borrowed by {book.get_borrowed_by()})")

    # Demonstrate searching
    print("\n--- Searching for Books ---")
    print("  Searching for 'the'...")
    results = library.find_books_by_title("the")
    for book in results:
        print(f"    - {book.title}")

    # Demonstrate returning
    print("\n--- Returning a Book ---")
    success, msg = library.return_book("M001", "978-0451524935")
    print(f"  {msg}")

    # Show member information
    print("\n--- Member Information ---")
    member = library.find_member("M001")
    if member:
        print(f"\n{member.get_info()}")
        print(f"  Borrowed books: {member.get_borrowed_count()}")

    # Save data
    print("\n--- Saving Data ---")
    data_manager = DataManager()
    if data_manager.save_all(library):
        print("  ✓ Data saved successfully to 'data/' directory")

    # Demonstrate encapsulation
    print("\n--- Demonstrating Encapsulation ---")
    book = library.find_book_by_isbn("978-0141439518")
    if book:
        print(f"  Book: {book.title}")
        print(f"  Available: {book.is_available()}")
        print("  Note: The availability status is private and can only be")
        print("  changed through the borrow() and return_book() methods!")

    print("\n" + "=" * 60)
    print("  Demo completed successfully!")
    print("  Run 'python main.py' to start the interactive application")
    print("=" * 60)


if __name__ == "__main__":
    demo()
