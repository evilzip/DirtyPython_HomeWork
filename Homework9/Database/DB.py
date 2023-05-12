# import sqlite3
#
# import text_fields
#
# connection = sqlite3.connect('Database/phone_book.db')
# cursor = connection.cursor()
#
#
# def create_phone_book():
#     sql = '''CREATE TABLE IF NOT EXISTS phone_book (man_id INTEGER PRIMARY KEY AUTOINCREMENT,
#      surname VARCHAR, name VARCHAR, patronymic VARCHAR, phone VARCHAR, comment TEXT)'''
#     cursor.execute(sql)
#     connection.commit()
#
#
# def add_contact(contact_info: tuple[str, str, str, str, str]):
#     sql = '''INSERT INTO phone_book (surname, name, patronymic, phone, comment) VALUES (?, ? , ?, ?, ?)'''
#     cursor.execute(sql, contact_info)
#     print(text_fields.contact_added)
#     connection.commit()
#
#
# def get_all_contacts() -> tuple:
#     sql = '''SELECT * FROM phone_book ORDER by surname, name, patronymic'''
#     cursor.execute(sql)
#     return cursor.fetchall()
#
#
# def find_contact(query_string: str) -> tuple:
#     sql = '''SELECT * FROM phone_book WHERE man_id = ? or
#     surname = ? or
#     name = ? or
#     patronymic = ? or
#     phone  = ?
#     ORDER by surname, name, patronymic'''
#     cursor.execute(sql, (query_string, query_string, query_string, query_string, query_string))
#     return cursor.fetchall()
#
# def delete_contact(id_contact: int):
#     try:
#         sql = '''DELETE FROM phone_book WHERE man_id = ?'''
#         cursor.execute(sql, (id_contact, ))
#         connection.commit()
#         print(text_fields.contact_has_been_deleted)
#     except:
#         print('Ошиблись с выбором...')
#
# def update_contact(id_contact: str, column: str, new_text: str):
#     match int(column):
#         case 1:
#             sql = '''UPDATE phone_book SET  surname = ? WHERE man_id = ?'''
#         case 2:
#             sql = '''UPDATE phone_book SET  name = ? WHERE man_id = ?'''
#         case 3:
#             sql = '''UPDATE phone_book SET patronymic = ? WHERE man_id = ?'''
#         case 4:
#             sql = '''UPDATE phone_book SET  phone = ? WHERE man_id = ?'''
#         case 5:
#             sql = '''UPDATE phone_book SET  comment = ? WHERE man_id = ?'''
#     try:
#         cursor.execute(sql, (new_text, id_contact))
#         connection.commit()
#         print(text_fields.contact_has_been_updated)
#     except:
#         print('не прошло...')
#
#
#
