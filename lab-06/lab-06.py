# # Завданння 1
# file = open('text.txt', 'w')
# file.write("Vitalii Prezent")
# file.close()

# # Завдання 2
# with open('tets-file.txt', 'w') as file:
#     lineСount = 0
#     charСount = 0

#     while True:
#         userInput = input("Введіть текст (порожній рядок для завершення): ")
        
#         if userInput == "":
#             break
        
#         file.write(userInput + '\n')
        
#         lineСount += 1
#         charСount += len(userInput)

# print("Кількість рядків: ", lineСount)
# print("Кількість символів: ", charСount)

# Завдання 3
# poetry = open('poetry.txt', 'r')
# lines = poetry.readlines()
# poetry.close()

# linesNotStartT = 0
# linesEndD = 0
# capitalizedWordsCount = 0


# for line in lines:

#     line = line.strip()

#     if not line.startswith('T'):
#         linesNotStartT  += 1

#     if line.endswith('d'):
#         linesEndD += 1

#     words = line.split()
#     for word in words:
#         if word[0].isupper():
#             capitalizedWordsCount += 1


# print("Кількість рядків, що не починаються з літери 'T':", linesNotStartT)
# print("Кількість рядків, що закінчуються на 'd':", linesEndD)
# print("Кількість слів, що починаються з великої літери:", capitalizedWordsCount)

# Завдання 5
# file = open('mbox-short.txt', 'r')
# lines = file.readlines()
# file.close()

# longestWord = ""
# max_length = 0

# for line in lines:
#     line = line.strip()

#     print("Кількість символів у рядку: ",len(line))

#     words = line.split()

#     for word in words:
#         if len(word) > maxLength:
#             maxLength = len(word)
#             longestWord = word

# print(f"Найдовше слово: {longestWord} (довжина: {maxLength} символів)")

# Завдання 6
file = open('mbox-short.txt', 'r')
lines = file.readlines()
file.close()


count = 0

for line in lines:
    if '@' in line:
        print(line.strip())  
        count += 1  

print("Кількість рядків, що містять знак '@':", count)
