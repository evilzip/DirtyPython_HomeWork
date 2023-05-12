import sys

import text_fields
import view
import model
import Database
from Database import DataBase

phone_book = DataBase()

try:
    phone_book.create_table('phone_book')
    print(text_fields.data_base_ok)
except:
    print(text_fields.data_base_fail)


def start():
    while True:
        menu_selection = view.main_menu()
        match menu_selection:
            case 1:  # Посмотреть все контакты
                view.show_all_contact(phone_book.get_all_contacts())
            case 2:  # Добавить контакт
                try:
                    phone_book.add_contact(view.contact_input())
                    print(text_fields.contact_added)
                except:
                    print(text_fields.data_base_fail)
            case 3:  # Найти контакт
                try:
                    query = view.find_input()
                    view.show_find_result(phone_book.find_contact(query))
                    phone_book.add_contact(view.contact_input())
                    print(text_fields.contact_added)
                except:
                    print(text_fields.data_base_fail)
            case 4:  # Изменить контакт
                update_contact_input = view.update_input()
                if Database.find_contact(update_contact_input):
                    view.show_find_result(phone_book.find_contact(update_contact_input))
                    update_id = view.update_input_id()
                    if int(update_id) in model.list_selected_id(phone_book.find_contact(update_contact_input)):
                        db_column_selected = view.update_menu()
                        new_info = view.new_update()
                        Database.update_contact(update_id, db_column_selected, new_info)
                        view.show_find_result(phone_book.find_contact(update_id))
                    else:
                        print('Ошибка подтверждения выбора контакта')
                else:
                    print(text_fields.nothing_found)

            case 5:  # Удалить контакт
                delete_contact = view.delete_input()
                if phone_book.find_contact(delete_contact):
                    view.show_find_result(phone_book.find_contact(delete_contact))
                    delete_id = view.delete_input_id()
                    if int(delete_id) in model.list_selected_id(phone_book.find_contact(delete_contact)):
                        try:
                            phone_book.delete_contact(delete_id)
                            print(text_fields.contact_has_been_deleted)
                        except:
                            print(text_fields.data_base_fail)
                    else:
                        print('Ошибка подтверждения выбора контакта!')
                else:
                    print(text_fields.nothing_found)

            case 6:  # Выход
                sys.exit()
