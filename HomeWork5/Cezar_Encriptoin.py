# shift_code = int(input('Сдвиг: '))
# # test_text = 'Привет дуралей'

letters_rus_lower = [chr(i) for i in range(ord('а'), ord('я')+1)]
letters_rus_upper = [chr(i) for i in range(ord('А'), ord('я')+1)]
letters_eng_lower = [chr(i) for i in range(ord('A'), ord('Z')+1)]
letters_eng_upper = [chr(i) for i in range(ord('a'), ord('z')+1)]


def cesar_letter_encrypted(symbol: str, letter_list: list, shift: int) -> str:
    if symbol.isalpha():
        return letter_list[((letter_list.index(symbol)) + shift) % len(letter_list)]
    return symbol


def letter_language_detect(symbol: str) -> list:
    if symbol in letters_rus_lower:
        return letters_rus_lower
    elif symbol in letters_rus_upper:
        return letters_rus_upper
    elif symbol in letters_eng_lower:
        return letters_eng_lower
    elif symbol in letters_eng_upper:
        return letters_eng_upper
    return []


def cesar_text_encryption(text_for_encryption: str, shift: int) -> str:
    text_encrypted = ''
    for i in range(len(text_for_encryption)):
        text_encrypted = text_encrypted + \
                         cesar_letter_encrypted(text_for_encryption[i],
                         letter_language_detect(text_for_encryption[i]), shift)
    return text_encrypted



_shift = int(input('Сдвиг: '))
test_text = 'Привет дуг мой! Шла Саша по шоссе и сосала сушку;%"?:%*?%№?*: Helo, my friend!Easy come easy go'
print(f'Зашифрованный текст:\n{cesar_text_encryption(test_text, _shift)}')
print(f'Расшифрованный текст:\n{cesar_text_encryption(cesar_text_encryption(test_text, _shift), - _shift)}')
