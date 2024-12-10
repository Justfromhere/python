# Завдання 1
# dictionary = {}
# dict_file = open('dict.txt', 'r')
# for line in dict_file:
#     parts = line.split('\t-\t')  
#     english_word = parts[0]  
#     ukrainian_word = parts[1].strip()  
#     dictionary[english_word] = ukrainian_word 
# dict_file.close() 


# translate_file = open('translate.txt', 'r')
# text_to_translate = translate_file.read() 
# translate_file.close() 


# translated_text = []  
# words = text_to_translate.split()  
# for word in words:
#     if word in dictionary: 
#         translated_text.append(dictionary[word])  
#     else:
#         translated_text.append(word)  


# output_file = open('output.txt', 'w')
# output_file.write(' '.join(translated_text))  
# output_file.close()  

# Завдання 2
countries = {}

with open('input_countries.txt', 'r', encoding='utf-8') as file:
    for line in file:
        sep = line.split(' : ')
        country = sep[0]
        lengs = sep[1]
        countries[country] = lengs

inputLeng = input('Введіть мову: ')

result = []

for country, lengs in countries.items():
    if inputLeng in lengs:
        result.append(country)

if result:
    print("Країни, де розмовляють цією мовою:", result)
else:
    print("Такої мови немає в списку.")
