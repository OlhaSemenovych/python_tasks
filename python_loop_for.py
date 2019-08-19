#1. Нужно создать кортеж который будет заполнен числами Фибоначчи от 0 до числа которое будет на больше заданногочисла max_value (100). Вывести максимальное значение этого кортежа.'''

to_fib=(0,1)
new_fib = list(to_fib)
for i in range (50):
    new_fib.append(new_fib[-1]+new_fib[-2])
    if new_fib[-1] > 100:
        break
print(max(new_fib))


#2. Дан список a = [1, 2, 3, 5]. Для каждого i выведите i  в степени i, т.е. a = [1, 4, 81, 3125].

numbers = [1, 2, 3, 4, 5]
sq_nums = []
for num in numbers:
        sq_nums.append(num**num)

print(sq_nums)

li = [1, 2, 3, 4, 5]
final_list = list(map(lambda x: x**x , li)) 
print(final_list)

#3. Дан список a = ['1', '2', '3', '5']. Ваша программа должна преобразовать этот список в a = ['1', '4', '9', '25']

numbers = [1, 2, 3, 4, 5]
sq_nums = []
for num in numbers:
        sq_nums.append(num*num)

print(sq_nums)

li = [1, 2, 3, 4, 5]
final_list = list(map(lambda x: x*x , li)) 
print(final_list)

#4. Постройте последовательность фибоначчи с помощью обычной функции, а потом с помощью lambda. В начальной точке у вас есть список to_fib = [0, 1].

to_fib=[0,1]
for i in range (50):
    to_fib.append(to_fib[-1]+to_fib[-2])

print(to_fib)

#5. Создайте словарь, в котором значение типа int. Выведите на экран ключ - значение+1 , например a = {'f': 5, 'd': 7} выведет f - 6, d - 8.

a = {'f': 5, 'd': 7}
for key in a:
    c = a[key] + 1
    print(key, '-', c)
    
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

#7. Удалить дубликаты из списка var = ['7','2','2','4','7','6','7','8']
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

#8. Распаковать все подсписки списка с одним уровнем вложенности (fruits = ['orange', ['apple'], 'pear', 'banana', ['kiwi', 'apple', 'banana']]), дубликаты удалить.
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
        
        
#9. Создайте список, содержащий элементы целочисленного типа, измените тип данных элементов на числа с плавающей точкой (int --> float())
a = [4,5,8,2,34,5,67,89,57]
new_list = []
for item in a:
    new_list.append(float(item))
print(new_list)

#10. Создать список, в котором каждый элемент - 2,3,4..10-ая степень числа с клавиатуры.

num = int(input('Please enter number:'))
some_list = []
for i in range(10):
    new_num = num**i
    some_list.append(new_num)
print(some_list)


#11. Дан список ['a', 'b', 'c', ['None'], {}]. Проверить, есть ли в списке None объект.

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
                

#12. Задан словарь d = {'Name': ['Zara', 'John', "Michael"], 'Age': [7, 19, 16], 'Class': ['First', None, "Eleventh"]}, где порядковый номер значения отвечает одному и тому же человеку например: Заре 7 лет, ходит в первый класс, добавить в словарь еще одного человека. Затем записать в файл имя, возвраст и класс каждого человека, каждого с новой строки.

my_dict = {'Name': ['Zara', 'John', "Michael"],
'Age': [7, 19, 16],
'Class': ['First', None, "Eleventh"]}
d['Name'].append('Andry')
d['Age'].append('34')
d['Class'].append('Second')
for i in range(len(my_dict['Name'])):
    print(i,my_dict['Age'],my_dict['Class'])
    
#13. Создайте список из 20 элементов. Если индекс элемента делится нацело на 5 - удалите его. Выведите получившийся список в одну строку без квадратных скобок.

a = """willsimplyloopoverthekeysinthediction"""
lst = list(a)
out = []
for index, val in enumerate(lst):# enumerate - показує індекс
    if index % 5 != 0:
        out.append(val)
print(out)  


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


#15.
'''Создать словарь из двух ключей "Male", "Female", их значения - пустые словари.
Мы добавляем в словарь имена:
names = "girl:Emma, boy:Logan, boy:Noah, girl:Olivia, girl:Ava, boy:Liam, girl:Isabella,
boy:Mason, girl:Sophia, boy:Elijah, girl:Mia, boy:James, girl:Charlotte,
girl:Amelia, boy:Benjamin, girl:Evelyn, boy:William, girl:Abigail"
Если имя женское - в значении создаем букву, с которой начинается имя, его значением будет список,
в список записываем имя. Если первая буква имени уже встречалась - дописываем в существующий список имя.
Если не встречалась - создаем букву, список и записываем имя в список.
например:
d = {"Male": {"E": ["Elijah"],
              "L": ["Logan", "Liam"]}}'''
              

lst = """girl:Emma, boy:Logan, boy:Noah, girl:Olivia, girl:Ava, boy:Liam, girl:Isabella, boy:Mason, girl:Sophia, boy:Elijah, girl:Mia, boy:James, girl:Charlotte, girl:Amelia, boy:Benjamin, girl:Evelyn, boy:William, girl:Abigail"""
out = {'Male':{}, 'Female':{}}
new_names = lst.split(", ")
for i in new_names:
    sex_name = i.split(':')
    if sex_name[0] == 'boy':
        key = 'Male'
    elif sex_name[0] == 'girl':
        key = 'Female'
    letter = sex_name[1][:1]    
    if out[key].get(letter) == None:
        out[key][letter] = [sex_name[1]]
    else:
        out[key][letter].append(sex_name[1])  
print(out) 