import phone_book

path = 'phone_book.txt'


def str_to_list(phone_book):
    new_phone_book = []
    for contact in phone_book:
        new_phone_book.append(contact.strip().split(' ; '))
    print(new_phone_book)


with open(path, 'r', encoding='UTF-8') as file:
    phone_book = file.readlines()
    print(phone_book)
str_to_list(phone_book)
phone_book.set_phone_book(phone_book)
print(phone_book)
