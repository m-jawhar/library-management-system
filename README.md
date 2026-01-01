# Library Management System

A comprehensive Object-Oriented Library Management System built in Python, demonstrating fundamental OOP concepts including encapsulation, inheritance, and abstraction.

## 🎯 Project Overview

This project is designed to showcase Object-Oriented Programming principles through a practical, real-world application. It manages a library's books, members, and borrowing activities with proper encapsulation and data persistence.

## ✨ Key Features

### Object-Oriented Design

- **Classes and Objects**: Separate classes for `Book`, `Member`, `Librarian`, and `Library`
- **Encapsulation**: Private attributes with controlled access through getter/setter methods
- **Data Abstraction**: Clean interfaces hiding implementation details
- **Method Encapsulation**: Business logic encapsulated within appropriate classes

### Core Functionality

- **Book Management**: Add, remove, search, and view books
- **Member Management**: Register members, track borrowed books
- **Librarian Functions**: Administrative access with authentication
- **Borrowing System**: Borrow and return books with status tracking
- **Data Persistence**: Save/load data using JSON files
- **Statistics**: View library statistics and reports

## 📁 Project Structure

```
library-management-system/
├── book.py                 # Book class with encapsulation
├── member.py              # Member class for library users
├── librarian.py           # Librarian class with admin privileges
├── library.py             # Central Library class managing all operations
├── data_manager.py        # Data persistence layer (JSON)
├── main.py                # Main application with CLI interface
├── README.md              # This file
├── requirements.txt       # Python dependencies
└── data/                  # Directory for data files (auto-created)
    ├── books.json
    ├── members.json
    └── librarians.json
```

## 🔧 Installation & Setup

### Prerequisites

- Python 3.7 or higher

### Installation Steps

1. **Clone or download the project**

   ```bash
   cd library-management-system
   ```

2. **No external dependencies required!**
   This project uses only Python standard library modules.

3. **Run the application**
   ```bash
   python main.py
   ```

## 🚀 Usage Guide

### Starting the Application

Run the main program:

```bash
python main.py
```

### Default Librarian Credentials

- **Librarian ID**: `LIB001`
- **Password**: `admin123`

### Main Menu Options

#### 1. Member Services

- Register as a new member
- Borrow books
- Return books
- Search for books
- View available books
- View your borrowed books

#### 2. Librarian Login

- Add new books to the library
- Remove books
- View all books
- View all members
- Remove members
- View borrowed books
- Change password

#### 3. View Library Statistics

- Total books in library
- Available vs borrowed books
- Total registered members

## 💡 OOP Concepts Demonstrated

### 1. Encapsulation

```python
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__available = True  # Private attribute

    def is_available(self):
        """Controlled access to private attribute"""
        return self.__available

    def borrow(self, member_id):
        """Controlled modification of private attribute"""
        if self.__available:
            self.__available = False
            return True
        return False
```

### 2. Data Abstraction

- Complex borrowing logic is hidden behind simple `borrow()` and `return_book()` methods
- Users interact with high-level methods without worrying about implementation

### 3. Information Hiding

- Private attributes (prefixed with `__`) prevent direct external access
- Public methods provide controlled access to internal state

### 4. Class Design

- Each class has a single, well-defined responsibility
- Methods are organized logically within their appropriate classes

## 📊 Example Usage

### Adding a Book (Librarian)

```python
book = Book("1984", "George Orwell", "978-0451524935")
library.add_book(book)
```

### Registering a Member

```python
member = Member("John Doe", "M001")
library.register_member(member)
```

### Borrowing a Book

```python
success, message = library.borrow_book("M001", "978-0451524935")
```

## 🗄️ Data Persistence

The system automatically saves data to JSON files in the `data/` directory:

- **books.json**: Stores all book information
- **members.json**: Stores member details and borrowed books
- **librarians.json**: Stores librarian credentials and login history

Data is automatically loaded when the application starts and saved when:

- The application exits normally
- Any modifications are made (add/remove books, borrow/return operations)

## 🎓 Learning Outcomes

This project demonstrates:

1. **Class Design**: Creating meaningful classes with appropriate attributes and methods
2. **Encapsulation**: Using private attributes and public methods for controlled access
3. **Data Management**: Implementing CRUD operations (Create, Read, Update, Delete)
4. **File I/O**: Saving and loading data from files
5. **Error Handling**: Validating inputs and handling edge cases
6. **User Interface**: Creating an interactive command-line application
7. **Code Organization**: Structuring a multi-file Python project

## 🔄 Future Enhancements

Potential features to add:

- Database integration (SQLite, PostgreSQL)
- Due dates and late fees
- Book reservations
- Search with filters (genre, publication year)
- Book ratings and reviews
- Email notifications
- Web interface (Flask/Django)
- Multiple book copies
- Borrowing history and statistics

## 📝 Code Quality

- **Docstrings**: All classes and methods include documentation
- **Type Hints**: Can be added for better code clarity
- **Error Handling**: Input validation and appropriate error messages
- **Naming Conventions**: Following PEP 8 Python style guide
- **Modularity**: Separated concerns across multiple files

## 🤝 Contributing

This is a portfolio/learning project. Feel free to:

- Fork the repository
- Add new features
- Improve existing code
- Report bugs or suggest improvements

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

Created as a demonstration of Object-Oriented Programming concepts for academic portfolio purposes.

---

## 🎯 Portfolio Highlights

This project showcases:

- ✅ Strong understanding of OOP principles
- ✅ Clean, maintainable code structure
- ✅ Practical problem-solving skills
- ✅ User-friendly interface design
- ✅ Data persistence implementation
- ✅ Comprehensive documentation
- ✅ Real-world application development

Perfect for demonstrating foundational programming skills to potential employers or for academic portfolios!
