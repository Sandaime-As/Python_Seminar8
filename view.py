def main_menu():
    print()
    print('Здравствуйте, чем могу помочь? Навигация осуществляется по цифрам.')
    print('\n1. Показать телефонную книгу:')
    print('2. Открыть файл телефонной книги:')
    print('3. Сохранить файл телефонной книги:')
    print('4. Добавить контакт телефонной книги:')
    print('5. Изменить контакт:')
    print('6. Удалить контакт:')
    print('7. Найти контакт:')
    print('0. Выход\n')
    return choice_main_menu()


def choice_main_menu():
    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if choice in range(0, 8):
                print()
                return choice
            else:
                print('Неверный ввод, повторите запрос ')

        except:
            print('Ошибка ввода, некорректные данные ')


def print_phone_book(phone_book: list):
    if len(phone_book) > 0:
        for id, contact in enumerate(phone_book):
            print(id, contact)
    else:
        print('Телефонная книга пуста, или не загружена')


def log_off():
    print('До свидания!')


def load_success():
    print('Телефонная книга загружена')


def save_success():
    print('Телефонная книга сохранена')


def remove_success():
    print('Контакт успешно удален')


def change_success():
    print('Контакт успешно обновлен')


def input_new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий к контакту: ')
    return [name, phone, comment]


def input_remove_contact():
    id = int(input('Ввeдите ID контакта: '))
    return id


def input_change_contact():
    id = int(input('Ввeдите ID контакта, который необходимо изменить: '))
    return id


def input_search_text():
    search_text = input('Введите имя контакта, который необходимо найти: ')
    return search_text
