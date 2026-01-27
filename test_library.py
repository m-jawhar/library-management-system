"""
Unit tests for the Library Management System
Demonstrates testing of OOP concepts and functionality
"""


def test_book_encapsulation():
    """Test that Book class properly encapsulates its data."""
    from book import Book

    print("Testing Book Encapsulation...")
    book = Book("Test Book", "Test Author", "123-456")

    # Test initial state
    assert book.is_available() == True, "New book should be available"

    # Test borrowing
    assert book.borrow("M001") == True, "Should successfully borrow available book"
    assert book.is_available() == False, "Borrowed book should not be available"
    assert book.get_borrowed_by() == "M001", "Should track who borrowed the book"

    # Test cannot borrow already borrowed book
    assert book.borrow("M002") == False, "Cannot borrow already borrowed book"

    # Test returning
    assert book.return_book() == True, "Should successfully return borrowed book"
    assert book.is_available() == True, "Returned book should be available"
    assert book.get_borrowed_by() == None, "Should clear borrower info"

    print("✓ Book encapsulation tests passed!")


def test_member_functionality():
    """Test Member class functionality."""
    from member import Member

    print("\nTesting Member Functionality...")
    member = Member("John Doe", "M001")

    # Test initial state
    assert member.get_borrowed_count() == 0, "New member should have no borrowed books"

    # Test borrowing books
    assert member.borrow_book("ISBN1") == True, "Should add book to borrowed list"
    assert member.borrow_book("ISBN2") == True, "Should add second book"
    assert member.get_borrowed_count() == 2, "Should have 2 borrowed books"

    # Test cannot borrow same book twice
    assert member.borrow_book("ISBN1") == False, "Cannot borrow same book twice"

    # Test checking borrowed status
    assert member.has_borrowed("ISBN1") == True, "Should confirm book is borrowed"
    assert member.has_borrowed("ISBN3") == False, "Should confirm book not borrowed"

    # Test returning books
    assert member.return_book("ISBN1") == True, "Should successfully return book"
    assert member.get_borrowed_count() == 1, "Should have 1 borrowed book"
    assert member.has_borrowed("ISBN1") == False, "Returned book should not be in list"

    print("✓ Member functionality tests passed!")


def test_library_operations():
    """Test Library class operations."""
    from library import Library
    from book import Book
    from member import Member

    print("\nTesting Library Operations...")
    library = Library("Test Library")

    # Test adding books
    book1 = Book("Book 1", "Author 1", "ISBN1")
    book2 = Book("Book 2", "Author 2", "ISBN2")

    assert library.add_book(book1) == True, "Should add first book"
    assert library.add_book(book2) == True, "Should add second book"
    assert library.add_book(book1) == False, "Cannot add duplicate ISBN"

    # Test registering members
    member1 = Member("Member 1", "M001")
    assert library.register_member(member1) == True, "Should register member"
    assert library.register_member(member1) == False, "Cannot register duplicate ID"

    # Test borrowing
    success, msg = library.borrow_book("M001", "ISBN1")
    assert success == True, f"Should borrow book: {msg}"

    # Test cannot borrow already borrowed book
    success, msg = library.borrow_book("M001", "ISBN1")
    assert success == False, "Cannot borrow already borrowed book"

    # Test returning
    success, msg = library.return_book("M001", "ISBN1")
    assert success == True, f"Should return book: {msg}"

    # Test searching
    results = library.find_books_by_title("Book")
    assert len(results) == 2, "Should find both books"

    # Test statistics
    stats = library.get_statistics()
    assert stats["total_books"] == 2, "Should have 2 books"
    assert stats["total_members"] == 1, "Should have 1 member"

    print("✓ Library operations tests passed!")


def test_librarian_authentication():
    """Test Librarian authentication."""
    from librarian import Librarian

    print("\nTesting Librarian Authentication...")
    librarian = Librarian("Admin", "LIB001", "password123")

    # Test authentication
    assert (
        librarian.authenticate("password123") == True
    ), "Should authenticate with correct password"
    assert librarian.authenticate("wrongpass") == False, "Should reject wrong password"

    # Test login count
    assert librarian.get_login_count() == 1, "Should track login count"

    # Test password change
    assert (
        librarian.change_password("password123", "newpass") == True
    ), "Should change password"
    assert (
        librarian.authenticate("password123") == False
    ), "Old password should not work"
    assert librarian.authenticate("newpass") == True, "New password should work"

    print("✓ Librarian authentication tests passed!")


def test_data_persistence():
    """Test data saving and loading."""
    from library import Library
    from book import Book
    from member import Member
    from data_manager import DataManager
    import os
    import shutil

    print("\nTesting Data Persistence...")

    # Use a test directory
    test_dir = "test_data"
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)

    data_manager = DataManager(test_dir)

    # Create and save data
    library = Library("Test Library")
    book = Book("Test Book", "Test Author", "TEST123")
    member = Member("Test Member", "M999")

    library.add_book(book)
    library.register_member(member)

    assert data_manager.save_all(library) == True, "Should save data"

    # Load data into new library
    new_library = Library("Test Library 2")
    books_count, members_count, _ = data_manager.load_all(new_library)

    assert books_count == 1, "Should load 1 book"
    assert members_count == 1, "Should load 1 member"

    # Verify loaded data
    loaded_book = new_library.find_book_by_isbn("TEST123")
    assert loaded_book is not None, "Should find loaded book"
    assert loaded_book.title == "Test Book", "Book data should match"

    loaded_member = new_library.find_member("M999")
    assert loaded_member is not None, "Should find loaded member"
    assert loaded_member.name == "Test Member", "Member data should match"

    # Cleanup
    shutil.rmtree(test_dir)

    print("✓ Data persistence tests passed!")


def run_all_tests():
    """Run all test functions."""
    print("=" * 60)
    print("  Running Library Management System Tests")
    print("=" * 60)

    try:
        test_book_encapsulation()
        test_member_functionality()
        test_library_operations()
        test_librarian_authentication()
        test_data_persistence()

        print("\n" + "=" * 60)
        print("  ✓ ALL TESTS PASSED!")
        print("=" * 60)
        return True
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
