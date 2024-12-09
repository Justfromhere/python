# Завдання 1
# for number in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
#     print(number)

# # Завдання 2
# A = 20
# B = 10

# if A < B:
#     while A <= B:
#         print(A)
#         A += 1
# else:
#     while A >= B:
#         print(A)
#         A -= 1

# # Завдання 3
# total = 1 

# print("Введіть 10 чисел:")
# for i in range(10):
#     number = int(input("Число: "))
#     total += number

# print("Добуток введених чисел:", total)

# Завдання 4
# print("Введіть 10 чисел:")

# numbers = [] 

# for i in range(10):
#     number = int(input("Число: "))
#     if number % 2 == 0:
#         numbers.append(number)

# print("Парні числа:", numbers)

# Завдфння 5
# biggestNum = 0

# for i in range(10):
#     num = int(input('Число: '))
#     if num > biggestNum:
#         biggestNum = num

# print("Найбільше число:", biggestNum)

# Завдання 6
# user_input = input("Введіть рядок: ")

# for i in range(len(user_input)):
#     if i % 2 == 0: 
#         print(user_input[i]) 

# Завдання 7
for i in range(1, 10):
    if i <= 5:
        print('* ' * i) 
    else:
        print('* ' * (10 - i))  
