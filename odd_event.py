# Подсчет четных и нечетных цифр в числе

a = int(input('Введите число: '))

even = 0
odd = 0

while a > 0:
  if a % 2 == 0:
    even += 1
  else:
    odd += 1
  a = a // 10

print(' Четных: ', even, '\n',
      'Нечетных: ', odd)