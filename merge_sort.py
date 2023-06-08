import random

def mergesort(list):
    if len(list)>1:
        mid = len(list)//2
        lefthalf = list[:mid]
        righthalf = list[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                list[k]=lefthalf[i]
                i=i+1
            else:
                list[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            list[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            list[k]=righthalf[j]
            j=j+1
            k=k+1
    

a = int(input('Введите начало диапазона: '))
b = int(input('Введите конец диапазона: '))
n = int(input('Введите число элементов масси: '))

list = [random.randint(a, b) for m in range(n)]

print('Несортированный:', '\n', list)
print('##############################')
mergesort(list)
print('Сортированный:', '\n', list)