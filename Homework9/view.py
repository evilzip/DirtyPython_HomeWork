import text_fields


def input_menu_selection():
    while True:
        number = input(text_fields.input_choice)
        if number.isdigit() and 0 < int(number) < 7:
            return int(number)
        else:
            print(text_fields.wrong_menu_selection)


def main_menu() -> int:
    print(text_fields.menu)
    return input_menu_selection()


def contact_input() -> tuple:
    surname = input(text_fields.surname_input)
    name = input(text_fields.name_input)
    patronymic = input(text_fields.patronymic_input)
    phone = input(text_fields.phone_input)
    comment = input(text_fields.comment_input)
    return (surname, name, patronymic, phone, comment)


def print_contact_table(income_tuple: tuple):
    header_fields = (' ', 'Фамилия', 'Имя', 'Отчество', 'Телефон', 'Комментарий')
    print('\n' + '=' * 110)
    print(f'{header_fields[0]:^2} | '
          f'{header_fields[1]:^15} | '
          f'{header_fields[2]:^15} | '
          f'{header_fields[3]:^15} | '
          f'{header_fields[4]:^15} | '
          f'{header_fields[5]:^15}')
    print('=' * 110)
    for contact in income_tuple:
        print(f'{contact[0]:^2} | '
              f'{contact[1]:<15} | '
              f'{contact[2]:<15} | '
              f'{contact[3]:<15} | '
              f'{contact[4]:<15} | '
              f'{contact[5]:<15}')
    print('=' * 110 + '\n')


def show_all_contact(all_in_tuple: tuple):
    if all_in_tuple:
        print_contact_table(all_in_tuple)
    else:
        print(text_fields.phone_book_empty)


def show_find_result(result_tuple: tuple):
    if result_tuple:
        print_contact_table(result_tuple)
    else:
        print(text_fields.nothing_found)


def find_input() -> str:
    return input(text_fields.find_contact)

def delete_input() -> str:
    return input(text_fields.delete_input)

def delete_input_id() -> str:
    return input(text_fields.delete_input_id)

def update_input() -> str:
    return input(text_fields.update_contact_input)

def update_menu()-> str:
    while True:
        print(text_fields.update_menu)
        selection = input('Выбор: ')
        if selection.isdigit() and 0< int(selection)< 6:
            return selection


def update_input_id() -> str:
    return input(text_fields.update_input_id)

def new_update() -> str:
    return input(text_fields.updated_info)