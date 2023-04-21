# 1. Написать функцию, которая принимает на вход строку из рандомных цифр и букв, а возвращает:
#   - строку только из букв
#   - строку только из цифр
#   - сравнить длину строк из цифр и из букв и вернуть ту, которая длиннее

def string_exclude_letters(input_string: str)->str:
    output_string = input_string
    for symbol in output_string:
        if symbol.isalpha():
            output_string = output_string.replace(symbol,'')
    return output_string


def string_exclude_numbers(input_string: str)->str:
    output_string = input_string
    for symbol in output_string:
        if symbol.isdigit():
            output_string = output_string.replace(symbol,'')
    return output_string


def string_length_comparation(input_string: str)->str:
    if len(string_exclude_numbers(input_string)) > len(string_exclude_letters(input_string)):
        return string_exclude_numbers(input_string)
    else:
        return string_exclude_letters(input_string)



any_string = 'jahsdlfjhasd9709870sdalfhsldkjfhlas'
print(any_string)
print(f'Строка без букв: \n {string_exclude_letters(any_string)}')
print(f'Стока без цифр:\n {string_exclude_numbers(any_string)}')
print(f'Стока которая длиннее:\n {string_length_comparation(any_string)}')
