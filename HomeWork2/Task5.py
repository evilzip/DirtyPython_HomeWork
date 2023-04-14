# 5. FIZZ BUZZ

# Напишите программу, которая выводит на экран числа от 1 до n. При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz», а вместо чисел, кратных пяти — слово «Buzz».
# Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»

limit_number = int(input('Введите, до какого числа нужно вывести последовательность: '))
current_number = 1
while current_number <= limit_number:
    if current_number % 5 == 0 and current_number % 3 == 0:
        print('"FizzBuzz"')
    elif current_number % 5 == 0:
        print('"Buzz"')
    elif current_number % 3 == 0:
        print('"Fizz"')
    else:
        print(current_number)
    current_number += 1
