# 3. функцию для проверки числа:
#   - четность - нечетность
#   - простое число (имеет всего два делителя - само себя и единицу)
#   - сумма всех цифр числа является делителем этого числа
#   - *принимает число и выдает его только простые делителиff

def number_check(number:int) -> dict: # {is_even: True/False,
                                         # is_prime:True/False,
                                         #  is_sum_digits_divide: True/False
                                         #  , prime_dividers: [, , , ,]}
    _is_even = _is_prime = _is_sum_digits_divider = False
    if number%2==0:
        _is_even = True
    count_divider = 0
    divider_list = []
    for i in range(1,number+1):
        if number%i == 0:
            count_divider+=1
            divider_list.append(i)
    if count_divider < 3:
        _is_prime = True
    sum_digits = 0
    while number>0:
        current_digit = number%10
        sum_digits+=current_digit
        number//=10
    if number%sum_digits==0:
        _is_sum_digits_divider = True
    divider_dict = { }
    for divider in divider_list:
        for j in range(1, divider+1):
            if divider % j == 0:
                if divider in divider_dict.keys():
                    divider_dict[divider] = divider_dict.get(divider, 0) + 1
                else:
                    divider_dict[divider] = 1
    list_prime_dividers = [key for key,vale in divider_dict.items() if vale<3]
    return {'is_even':_is_even,
            'is_prime':_is_prime,
            'is_sum_digits_divider': _is_sum_digits_divider,
            'prime_dividers': list_prime_dividers}


user_input=int(input('Задайте натуральное число для проверки: '))
print(number_check(user_input))