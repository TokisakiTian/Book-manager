from database import create_table, add_element, show_table, delete_element, find_a_book, update_status

def operations():
    print()
    print("Введите 0, если хотите создать базу данных.")
    print("Введите 1, если хотите добавить новую книгу в базу данных.")
    print("Введите 2, если хотите удалить существующий элемент в базе данных.")
    print("Введите 3, если хотите получить информацию о конкретной книге.")
    print("Введите 4, если хотите обновить информацию о статусе конкретной книги.")
    print("Введите 5, если хотите вывести всю базу данных.")
    print("Введите 6, чтобы завершить работу программы.")
    print()

    marker = int(input())

    if marker not in [0, 1, 2, 3, 4, 5, 6]:
        print("Недоступная операция попробуйте ещё.")
        return operations()

    if marker == 0:
        create_table()
        print("База данных создана.")
        return operations()

    if marker == 1:
        print("Введите данные о новой книге в формате: Название, Автор, Год выпуска")
        element = input()
        add_element(element)
        print("Книга добавленная в базу данных.")
        return operations()

    if marker == 2:
        print("Введите id элемента, который вы хотите удалить:", end="")
        removable_id = int(input())
        delete_element(removable_id)
        return operations()

    if marker == 3:
        print("Введите данные о книге в формате: Название, Автор, Год выпуска")
        book = input().split(", ")
        title = book[0]
        author = book[1]
        year = int(book[2])
        find_a_book(title, author, year)
        return operations()

    if marker == 4:
        print("Введите id книги статус которой вы хотите обновить:")
        id = int(input())
        print("Введите новый статус для книги с введенным значением id:")
        status = input()
        update_status(id, status)
        return operations()


    if marker == 5:
        show_table()
        return operations()

    if marker == 6:
        exit()


if __name__ == "__main__":
    operations()