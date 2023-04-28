# написать программу, которая прочитает этот файл. после этого
#
# надо изменить текст, чтобы каждое предложение было записано
#
# с большой букы (после точки большая буква). и записать текст
#
# обратно в этот файл. скинуть на репозиторий этот файл и файл
#
# с самой программой.

file_with_text = open('sample.txt', 'r', encoding='utf-8')
text_from_file = file_with_text.read()
list_all_sentences = text_from_file.split('. ')
corrected_text = '. '.join([sentence.replace(sentence[0], sentence[0].title(), 1) for sentence in list_all_sentences])
file_with_text.close()
file_to_write = open('sample.txt', 'r+', encoding='utf-8')
file_to_write.write(corrected_text)
file_to_write.close()

