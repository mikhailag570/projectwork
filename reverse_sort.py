import random

def bubble_sr(array):
    for j in range(len(array) - 1):
        for i in range(len(array) - 1 - j):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array
  
a = int(input('Введите начало диапазона: '))
b = int(input('Введите конец диапазона: '))
n = int(input('Введите число элементов масси: '))

arr = [random.randint(a, b) for _ in range(n)]

print('Исходный массив:', arr)
print('Обратная пузырьковая:', bubble_sr(arr[:]))