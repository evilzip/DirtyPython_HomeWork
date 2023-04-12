#3. На вход поступает десятичное число, вывести его в виде двоичного

user_number = int(input('Введите ваше число: '))
binary_user_number = ''
while user_number>0:
    binary_user_number = str(user_number%2) + binary_user_number
    user_number //= 2

print(f'Ваше число в двоичной системе {binary_user_number}')