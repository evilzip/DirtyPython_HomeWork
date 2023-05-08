import sys

import view
import model


def start():
    while True:
        menu_selection = view.main_menu()
        match menu_selection:
            case 1:  #
                model.open_file()
            case 2:  # показать текущий журнал с оценками
                view.show_garde_book(model.grade_book)
            case 3:  # Выбрать предмет
                view.show_all_subjects(model.create_subject_list(model.grade_book))
                selected_subject = \
                    model.subject_selected(model.grade_book,
                                           view.subject_selection(model.create_subject_list(model.grade_book)))
            case 4:  # Выбрать ученика
                view.show_all_pupils(model.create_pupils_list(model.grade_book))
                selected_pupil = \
                    model.pupil_selected(model.grade_book,
                                         view.pupil_selection(model.create_pupils_list(model.grade_book)))
                view.current_pupil(selected_subject, selected_pupil)
            case 5:  # Поставить оценку
                current_garde = view.input_grade()
                model.put_grade(selected_subject, selected_pupil, current_garde)
            case 6:  # Сохранить текущий словарь в файл журнала
                model.copy_to_file()
            case 7:  # Выход
                sys.exit()
