# 3. у нас есть шахматная доска. по горизонтали нумерована цифрами,
# по вертикали буквами. написать программу,
# которая определяет цвет клетки по ее координатам (например B7 = Белая),
# если точно знаем, что клетка А1 - черная

cell_position = input('Какая клетка интересует: ')
horizontal_letter = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
# ниже проверяем ввод: должно быть два знака в строке, первый - буква, второй - цифра
if len(cell_position) == 2 and cell_position[0].isalpha() and cell_position[1].isdigit():
    if (cell_position[0]).upper() in horizontal_letter.keys() and (1 < int(cell_position[1]) < 9):
        if (horizontal_letter.get((cell_position[0]).upper()) + int(cell_position[1])) % 2 == 0:
            print('ЧЕРНАЯ')
        else:
            print('БЕЛАЯ')
    else:
        print('На шахматной доске нет такой клетки')
else:
    print('Ошибка формата ввода')
