import random

n = int(input('Введите длину массива: '))

# Генерируем список последовательных целых чисел заданной длины
lst = list(range(n))

# Перемешиваем список
random.shuffle(lst)

print('Исходный массив:', '\n', lst)

# Разделитель

print('_________________________')

# Меняем местами минимальный и максимальный элемент

lst[lst.index(max(lst))], lst[lst.index(min(lst))] = lst[lst.index(min(lst))], lst[lst.index(max(lst))]

print('Измененный массив:', '\n', lst)