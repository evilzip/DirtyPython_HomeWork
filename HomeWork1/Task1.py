# 1. На вход поступает число: найти сумму цифр числа, в том числе если оно отрицательное или вещественное. (float)

user_number = input('ВВедите ваше число: ')
symbols_set = ('+', '-', ',', '.')
number_set = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
numbers_sum = 0
is_number = False
for current_symbol in user_number:
    if not current_symbol in symbols_set and current_symbol in number_set:
        numbers_sum += int(current_symbol)
        is_number = True
print(f'Сумма всех цифр в вашем числе {numbers_sum}' if is_number is not False else 'Вы ввели не число')

