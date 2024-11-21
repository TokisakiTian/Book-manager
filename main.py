from database import create_table, add_element, show_table, delete_element, find_a_book, update_status
import os

def operations():
    """
    This function calls other functions at the user's request
    :return:None
    """
    print()
    print("Введите 0, если хотите создать базу данных.")
    print("Введите 1, если хотите добавить новую книгу в базу данных.")
    print("Введите 2, если хотите удалить существующий элемент в базе данных.")
    print("Введите 3, если хотите получить информацию о конкретной книге.")
    print("Введите 4, если хотите обновить информацию о статусе конкретной книги.")
    print("Введите 5, если хотите вывести всю базу данных.")
    print("Введите 6, чтобы завершить работу программы.")
    print()

    #Выбор функционала
    try:
        marker = int(input())

    except ValueError:
        print("Недоступная операция попробуйте ещё раз.")
        operations()

    os.system('cls')

    if marker not in [0, 1, 2, 3, 4, 5, 6]:
        print("Недоступная операция попробуйте ещё.")
        return operations()

    #Если выбрано создать таблицу
    if marker == 0:
        create_table()
        print("База данных создана.")
        return operations()

    #Если выбрано добавить новую книгу
    if marker == 1:
        print("Введите данные о новой книге в формате: Название, Автор, Год выпуска")
        element = input()
        try:
            add_element(element)
        except ValueError:
            print("Недопустимый формат данных.")
        else:
            print("Книга добавленная в базу данных.")

        finally:
            return operations()

    #Если выбрано удалить книгу
    if marker == 2:
        print("Введите id элемента, который вы хотите удалить:", end="")
        removable_id = int(input())
        delete_element(removable_id)
        return operations()

    #Если выбранно вывести данные о книге
    if marker == 3:
        print("Введите данные о книге в формате: Название, Автор, Год выпуска")
        book = input().split(", ")
        try:
            title = book[0]
            author = book[1]
            year = int(book[2])
            find_a_book(title, author, year)
        except IndexError:
            print("Недопустимый формат данных.")
        finally:
            return operations()

    #Если выбрано обновить статус
    if marker == 4:
        print("Введите id книги статус которой вы хотите обновить:")
        try:
            id = int(input())

        except ValueError:
            print("Недопустимый формат данных.")

        else:
            print("Введите новый статус для книги с введенным значением id:")
            status = input()
            update_status(id, status)
        finally:
            return operations()

    #Если выбрано вывести всю таблицу
    if marker == 5:
        show_table()
        return operations()

    #Если выбрано завершить работу программы
    if marker == 6:
        exit()


if __name__ == "__main__":
    operations()
