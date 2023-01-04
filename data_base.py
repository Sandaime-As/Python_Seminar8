import phone_book

path = 'phone_book.txt'


def load_data_base():
    with open(path, 'r', encoding='UTF-8') as file:
        phone_book_perm = file.readlines()
    phone_book.set_phone_book(str_to_list(phone_book_perm))


def str_to_list(phone_book):
    new_phone_book = []
    for contact in phone_book:
        new_phone_book.append(contact.strip().split(' ; '))
    return new_phone_book


def save_data_base():

    with open(path, 'w', encoding='UTF-8') as file:
        file.write(list_to_str())


def list_to_str():
    pb = phone_book.get_phone_book()
    new_phone_book = []
    for contact in pb:
        new_phone_book.append(';'.join(contact)+'\n')
    new_phone_book[-1] = new_phone_book[-1][:-1]
    return ''.join(new_phone_book)
