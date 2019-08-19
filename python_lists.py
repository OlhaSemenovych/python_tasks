#1. Дан список ['a', 'b', 'c', ['None'], {}]. Проверить, есть ли в списке None объект.

some_list = ['a', 'b', 'c', ['None'], '{}']
result = []
for i in some_list:
    if isinstance(i, (list,)):
        for j in i:
            result.append(j)
            if j == 'None':
                print('This world is here')
            else:
                print('This world is not here')
                
#2. Дан список из строк. Изменить регистр всех букв на противоположный. Т.е. ['Abc', 'cBD'] --> ['bBC', 'Cbd'].

some_list = ['Abc', 'cBD']
some_str = ' '.join(some_list)
print(some_str.swapcase())    



#3. Создать список, в котором каждый элемент - 2,3,4..10-ая степень числа с клавиатуры.

num = int(input('Please enter number:'))
some_list = []
for i in range(10):
    new_num = num**i
    some_list.append(new_num)
print(some_list)

#4. Создайте список, содержащий элементы целочисленного типа, измените тип данных элементов на числа с плавающей точкой (int --> float())
a = [4,5,8,2,34,5,67,89,57]
new_list = []
for item in a:
    new_list.append(float(item))
print(new_list)


#5. Удалить дубликаты из списка var = ['7','2','2','4','7','6','7','8']
var = ['7','2','2','4','7','6','7','8']
c = []
for item in var:
    found = False
    for item1 in c:
        if item == item1:
            found = True
    if found == False:    
        c.append(item)
print(c)

#6. Дано два списка: a = [1, 2, 3, 4], b = [1, 7, 21, 4]. Удалить из списка a элементы, которые встречаются в списке b
a = [1, 2, 3, 4]
b = [1, 7, 21, 4]
c = []
for item in a:
    found = False
    for item1 in b:
        if item == item1:
            found = True
    if found == False:    
        c.append(item)
print(c)   

#7. Удалить первый, третий и шестой элементы списка list_1 = ['1','2','3','4','5','6','7','8'].

list_1 = ['1','2','3','4','5','6','7','8']
list_1.pop(0)
list_1.pop(2)
list_1.pop(5)
print(list_1)


#8. Есть два списка. Найдите пересекающиеся элементы и выведите их. Если в них будут подсписки ['7', '8'] и ['8', '9'] - '8' - не является пересечением.

a = ['7', '8', '9']
b = ['8', '9', '1', '2']
result = list(set(a) & set(b))
print(result)

#9. Создайте список из 20 элементов. Если индекс элемента делится нацело на 5 - удалите его. Выведите получившийся список в одну строку без квадратных скобок.

a = """willsimplyloopoverthekeysinthediction"""
lst = list(a)
out = []
for index, val in enumerate(lst):# enumerate - показує індекс
    if index % 5 != 0:
        out.append(val)
print(out)  


#10. В списке  list_5 = ['1','2','3','4','5','6','7','8'] найти индекс (порядковый номер начиная с 0) элемента "5", затем удалить элемент с индексом 0 снова найти индекс "5"
list_5 = ['1','2','3','4','5','6','7','8']
list_1 = list_5.index('5')
print(list_1)

#11. Распаковать все подсписки списка с одним уровнем вложенности (fruits = ['orange', ['apple'], 'pear', 'banana', ['kiwi', 'apple', 'banana']]), дубликаты удалить.
fruits = ['orange', ['apple'], 'pear', 'banana', ['kiwi', 'apple', 'banana']]
res = []
for i in fruits:
    if isinstance(i, (list,)):
        for j in i:
            res.append(j)
    else:
        res.append(i) 
c = []
for item in res:
    found = False
    for item1 in c:
        if item == item1:
            found = True
    if found == False:    
        c.append(item)
print(c)  

#12. Есть два списка целочисленных данных. Найти наибольший из них по сумме чисел
from functools import reduce
li_1 = [5, 8, 10, 20, 50, 100] 
li_2 = [5, 7, 10, 200, 1, 100] 
max_sum = max(reduce((lambda x, y: x + y), li_1), reduce((lambda x, y: x + y), li_2)) 
print(max_sum) 

#13. Дан список a = ['1', '2', '3', '5']. Ваша программа должна преобразовать этот список в a = ['1', '4', '9', '25']

numbers = [1, 2, 3, 4, 5]
sq_nums = []
for num in numbers:
        sq_nums.append(num*num)

print(sq_nums)

li = [1, 2, 3, 4, 5]
final_list = list(map(lambda x: x*x , li)) 
print(final_list)

#14. Есть два списка: a = [1, 2, 3, 11, 15] b = [3, 33, [4, 5, [7, 8]], 6, 9, 10, 22]. Создайте отсортированный список без вложенности (т.е. 4,5,7,8 должны быть вынесены в основной список).

a = [1, 2, 3, 11, 15]
b = [3, 33, [4, 5, [7, 8]], 6, 9, 10, 22]
new_list = []
for i in b:
    if isinstance(i,list):
        for j in i:
            if isinstance(j, list):
                new_list.extend(j)
            else:
                new_list.append(j)    
    else:
        new_list.append(i)
new_list.extend(a)
new_list.sort()
print (new_list)


#15. Дан список a = [1, 2, 3, 5]. Для каждого i выведите i  в степени i, т.е. a = [1, 4, 81, 3125].

numbers = [1, 2, 3, 4, 5]
sq_nums = []
for num in numbers:
        sq_nums.append(num**num)

print(sq_nums)

li = [1, 2, 3, 4, 5]
final_list = list(map(lambda x: x**x , li)) 
print(final_list)