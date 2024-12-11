# # Завдання 1
# arr = (1,2,3,5,2)

# count = 0
# for i in arr:
#     if i == 2:
#         count += 1

# print(count)

# Завдання 2
# data = (10, 20, 30, 40, 50)

# element = int(input("Введіть елемент: "))

# if element in data:
#     print("Індекс елемента:", data.index(element))
# else:
#     print("Елемента немає")

# # Завдання 3
# data = (10, 20, 30, 40, 50)

# new_data = (data[0], data[-1])
# print("Новий кортеж:", new_data)

# Завдання 4
data = (10, 20, 30, 40, 50)

if all(element == data[0] for element in data):
    print("Всі елементи кортежу однакові.")
else:
    print("Елементи кортежу різні.")
