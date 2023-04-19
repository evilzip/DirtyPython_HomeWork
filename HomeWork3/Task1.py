# 1.  Дан список чисел. Создать новый список,
# который будет содержать только уникальные элементы исходного списка
import random

test_list_size = int(input('Размер списка: '))
test_list = [random.randint(-5,5) for i in range(test_list_size)]
print(test_list)
print(f'Список уникальных элементов: {list(set(test_list))}')
