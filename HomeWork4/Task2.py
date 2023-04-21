# 2. Написать функцию, которая будет возвращать список созданный по заданным критериям:
# размер,
# минимальное и максимальное значение,
# наличие повторяющихся элементовff

def create_list(list_length: int, min_value: int, max_value: int, element_recurrence=False) -> list:
    import random
    if max_value < min_value:
        print('Ошибка! Максимальный элемент не может быть меньше минимального!')
        return None
    list_no_recurrence = []
    if element_recurrence:
        return [random.randint(min_value, max_value) for _ in range(list_length)]
    else:
        if max_value - min_value >= list_length:
            while len(list_no_recurrence) < list_length:
                element = random.randint(min_value, max_value)
                if list_no_recurrence.count(element) == 0:
                    list_no_recurrence.append(element)
            return list_no_recurrence
        else:
            print('Ошибка! Невозможно создать список без повторяющихся элементов')


print(f'Список из чисел без повторений:\n {create_list(15, -10, 10)}')
print(f'Список чисел с повторениями: \n {create_list(15, -10, 10, element_recurrence=True)}')
