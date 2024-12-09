# Завдання 1
# c = 1
# while c <=512:
#     print(c)
#     c*=2

# Завдання 2
# number = int(input("Введіть чотиризначне число: "))
# if 1000 <= number <= 9999:
#     num1 = number // 1000            
#     num2 = (number // 100) % 10      
#     num3 = (number // 10) % 10
#     num4 = number % 10            
    
#     sum = num1 + num2 + num3 + num4
#     print("Сума цифр числа:", sum)

# Завдання 3
# Ініціалізуємо змінні для зберігання введеного числа і суми додатніх чисел
total_sum = 0

while True:
    # Зчитуємо число від користувача
    user_input = int(input("Введіть число: "))
    
    # Перетворюємо введений рядок на ціле число
    number = 0
    negative = False
    for char in user_input:
        if char == '-':
            negative = True
            continue
        number = number * 10 + (ord(char) - ord('0'))
    
    if negative:
        number = -number

    # Якщо число від'ємне, завершуємо цикл
    if number < 0:
        break

    # Додаємо число до суми
    total_sum += number

# Виводимо суму додатніх чисел
print("Сума додатніх чисел:", total_sum)
