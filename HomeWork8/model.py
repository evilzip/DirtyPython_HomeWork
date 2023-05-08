grade_book = {}
PATH = 'gradebook.txt'


def open_file():
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.read()
    subject_list = []
    name_list = []
    data = data.split('}, ')
    for string in data:
        subject = string[:string.find(':')].replace('{', '').replace("'", '')
        subject_list.append(subject)
        string_with_name = string[string.find(':') + 1:].split('],')
        # print(subject, string_with_name)
        grade_book[subject] = {}
        for st in string_with_name:
            name = st[:st.index(':')].replace('{', '').replace("'", '').replace(' ', '')
            if name not in name_list:
                name_list.append(name)
                grade_book[subject][name] = []
            # print(111, subject, name)
            garde_list = []
            # print(1111, subject)
            for s in st[st.index(':') + 3:]:
                if s.isdigit():
                    garde_list.append(int(s))
                    # print(subject, name, garde_list)
            grade_book[subject][name] = garde_list
    #print(grade_book)


def create_subject_list(book: dict) -> list:
    return list(book.keys())


def subject_selected(book: dict, pos: str) -> str:
    return list(book.keys())[int(pos) - 1]


def create_pupils_list(book: dict) -> list:
    first_dict_in_book = book.get(list(book.keys())[0])
    return list(first_dict_in_book.keys())


def pupil_selected(book: dict, pos: str) -> str:
    first_dict_in_book = book.get(list(book.keys())[0])
    return list(first_dict_in_book.keys())[int(pos) - 1]


def put_grade(subj: str, name: str, grade: str):
    grade_book[subj][name].append(int(grade))


def copy_to_file():
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(str(grade_book))
