import sqlite3

def create_table():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    status TEXT NOT NULL
    )
    ''')

    connection.commit()
    connection.close()
    return 0


def add_element(element):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    element = list(element.split(", "))

    cursor.execute(
        'INSERT INTO books (title, author, year, status) VALUES (?, ?, ?, ?)',
        (element[0], element[1], int(element[2]), "в наличии")
    )

    connection.commit()
    connection.close()


def show_table():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')

    books = cursor.fetchall()
    for book in books:
        print(book)

    connection.commit()
    connection.close()


def find_a_book(title, author, year):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books WHERE title = ? AND author = ? AND year = ?', (title, author, year))

    out = cursor.fetchall()
    for elements in out:
        print(elements)

    connection.commit()
    connection.close()


def delete_element(id):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books WHERE id = ?', (id,))

    out = cursor.fetchall()
    for elements in out:
        print(elements)

    connection.commit()
    connection.close()


def update_status(id, status):
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute('UPDATE books SET status = ? WHERE id = ?', (status, id))

    connection.commit()
    connection.close()