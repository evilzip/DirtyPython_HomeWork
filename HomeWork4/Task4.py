# 4. Функция принимает предложение, вычислzет какой буквы в этом предложении больше и возdращает эту букву и
# процент ее вхождения предложениеff

def letter_counter(input_string: str):
    frequency_dict = {}
    for symbol in input_string:
        if symbol.isalpha():
            if symbol in frequency_dict.keys():
                frequency_dict[symbol] = frequency_dict.get(symbol, 0) + 1
            else:
                frequency_dict[symbol] = 1

    for key, value in frequency_dict.items():
        if value == max(frequency_dict.values()):
            symbol_max_frequency = key
    symbol_max_frequency_percent = round(max(frequency_dict.values())/sum(frequency_dict.values())*100,2)
    return symbol_max_frequency, symbol_max_frequency_percent

user_sentence = 'лываываопдлофыва dddddddddd ffffffffffffffffffffffffffff'
print(letter_counter(user_sentence))


