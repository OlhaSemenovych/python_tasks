
#1
'''2.1 Создайте словарь с именами-ключами и паролями-значениями.
Создайте функцию get_user_name, которая вернет введенное с клавиатуры имя пользователя, get_user_pass - вернет пароль
Создайте функцию login для верификации логина и пароля согласно существующему словарю. Если данные не верифицированы -
повторяйте, пока пользователь не введет правильные лог/пас
Создайте функцию, которая делает, что вы хотите, если модуль запущен сам по себе'''

users = {'jason': 'oeros', 'nicole': 'chance'}

def get_user_name():
    username = input('Username: ')
    return username

def get_user_pass():
    password = input('Password: ')
    return password
    
def login():
    while True:
        username = get_user_name()
        password = get_user_pass()
        if users.get(username) and users.get(username) == password:
            print('Welcome!')
            break
        else:
            print('Not corect login or password! Try again')
            continue

login()   

#1. Переделайте задачу 1, чтобы print напечатал таблицу умножения для числа 3.

def mult(number):
    for i in range(11):
        tab = "{} x {} = {}".format(number, i, number*i)
        return(tab)
number = 3
print(mult(number))

#2. Создайте функцию, которая будет рандомно возвращать True или False.

def some_random(my_list):
    import random
    a = random.choices(my_list)
    return(a)

my_list = ['true', 'false']
print(some_random(my_list))

#3. Создайте функцию, которой на вход передается любой тип данных. Если это строковая переменная - выведите 1, если список - выведите 2, во всех остальных случаях - 3.

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


#4. Создайте функцию, которой на вход передается список. Пройдитесь по списку и печатайте элементы до тех пор, пока не встретите "5". Пример списка lst = ['1','2','5','9','8'] Пример вывода: 1 2.
def some_func(my_list):
    for element in my_list:
        if element == '5':
            continue
        print(element)


my_list = ['1','2','5','9','8']
some_func(my_list)



#5 
''' 1. Write a simple python function with one of the editors (IDLE, Notepad++, PyCharm)
•	Check the 6_mts_detail.txt file
•	Split all file data to header and call log
•	Create function with one argument
•	Argument – it’s service type
•	Function need to return lines with argument service type only'''

with open("6_mts_detail.txt", "r") as f:
    read_file = f.readlines()
data = []
for index, i in enumerate(read_file):
    if index > 7:
        data.append(i.split('\t'))


def filter_by_service(type):
    out = []
    for line in data:
        if line[1] == type:
            out.append(' '.join(line))
    return out


print('\n'.join(filter_by_service('SMS<--')))

#6. Создать функцию с одним аргументом, которая проверяет, является ли переданное в аргумент значение изменяемым (mutable) или неизменяемым (immutable) типом данных. Вывод на экран должен выглядеть как: "Value is: (1, 2, 3). It is tuple. Tuple is immutable.

def type_of_arg(arg):
    a = type(arg)
    if a == set or a == list or a == dict:
        print('Value is:', arg, 'It is', a, '. Tuple is mutable.')
    else:
        print('Value is:', arg, '. It is', a,'. Tuple is immutable.')
    return arg
arg = (1,2,3)
print(type_of_arg(arg))