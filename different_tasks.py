#1. Найти факториал случайного числа от 1 до 20.

import math
import random
a = random.randint(1,20)
print (math.factorial(a))

#2. Дана строка. Переделать ее так чтобы каждая вторая буква была в верхнем регистре. Вывод: aBcDe

import string
str = string.ascii_lowercase
num = 0
new_word = []
for i in str:
    if num % 2 == 0:
        num += 1
        new_word.append(i.upper())
    else:
        num += 1
        new_word.append(i.lower())
print(''.join(new_word))

#3. Есть пары (('1', 1),('2', 2),('3', 3)). Создайте словарь с помощью генератора словаря.

some_tuple = (('1', 1),('2', 2),('3', 3))
tuple_123 = {v: k for k, v in iter(some_tuple)}
print(tuple_123)

#4. Есть список [{'a': 123, 'b': 1234}, {'a': 3222, 'b': 1234}, {'a': 123, 'b': 1234}]. Удалить дубликаты с помощью генератора.

lst = [{'a': 123, 'b': 1234}, {'a': 3222, 'b': 1234}, {'a': 123, 'b': 1234}]
unique = []
for item in lst:
    if item not in unique:
        unique.append(item)

print(unique)

#5. Постройте последовательность фибоначчи с помощью обычной функции. В начальной точке у вас есть список to_fib = [0, 1].

to_fib=[0,1]
for i in range (50):
    to_fib.append(to_fib[-1]+to_fib[-2])

print(to_fib)

#6. Bвести с клавиатуры символы. Если это не число - вывести их на экран.

num = input("Please, enter something:")
if not num.isdigit():
    print('You have entered anything, but not a number!')
else:
    print("This is number!")

#7. Напечатать сегодняшнюю дату (import time)   

import datetime
now = datetime.datetime.now()
print(now)

#8. Найти остаток от деления двух чисел с клавиатур.

a = int(input('Please enter first number:'))
b = int(input('Please enter second number:'))
print(a % b)


