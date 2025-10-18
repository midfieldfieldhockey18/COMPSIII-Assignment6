# library.py

# Step 1: Import the sqlite3 module
import sqlite3

# Step 2: Connect to (or create) the library.db database
connection = sqlite3.connect('library.db')

# Step 3: Create a cursor to execute SQL commands
cursor = connection.cursor()

# Step 4: Drop the books table if it already exists (to avoid duplication during testing)
cursor.execute('DROP TABLE IF EXISTS books')

# Step 5: Create the books table with specified columns
cursor.execute('''
    CREATE TABLE books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT
    )
''')

# Step 6: Insert 10 books into the books table
books_to_insert = [
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Fiction'),
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian Fiction'),
    ('The Lord of the Rings', 'J.R.R. Tolkien', 1954, 'Fantasy'),
    ('The Catcher in the Rye', 'J.D. Salinger', 1951, 'Fiction'),
    ('One Hundred Years of Solitude', 'Gabriel Garcia Marquez', 1967, 'Magical Realism'),
    ('The Hitchhikers Guide to the Galaxy', 'Douglas Adams', 1979, 'Science Fiction'),
    ('The Handmaids Tale', 'Margaret Atwood', 1985, 'Dystopian Fiction'),
    ('War and Peace', 'Leo Tolstoy', 1869, 'Fiction'),
    ('Ulysses', 'James Joyce', 1922, 'Fiction')
]

cursor.executemany('''
    INSERT INTO books (title, author, publication_year, genre)
    VALUES (?, ?, ?, ?)
''', books_to_insert)

# Step 7: Fetch and print all data in the books table (optional verification)
cursor.execute('SELECT * FROM books')
all_books = cursor.fetchall()
print("\nAll Books in Database:")
for book in all_books:
    print(book)

# Step 8: Fetch all Fiction books and store in a variable
cursor.execute('SELECT * FROM books WHERE genre = "Fiction"')
fiction = cursor.fetchall()
print("\nFiction Books:")
for book in fiction:
    print(book)

# Step 9: Update publication year of "The Handmaids Tale" to 1985
cursor.execute('''
    UPDATE books
    SET publication_year = 1985
    WHERE title = "The Handmaids Tale"
''')

# Step 10: Delete the book titled "1984"
cursor.execute('''
    DELETE FROM books
    WHERE title = "1984"
''')

# Final Step: Commit all changes to the database
connection.commit()

python3 -m unittest
