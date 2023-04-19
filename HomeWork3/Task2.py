# 2. Мы уже делали переводчик числа из десятичной в двоичную в двоичную,
# самое время сделать для восьмиричной и шестнадцатиричной.
# а лучше сделать универсальный (двоичная, восьмиричная, шеснадцатиричная)
# и подумать как интереснее оформить "меню" выбора в какую систему переводим:)

user_number = int(input('Введите ваше число: '))
user_choiсe = input('В какую систему счисления перевести (2, 8 или 16): ')
result_dict = {'2':'', '8':'', '16':''}
match user_choiсe:
    case '2':
        binary_user_number = ''
        while user_number > 0:
            binary_user_number = str(user_number%2) + binary_user_number
            user_number //= 2
        result_dict['2'] = binary_user_number
    case '8':
        octal_user_number = ''
        while user_number > 0:
            octal_user_number = str(user_number%8) + octal_user_number
            user_number //= 8
        result_dict['8'] = octal_user_number
    case '16':
        hexal_letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        hexal_user_number = ''
        while user_number > 0:
            if user_number % 16 > 9:
                remains = hexal_letters.get(user_number % 16)
            else:
                remains = user_number % 16
            hexal_user_number = str(remains) + hexal_user_number
            user_number //= 16
        result_dict['16'] = hexal_user_number

print(f'Ваше число в {user_choiсe}-ной системе {result_dict.get(user_choiсe)}')