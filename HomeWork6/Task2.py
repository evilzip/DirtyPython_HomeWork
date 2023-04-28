# выдать топ 5 самых встречаемы слов в Алисе длинна которых не меньше 5 букв
#
# так же можете собрать еще какую-то статистику (не обязательное задание на фантазию) :)
import string


def create_word_len_frequency_dict(text: str, min_word_len=0, max_word_len=100) -> dict:
    """Функция создает словарь количества повторений каждого слова ограниченного минимальным
     и максимальным количеством букв тексте text"""
    text_filtered = ''.join(filter(lambda symbol: symbol.isalpha() or symbol.isspace(), text))
    list_all_words = text_filtered.split()
    # print(list_all_words)
    word_frequency_dict_lower = {}
    for word in list_all_words:
        if min_word_len < len(word) < max_word_len:
            word_frequency_dict_lower[word.lower()] = word_frequency_dict_lower.get(word.lower(), 0) + 1
    return word_frequency_dict_lower


def create_word_frequency_dict(text: str) -> dict:
    """Функция создает словарь количества повторений каждого слова в тексте text"""
    text_filtered = ''.join(filter(lambda symbol: symbol.isalpha() or symbol.isspace(), text))
    list_all_words = text_filtered.split()
    # print(list_all_words)
    word_frequency_dict_lower = {}
    for word in list_all_words:
        word_frequency_dict_lower[word.lower()] = word_frequency_dict_lower.get(word.lower(), 0) + 1
    return word_frequency_dict_lower


def words_frequency_rating_tuple(input_dict: dict, size_list=10) -> tuple:
    """Функция создает кортеж заданной длины (слово, частота вхождения) где значения частоты вхождения отсортированы
      от максимально до минимального"""
    result_tuple = ()
    value_list_top = (sorted(list(input_dict.values()), reverse=True))[0:size_list]
    for i in range(len(value_list_top)):
        for (key, value) in input_dict.items():
            if value == value_list_top[i] and value != value_list_top[i - 1]:
                result_tuple += ((key, value),)
    return result_tuple


def words_by_len_rating_tuple(input_dict: dict, size_list=10) -> tuple:
    """Функция создает кортеж заданной длины (слово, его дина) где значения длины слов отсортированы
          от максимально до минимального"""
    input_dict_key_list_sorted = sorted(list(input_dict.keys()), key=len, reverse=True)[0:size_list]
    return tuple([(i, len(i)) for i in input_dict_key_list_sorted])


def find_longest_word(word_dict: dict) -> str:
    """Функция ищет самое длинное слова в словаре"""
    key_lit_sorted_len = sorted(list(word_dict.keys()), key=len, reverse=True)
    return key_lit_sorted_len[0]


def total_words_in_dict(word_dict: dict) -> int:
    """Общее количество слова в словаре"""
    return len(list(word_dict.keys()))


def print_rating_tuple(word_tuple: tuple, units: str) -> None:
    """Распечатка кортежа с рейтингом с указанием единиц значений: кол-во раз, количество букв и тд """
    for couple in word_tuple:
        print(f'{couple[0]:<1}' + ' ' * (50 - (len(str(couple[0])) + len(str(couple[1])))) + f'{couple[1]:<5} {units}')


# Работа с файлом и вытаскивание текста
file_with_text = open('Alice in Wonderland.txt', 'r', encoding='utf-8')
text_from_file = file_with_text.read()
file_with_text.close()
# Выводы результатов работы функций
input_rating_size = 10  # Размер списка рейтингов. Аргумент функций, можно задать при вызове функции. Задал тут
# что бы не громоздить
print(f'Список из {input_rating_size} слов с максимальной частотой повторения в тексте:')
print_rating_tuple(words_frequency_rating_tuple
                   (create_word_len_frequency_dict(text_from_file), input_rating_size), 'раз')
print('Можно создать список частоты вхождения слов с определенной длинной')
min_word_len_ = int(input('Минимальная длина слова: '))
max_word_len_ = int(input('Максимальная длина слова: '))
print_rating_tuple(words_frequency_rating_tuple
                   (create_word_len_frequency_dict
                    (text_from_file, min_word_len_, max_word_len_), input_rating_size), 'раз')
print(f'Список из {input_rating_size} самых длинных слов и их длина  ')
print_rating_tuple(words_by_len_rating_tuple
                   (create_word_len_frequency_dict(text_from_file), input_rating_size), 'букв')

print(f'Самое длинное слово: {find_longest_word(create_word_len_frequency_dict(text_from_file))}')
print(f'Общее количество слов в тексе: {total_words_in_dict(create_word_len_frequency_dict(text_from_file))}')
