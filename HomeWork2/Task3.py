# 3. ИСТИННОСТЬ ПРЕДИКАТ

# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# Данное выражение истинно при любых значениях предикат (предикат - переменная, которая может иметь
# только два значения True или False)
# Напишите программу, которая докажет это.
# https://ru.wikipedia.org/wiki/Список_логических_символов - вот вам ссылочка, если непонятно, что за символы)
expression_true = True
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not (x or y or z) == ((not x) and (not y) and (not z)):
                print(f'Комбинации при которых выражение истинно: x={x}, y={y}, z={z}')
            else:
                expression_true = False
                print(f'Комбинации при которых выражения НЕ истинно: x={x}, y={y}, z={z}')
print('Доказано, выражение истинно' if expression_true else '')
