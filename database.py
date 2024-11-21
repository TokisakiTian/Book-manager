import sqlite3


def create_table():
    """
    This function creates a new database "library.json" with the table "books"
    :return: None
    """
    connection = sqlite3.connect("library.json")
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
    """
    This function adds a new element to the table in the format: title, author, year
    :param element: the string in the format: title, author, year
    :return:None
    """
    connection = sqlite3.connect("library.json")
    cursor = connection.cursor()

    element = list(element.split(", "))

    cursor.execute(
        'INSERT INTO books (title, author, year, status) VALUES (?, ?, ?, ?)',
        (element[0], element[1], int(element[2]), "в наличии")
    )

    connection.commit()
    connection.close()


def show_table():
    """
    This function shows the entire table "books"
    :return:None
    """
    connection = sqlite3.connect("library.json")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')

    books = cursor.fetchall()
    for book in books:
        print(book)

    connection.commit()
    connection.close()


def find_a_book(title, author, year):
    """
    This function finds a book in the database by its name
    :param title:string with the title of the book
    :param author:string with the author's name
    :param year:int with the year of publication of the book
    :return:
    """
    connection = sqlite3.connect("library.json")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books WHERE title = ? AND author = ? AND year = ?', (title, author, year))

    out = cursor.fetchall()
    for elements in out:
        print(elements)

    connection.commit()
    connection.close()


def delete_element(id):
    """
    This function removes an item from the database
    :param id: the id of the book to delete
    :return:None
    """
    connection = sqlite3.connect("library.json")
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books WHERE id = ?', (id,))

    out = cursor.fetchall()
    for elements in out:
        print(elements)

    connection.commit()
    connection.close()


def update_status(id, status):
    """
    This function changes the status of a book by its id
    :param id: the id of the book to change status
    :param status: the text to replace the status with
    :return:None
    """
    connection = sqlite3.connect("library.json")
    cursor = connection.cursor()

    cursor.execute('UPDATE books SET status = ? WHERE id = ?', (status, id))

    connection.commit()
    connection.close()
