#1. Нужно создать кортеж который будет заполнен числами Фибоначчи от 0 до числа которое будет на больше заданногочисла max_value (100). Вывести максимальное значение этого кортежа.'''

to_fib=(0,1)
new_fib = list(to_fib)
for i in range (50):
    new_fib.append(new_fib[-1]+new_fib[-2])
    if new_fib[-1] > 100:
        break
print(max(new_fib))


#2. Есть список, состоящий из файлов результатов выполнения программы. a = ['step1.xml', 'step2.xml', 'step1_log.xml', 'step3.xml', 'step2_log.xml']. Погруппировать его в двойки кортежей, если файл log не в списке, его значение может быть None.

a = ['step1.xml', 'step2.xml', 'step1_log.xml', 'step3.xml', 'step2_log.xml']
b = a[0:2]
c = a[2:4]
d = a[4:]
if d[-3:] == 'log':
    d.replace('log','None')
print(b,c,d)

#3. Дан кортеж a = (1,4,9,12,34,8,3) Проверить, все ли/хотя бы одно из чисел >0, >12, <6
a = (1,4,9,12,34,8,3)
if all(a) > 12:
    print(all(a))
    
#4. Палиндром
my_str = (input('Please enter some world:'))
my_str = my_str.lower()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
   print("YES")
else:
   print("NO")
   
#5. Создайте функцию, которой на вход передается любой тип данных. Если это строковая переменная - выведите 1, если список - выведите 2, во всех остальных случаях - 3.

num = input('Please enter something:')
def some_func(num):
    if type(num) == str:
        print(1)
    elif type(num) == list:
        print(2)
    else:
        print(3)
    return (num)

print(some_func(num))

#6. Создать список. Проверить, является ли список пустым.
some_list = []
if len(some_list) == 0:
    print('This list is empty')
else:
    print('This list is full')
    
#7. Ввести число с клавиатуры. Если оно больше 100 или меньше 0 напечатать "not in range 0..100". Если оно входит в диапазон [0-50] - напечать "in range 0..50". Если оно в диапазоне [51-100] - напечатать "in range 51..100".

num = int(input('Please, enter something:'))
if num > 100 and num < 0:
    print("not in range 0..100")
if num <= 50 and num >= 0:
    print("in range 0..50")
if num >= 51 and num <= 100:
    print("in range 51..100")
    
#8. Дано два списка: a = [1, 2, 3, 4], b = [1, 7, 21, 4]. Удалить из списка a элементы, которые встречаются в списке b
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

#9. Удалить дубликаты из списка var = ['7','2','2','4','7','6','7','8']
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

#10. Распаковать все подсписки списка с одним уровнем вложенности (fruits = ['orange', ['apple'], 'pear', 'banana', ['kiwi', 'apple', 'banana']]), дубликаты удалить.
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
                


#12.
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
