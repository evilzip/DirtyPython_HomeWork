# 5. Вводим сегодняшнюю дату и сегодняшний день недели,
# затем вводим новую дату и программа должна выдать нам какой день недели будет в эту дату
days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
days_in_month_visocos = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
week_days = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда', 4: 'Четверг', 5: 'Пятница', 6: 'Суббота', 7: 'Воскресенье'}

# test_date = input('Формат даты дд.мм.гггг: ')
# # Формат даты дд.мм.гггг
# base_date = '09.05.1945'
# base_week_day = 3


user_base_date = '18.04.2023' #input('Сегодняшняя дата дд.мм.гггг: ')
user_base_week_day= '2' #input('Какой сегодня день недели (от 1 до 7): ')
user_taste_date = input('Какая дата интересует дд.мм.гггг: ')
# проверка раньше или позже чем сейчас пользователь ввел дату
base_test = True
if int(user_taste_date[6:10]) > int(user_base_date[6:10]):
    test_date = user_taste_date
    base_date = user_base_date
elif int(user_taste_date[6:10]) == int(user_base_date[6:10]):
    if int(user_taste_date[3:5]) >= int(user_base_date[3:5]):
        test_date = user_taste_date
        base_date = user_base_date

elif int(user_taste_date[6:10]) == int(user_base_date[6:10]):
    if int(user_taste_date[3:5]) == int(user_base_date[3:5]):
        if int(user_taste_date[0:2]) >= int(user_base_date[0:2]):
            test_date = user_taste_date
            base_date = user_base_date
        else:
            test_date = user_base_date
            base_date = user_taste_date
            base_test = False
else:
    test_date = user_base_date
    base_date = user_taste_date
    base_test = False

# Берем год месяц и число из меньшей даты
total_days = 0
day_base = int(base_date[0:2])
month_base = int(base_date[3:5])
year_base = int(base_date[6:10])
# Берем год месяц и число из большей даты
day_test = int(test_date[0:2])
month_test = int(test_date[3:5])
year_test = int(test_date[6:10])
base_week_day = int(user_base_week_day)
######################################
if year_test > year_base:
    # Подсчет дней в годах между датами
    days_by_year = 0
    for year in range(year_base+1, year_test):
        if year % 4 == 0:
            days_by_year += 366
        else:
            days_by_year += 365
        year_base += 1
    # подсчет дней в месяцах между датами
    if month_base == month_test:
        total_days = days_by_year + day_test - day_base
    else:
        # подсчет количества дней от меньшей даты до конца ее года
        days_by_months_to_end_base_month = 0
        if year_base % 4 != 0:
            for key in days_in_month.keys():
                if int(month_base) < key:
                    days_by_months_to_end_base_month += days_in_month.get(key)
        else:
            for key in days_in_month_visocos.keys():
                if int(month_base) < key:
                    days_by_months_to_end_base_month += days_in_month_visocos.get(key)
        if month_base == 2:
            days_to_end_base_year = days_by_months_to_end_base_month + days_in_month_visocos.get(month_base) - day_base
        else:
            days_to_end_base_year = days_by_months_to_end_base_month + days_in_month.get(month_base) - day_base
        # подсчет дней от начала года до большей даты
        days_from_begin_test_month = 0
        if year_test % 4 != 0:
            for key in days_in_month.keys():
                if int(month_test) > key:
                    days_from_begin_test_month += days_in_month.get(key)
        else:
            for key in days_in_month_visocos.keys():
                if int(month_test) > key:
                    days_from_begin_test_month += days_in_month_visocos.get(key)
        days_from_begin_test_year = days_from_begin_test_month + day_test
        # суммирование всех выше подсчитанных дней
        total_days = days_by_year + days_to_end_base_year + days_from_begin_test_year
elif year_test == year_base: # если года раны
    if month_base == month_test:
        total_days = day_test - day_base
    elif month_test > month_base: # если месяцы равны
        days_by_months = 0
        for key in days_in_month.keys():
            if int(month_base) < key < int(month_test):
                days_by_months += days_in_month.get(key)
        days_to_end_base_month = days_in_month.get(month_base) - day_base
        total_days = days_by_months + days_to_end_base_month + day_test
total_weeks = total_days // 7
week_day = total_days % 7
if not base_test: # когда пользователь ввел даты раньше чем сегодня
    week_day = 7-week_day
if base_week_day + week_day > 7:
    total_week_day = week_days.get((base_week_day + week_day) % 7)
else:
    total_week_day = week_days.get(base_week_day + week_day)
print(f'День недели интересующей даты: {total_week_day}')