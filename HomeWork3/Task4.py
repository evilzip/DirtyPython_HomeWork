# 4. Принимаем с консоли число и выводим две последовательности Фибоначчи и Негафибоначчи
# (можно прочитать в wiki что это)
# Пример: Вводим 8
# [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
limit_number = int(input('Длина последовательности чисел Фибоначи и НегаФибоначи: '))
fibo_list = [1, 0, 1]
shift = 0
for i in range(3, limit_number + 2):
    fibo_list.append(fibo_list[(i + shift) - 1] + fibo_list[(i + shift) - 2])
    fibo_list.insert(0, (fibo_list[1] - fibo_list[0]))
    shift += 1
print(fibo_list)
