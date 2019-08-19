#1.
"""
1. На вход подается несколько списков разного вида, например:
a = ['--opt3', '2', '--files', '*.c', '*.java', '--opt1', 'True']
b = ['--opt3', '2', '--opt1=True', '--files', '*.c', '*.java']
c = ['--opt1', 'False', '--opt3', '2', '--files', '*.c', '*.java']
d = ['--opt1=False', '--opt3', '2', '--files', '*.c', '*.java']
e = d = ['--opt3', '2', '--files', '*.c', '*.java']
В каждом запуске программы учавствует только один из списков.
Если opt1 не задан, по умолчанию он считается False.
Если opt1 True: Напечатать <p>opt1 is True!</p>
Если opt1 False: Напечатать <p>opt1 is False</p>"""

a = ['--opt3', '2', '--files', '*.c', '*.java', '--opt1', 'True']
b = ['--opt3', '2', '--opt1=True', '--files', '*.c', '*.java']
c = ['--opt1', 'False', '--opt3', '2', '--files', '*.c', '*.java']
d = ['--opt1=False', '--opt3', '2', '--files', '*.c', '*.java']
e = d = ['--opt3', '2', '--files', '*.c', '*.java']

a = ['--opt1=False', '--opt3', '2', '--files', '*.c', '*.java']

if '--opt1=True' in a:
    print('<p>opt1 is True!</p>')
elif '--opt1' in a and a[a.index('--opt1') + 1] == 'True':
    print('<p>opt1 is True!</p>')
else:
    print('<p>opt1 is False!</p>')
    
    
    
def function_to_decorate(func):
    def wrapper():
        print('<p>')
        func()
        print('</p>')
    return wrapper

@function_to_decorate
def opt_function():
    a = ['--opt1=False', '--opt3', '2', '--files', '*.c', '*.java']
    if '--opt1=True' in a:
        print('opt1 is True!')
    elif '--opt1' in a and a[a.index('--opt1') + 1] == 'True':
        print('opt1 is True!')
    else:
        print('opt1 is False!')

opt_function()


#2.Используя property напишите ООП программу: создайте класс Celsius в аттрибутом temperature, создайте функции для добавления температуры и взтия (getter и setter), напишите функцию, которая будет переводить цельсий в фаренгейт


class Celsius:
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    #@temperature.getter
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, num):
        sign = num[-1]
        num = int(num[0:-1])
        if sign == 'C' or sign == 'c':
            num = round(num * (9 / 5) + 32)
            print(str(num) + 'F')
        elif sign == 'F' or sign == 'f':
            num = round((num - 32) * (5 / 9))
            print(str(num) + 'C')
            self._temperature = num


t = Celsius('')
t.temperature = '19C'



#3. Декоратор, выводящий время, которое заняло выполнение функции которая создает tuple и на каждой итерации добавляет в него рандомный элемент от 1 до 100, и так 1000000 раз.

import random
import time


def time_of_func(func):
    def wrapper():
        start_time = time.time()
        func()
        print("--- %s seconds ---" % (time.time() - start_time))
    return wrapper


@time_of_func
def random_numbers():
    some_list = []
    for i in range(1000000):
        some_list.append(random.randint(1, 100))


random_numbers()