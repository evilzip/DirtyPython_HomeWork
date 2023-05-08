import text_fields


def input_menu_selection():
    while True:
        number = input(text_fields.input_choice)
        if number.isdigit() and 0 < int(number) < 8:
            return int(number)
        else:
            print(text_fields.wrong_menu_selection)


def main_menu() -> int:
    print(text_fields.menu)
    return input_menu_selection()


def show_garde_book(book: dict):
    for key, value in book.items():
        print('-' * 20)
        print(f'{key:^20}')
        print('-' * 20)
        for k, v in value.items():
            print(k, *v)
    print('-' * 20 + '\n')


def subject_selection(subj_list: list) -> str:
    while True:
        input_position = input(text_fields.subject_selection)
        if input_position.isdigit() and 0 < int(input_position) < len(subj_list) + 1:
            return input_position
        else:
            print(text_fields.wrong_subject_selection)


def pupil_selection(pupil_list: list) -> str:
    while True:
        input_position = input(text_fields.pupil_selection)
        if input_position.isdigit() and 0 < int(input_position) < len(pupil_list) + 1:
            return input_position
        else:
            print(text_fields.wrong_pupil_selection)
    return input(text_fields.pupil_selection)


def show_all_subjects(subj_list: list):
    print(text_fields.subject_list_header)
    for i, subj in enumerate(subj_list, 1):
        print(f'{i:>3}. {subj:<20}')


def show_all_pupils(subj_list: list):
    print(text_fields.pupils_list_header)
    for i, subj in enumerate(subj_list, 1):
        print(f'{i:>3}. {subj:<20}')


def current_pupil(subj: str, name: str):
    print('=' * len(text_fields.current_pupil + f'{name}'))
    print(text_fields.current_subject + f'{subj}')
    print(text_fields.current_pupil + f'{name}')
    print('=' * len(text_fields.current_pupil + f'{name}'))


def input_grade() -> str:
    while True:
        grade = input(text_fields.grade)
        if grade.isdigit() and 0 < int(grade) < 6:
            return grade
        else:
            print(text_fields.wrong_grade)
