# 1. ПАЛИНДРОМЫ

# а) на вход подается слово - проверить, является ли оно палиндромом
# Например на слово  ‘довод’ выводит  ‘да’, а на слово  ‘повод’ - нет.
# Больше примеров слов-палиндромов
# довод, доход, заказ, кабак, комок, мадам, олололо, потоп, радар, ротатор, топот, шалаш
# level deified noon Racecar radar repaper

# б) на вход подается фраза - проверить, является ли она палиндромом
# Не учитывается регистр, знаки препинания и пробелы.
# Примеры фраз-палиндромов
# А роза упала на лапу Азора
# Я иду с мечем судия
# Хил, худ, а дух лих. ——> точки и запятые?
# Тарту дорог, как город утрат
# А путана тупа
# И темен город. Мороз, узором дорог не мети.
# Леша на полке клопа нашел.
# Аргентина манит негра
# Straw? No, too stupid a fad. I put soot on warts
# Was it a cat I saw?
# Do geese see God?
# Madam, I'm Adam
# Pull up if I pull
# No lemon, no melon
# SATOR AREPO TENET OPERA ROTAS

user_string = input('Введите ваше слово или строку для проверки на полиндромию:\n')

user_string_filtered = ''
reversed_user_string_filtered = ''
for i in range(len(user_string)):
    # Убираем из введеной строки все что не буквы и собираем прямую строку и строку в обратном порядке
    # (в нижнем регистре)
    if user_string[i].isalpha():
        user_string_filtered = user_string_filtered + user_string[i].lower()
        reversed_user_string_filtered = user_string[i].lower() + reversed_user_string_filtered
if user_string_filtered == reversed_user_string_filtered:
    print('Да! Это полиндром!')
else:
    print('Нет! Это не полиндром!')
