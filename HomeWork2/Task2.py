# 2. ТАБЛИЦА УМНОЖЕНИЯ

# Напишите программу, которая будет выводить в консоль таблицу умножения от 1 до 10
# (как в вконце старых тетрадок, квадратная такая


horizontal_header_numbers = ''
# header_horizontal_lines = ''
for i in range(1, 11):
    horizontal_header_numbers = horizontal_header_numbers + '{:>4}'.format(str(i))

print('  ' + '|' + horizontal_header_numbers)
print('-' * 43)

for i in range(1, 11):
    horizontal_string_results = ''
    for j in range(1, 11):
        horizontal_string_results = horizontal_string_results + '{:>4}'.format(str(i * j))
    print('{:>2}'.format(str(i)) + '|' + horizontal_string_results)

