# Завдання 1
dictionary = {}
with open('dict.txt', 'r', encoding='utf-8') as dict_file:
    for line in dict_file:
        english_word, ukrainian_word = line.strip().split('\t-\t')
        dictionary[english_word] = ukrainian_word

with open('translate.txt', 'r', encoding='utf-8') as translate_file:
    text_to_translate = translate_file.read()

translated_text = []
for word in text_to_translate.split():

    translated_word = dictionary.get(word, word) 
    translated_text.append(translated_word)

with open('output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(' '.join(translated_text))
