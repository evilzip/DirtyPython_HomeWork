# 1. Реализовать алгоритм RLE (упрощенный - это на случай вдруг вы полезете в Wiki)
# что такое RLE? алгоритм сжатия данных, например
# ssssdddfffffgggggggghhkkk -> 4s3d5f8g2h3k
# запаковка и распаковка в обратную сторону
# делаем файл с рандомно созданными строками (как запакованными, так и распакованными)
# считываем файл функция определяет - запакована строка или распакована
# и выполнить соответствующий алгоритм - результаты записать в новый файл
import random


def rle_string_coding(input_string: str) -> str: # кодирование строки
    first_letter = input_string[0]
    result_string = ''
    k = 0
    for letter in input_string:
        if letter != first_letter:
            result_string = result_string + str(k) + first_letter
            first_letter = letter
            k = 1
        elif letter == first_letter:
            k += 1
    else:
        result_string = result_string + str(k) + first_letter
    return result_string


def rle_string_decoding(input_string: str) -> str: # раскодирование строки
    result_string = ''
    for i in range(len(input_string)):
        if not input_string[i].isdigit():
            result_string = result_string + int(input_string[i - 1]) * input_string[i]
    return result_string


def create_random_rle_string() -> str: # генерация рандомных строк RLE закодированнх и раскодоированных
    option_tuple = ('c', 'd')
    option = option_tuple[random.randint(0, 1)]
    rle_string = ''
    len_rle_string = random.randint(1, 20)
    match option:
        case 'd': # создание декодированной строки
            for _ in range(len_rle_string):
                flag = random.randint(0, 1)
                if flag:
                    rle_string = rle_string + random.randint(0, 5) * chr(random.randint(ord('A'), ord('Z')))
                else:
                    rle_string = rle_string + random.randint(0, 5) * chr(random.randint(ord('a'), ord('z')))

        case 'c': # создание кодированной строк
            for _ in range(len_rle_string):
                flag = random.randint(0, 1)
                if flag:
                    rle_string = rle_string + str(random.randint(1, 5)) + chr(random.randint(ord('A'), ord('Z')))
                else:
                    rle_string = rle_string + str(random.randint(1, 5)) + chr(random.randint(ord('a'), ord('z')))
    return rle_string


file = open('RLE strings input.txt', 'w') # очистка файла перед записью
file.close()

file = open('RLE strings input.txt', 'a', encoding='UTF-8') # запись в файл 20 рандомных строк RLE
# (кодированных и не кодированных)
for _ in range(1, 20):
    file.write(create_random_rle_string() + '\n')
file.close()

with open('RLE strings input.txt', 'r', encoding='UTF-8') as file: #чтение из файла заддных строк RLE
    RLE_strings_from_file = file.readlines()

file = open('RLE strings result.txt', 'w')# очистка файла результатов кодирования/декодирования
file.close()

file = open('RLE strings result.txt', 'a', encoding='UTF-8') # запись результата в файл RLE strings result.txt
# преобразования строк  взятых из файла RLE strings input.txt
for line in RLE_strings_from_file:
    if any(map(str.isdigit, line.strip())):
        file.write(rle_string_decoding(line.strip()) + '\n')
    else:
        file.write(rle_string_coding(line.strip()) + '\n')
file.close()
