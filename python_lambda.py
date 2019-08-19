#1. fibonacci = [0,1,1,2,3,5,8,13,21,34,55] Найти четные и нечетные числа с помощью lambda переделать следующий код в более простой, т.е. не используя lambda и reduce:

f1 = lambda a, b: a + b
print(reduce(f1, range(1, 10)))

fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)

#2. Дано три массива одинаковой длины, все элементы типа int. Создать список с перемноженными поэлементно значениями (т.е. a=[1,2], b=[10,20], c=[100,200] -> [1000, 8000]).

list1=[1,2]
list2=[10,20]
list3=[100,200]
out = list(map(lambda x, y, c: x * y * c, list1, list2, list3))
print(out)