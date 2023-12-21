## Table of Contents

- [Models](#models)
- [CRUD Operations](#crud-operations)
- [Aggregation Methods](#aggregation-methods)
- [User Interface](#user-interface)
- [Getting Started](#getting-started)

## Models

### Book Model

- **Title (CharField):** The title of the book.
- **Author (Foreign key):** The author of the book.
- **Publication Year (IntegerField):** The year the book was published.
- **ISBN (CharField):** The International Standard Book Number of the book.
- **Price (DecimalField):** The price of the book.

### Author Model

- **First Name (CharField):** The first name of the author.
- **Second Name (CharField):** The second name of the author.
- **Address (CharField):** The address of the author.

## CRUD Operations

### Books

- **View all books:** Display a list of all books.
- **Add a new book:** Create a new book record.
- **Edit book details:** Modify existing book information.
- **Delete a book:** Remove a book from the database.

### Authors

- **View all authors:** Display a list of all authors.
- **Add a new author:** Create a new author record.
- **Edit author details:** Modify existing author information.
- **Delete an author:** Remove an author from the database.

## Aggregation Methods

- **Total number of books:** Count of all books in the database.
- **Average price of all books:** Calculate the average price of books.
- **Oldest and newest books:** Identify the oldest and newest books.
- **Count of books published each year:** Group books by publication year and provide a count.

## User Interface

Design a simple and user-friendly interface for performing CRUD operations and viewing aggregation results.

## Getting Started

Follow these instructions to set up and run the application locally. Make sure you have Python and Django installed.

1. Clone the repository: `git clone https://github.com/your-username/django-book-management.git`
2. Navigate to the project directory: `cd django-book-management`
3. Install dependencies: `pip install -r requirements.txt`
4. Apply database migrations: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`
