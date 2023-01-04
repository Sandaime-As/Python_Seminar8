phone_book = []


def get_phone_book():
    global phone_book
    return phone_book


def set_phone_book(new_phone_book):
    global phone_book
    phone_book = new_phone_book


def add_contact(contact):
    global phone_book
    phone_book.append(contact)


def remove_contact(id):
    global phone_book
    name = phone_book[id-1][0]
    confirm = input(f'Вы хотите удалить контакт {name}? y/n ')
    if confirm.lower() == 'y':
        phone_book.pop(id-1)
        return True
    return False


def change_contact(id):
    global phone_book
    name = phone_book[id][0]
    confirm = input(f'Вы хотите изменить контакт {name}? y/n ')
    if confirm.lower() == 'y':
        information_for_chage = str(phone_book[id]).split(';')
        temp = int(input
            ('Введите цифру параметра, который хотите изменить: 1. Имя, 2. Телефон, 3. Комментарий: '))
        if temp == 1:
            name_contact = input('Введите новое имя: ')
            information_for_chage[0] = name_contact
        elif temp == 2:
            telephone = input('Введите новый телефон: ')
            information_for_chage[1] = telephone
        elif temp == 3:
            comment = input('Введите новый комментарий: ')
            information_for_chage[2] = comment
        else:
            print('Неверно')
        phone_book[id] = list(information_for_chage)
        return True
    return False


def find_contact(search_text, phone_book):
    new_list_with_name = []
    for item in phone_book:
        new_list_with_name.append(str(item).split(';')[0][2:].lower())
    for i in range(len(new_list_with_name)):
        if new_list_with_name[i].find(search_text.lower()):
            return print(f'Данные необходимого пользователя: {phone_book[i]}')
        else:
            return 'Нет контакта с такими данными'
