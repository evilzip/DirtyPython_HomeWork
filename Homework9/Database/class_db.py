import sqlite3


class DataBase:

    def __init__(self, db_path: str = 'Database/phone_book.db'):
        self.db_path = db_path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, sql: str, parameters: tuple = tuple(), fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    @staticmethod
    def extract_kwargs(sql: str, parameters: dict) -> tuple:
        sql += ' AND '.join([f'{key}=?' for key in parameters])
        return sql, tuple(parameters.values())

    def disconnect(self):
        self.connection.close()

    def create_table(self, table_name: str):
        sql = f'CREATE TABLE IF NOT EXISTS {table_name} ' \
              f'(man_id INTEGER PRIMARY KEY AUTOINCREMENT, ' \
              f'surname VARCHAR, ' \
              f'name VARCHAR, ' \
              f'patronymic VARCHAR, ' \
              f'phone VARCHAR, ' \
              f'comment TEXT)'
        self.execute(sql, commit=True)

    def add_contact(self, contact_info: tuple[str, str, str, str, str]):
        sql = '''INSERT INTO phone_book (surname, name, patronymic, phone, comment) VALUES (?, ? , ?, ?, ?)'''
        self.execute(sql, contact_info, commit=True)


    def get_all_contacts(self) -> tuple:
        sql = '''SELECT * FROM phone_book ORDER by surname, name, patronymic'''
        return self.execute(sql, fetchall=True)


    def find_contact(self, query_string: str) -> tuple:
        sql = '''SELECT * FROM phone_book WHERE man_id = ? or 
        surname = ? or 
        name = ? or 
        patronymic = ? or  
        phone  = ?
        ORDER by surname, name, patronymic'''
        return self.execute(sql, (query_string, query_string, query_string, query_string, query_string), fetchall=True)

    def delete_contact(self, id_contact: str):
        sql = '''DELETE FROM phone_book WHERE man_id = ?'''
        self.execute(sql, (id_contact,), commit=True)

    def update_contact(self, id_contact: str, column: str, new_text: str):
        sql = '''UPDATE phone_book SET  surname = ? WHERE man_id = ?'''
        self.execute(sql, (id_contact, new_text), commit=True)

