#1. Выведите на экран элементы словаря с помощью цийла while и блока try/except:

some_dict = {'dict': 1, 'dictionary': 2}
a = iter(some_dict.items())
while True:
    try:
        print(next(a))
    except StopIteration:
        break
        
#2. d = {'a': 1, 'b': 2, 3: 'c'}). Оставить пару ключ-значение, только если ключ является стрингом
d = {'a': 1, 'b': 2, 3: 'c'}
print({k: v for k, v in d.items() if type(k) is str})

#3. Задан словарь d = {'Name': ['Zara', 'John', "Michael"], 'Age': [7, 19, 16], 'Class': ['First', None, "Eleventh"]}, где порядковый номер значения отвечает одному и тому же человеку например: Заре 7 лет, ходит в первый класс, добавить в словарь еще одного человека. Затем записать в файл имя, возвраст и класс каждого человека, каждого с новой строки.

my_dict = {'Name': ['Zara', 'John', "Michael"],
'Age': [7, 19, 16],
'Class': ['First', None, "Eleventh"]}
d['Name'].append('Andry')
d['Age'].append('34')
d['Class'].append('Second')
for i in range(len(my_dict['Name'])):
    print(i,my_dict['Age'],my_dict['Class'])
    
#4.
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