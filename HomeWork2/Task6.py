# 6. ПРОСТЕЙШИЙ КАЛЬКУЛЯТОР

# Написать программу, которая выполняет над двумя вещественными числами одну из четырех арифметических операций
# (сложение, вычитание, умножение или деление):
# вводим первое число,
# потом операцию
# и второе число
# выводится результат
#
# Программа должна завершаться только по желанию пользователя:
# можно ввести enter и программа закончится, или еще операцию и еще число. Ну и помним, что на ноль делить нельзя.

math_operations = ('+', '-', '*', '/')
math_operations_selected = ''
user_number_input = 0
result = 0
flag_program_termination = True
output_to_console = {
    'enter_key': 'Ошибка! Пустой ввод приводит к завершению из программы!',
    'repeat_number': 'Ошибка! Повторный ввод числа приводит к завершению программы!',
    'repeat_operation': 'Ошибка! Повторный ввод операции приводит к завершению программы',
    'dev_by_zero': 'Ошибка! На ноль деление запрещено!Выход!',
    'math_operation': 'Действие : ',
    'allowed_operations': 'Можно только + - * /',
    'not_number': 'Это не число!'}
flag_input_start_number = True
while flag_input_start_number:
    user_number_float = True
    start_number = input('Введите 1е число: ')
    try:
        float(start_number)
    except ValueError:
        user_number_float = False
    if user_number_float:
        result = float(start_number)
        flag_input_start_number = False
        continue
    if start_number == '':
        print(output_to_console['enter_key'])
        flag_input_start_number = False
        flag_program_termination = False
        continue
    print(output_to_console['not_number'])


while flag_program_termination:

    flag_math_operation_input = True
    while flag_math_operation_input:  # Зацикленный ввод мат. операции
        user_number_float = True
        input_math_operation = input(output_to_console['math_operation'])
        try:
            float(input_math_operation)
        except ValueError:
            user_number_float = False
        if input_math_operation in math_operations:
            math_operations_selected = input_math_operation
            flag_math_operation_input = False  # Выход из цикла ввода мат. действия
            continue
        elif input_math_operation == '':  # Выход из всей программы - нажатие Enter = ввод пустой строки
            print(output_to_console['enter_key'])
            flag_math_operation_input = False
            flag_program_termination = False
            continue
        elif user_number_float:  # Выход из всей программы - повторный ввод числа
            print(output_to_console['repeat_number'])
            flag_math_operation_input = False
            flag_program_termination = False
            continue
        else:
            print(output_to_console['allowed_operations'])
            continue

    if flag_program_termination is not False:
        flag_number_input = True

        while flag_number_input:  # Зацикленный ввод числа. Выход из цикла - ввод числа с плав. точкой
            user_input = input('Введите число: ')
            user_number_float = True
            try:
                float(user_input)
            except ValueError:
                user_number_float = False
            if user_number_float:
                user_number_input = float(user_input)
                flag_number_input = False  # выход из цикла ввода числа.
                continue
            elif user_input == '':
                print(output_to_console['enter_key'])  # Выход из всей программы - нажатие Enter = ввод пустой строки
                flag_number_input = False
                flag_program_termination = False
                continue
            elif user_input in math_operations:
                print(output_to_console['repeat_operation'])  # Выход из всей программы - повторный ввод мат.операции
                flag_number_input = False
                flag_program_termination = False
                continue
        if flag_program_termination is not False:  # вычисления
            match math_operations_selected:
                case '+':
                    result = result + user_number_input
                case '-':
                    result = result - user_number_input
                case '*':
                    result = result * user_number_input
                case '/':
                    if user_number_input != 0:
                        result = result / user_number_input
                    else:
                        print(output_to_console['dev_by_zero'])
                        flag_program_termination = False
                        continue
            print(f'Текущий результат: {result} ')
