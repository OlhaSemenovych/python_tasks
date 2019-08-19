#1
'''Возьмите первую задачу с предыдущего занятия.
a- создайте методы plus и minus для увеличения и уменьшения количества материалов
b- создайте объект для белого кирпича с 300 в качестве начального количества'''

'''
Условие задачи с предыдущего занятия
Напишите объектно-ориентированную программу, которая показыват
строй материалы и их количество
1. Определите класс Building
2. Создайте конструктор с аттрибутами: material, color, number
(дефолтное значение - 0)
material будет хранить название материала
color - цвет
number - количество
number <= 0  - напечатать "out of stock"
0 < number < 100 - "warehouse"
иначе - "Remote warehouse'''



#a
class Building:
    def __init__(self, material, color, number):
        self.material = material
        self.color = color
        self.number = number

    def calc(self):
        if self.number <= 0:
            print("out of stock")
        elif 0 < self.number < 100:
            print("warehouse")
        else:
            print("Remote warehouse")

    def plus(self, num):
        self.number += num

    def minus(self, num):
        self.number -= num


b = Building('brick', 'red', 0)
white = Building('brick', 'white', 300)
board = Building('board', 'brown', 20)
print(white.number, board.number)
white.plus(50)
board.minus(3)
print(white.number, board.number)

#b
class Building:
    def __init__(self, material, color, number):
        self.material = material
        self.color = color
        self.number = number

    def calc(self):
        if self.number <= 0:
            print("out of stock")
        elif 0 < self.number < 100:
            print("warehouse")
        else:
            print("Remote warehouse")

    def plus(self, num):
        self.number += num

    def minus(self, num):
        self.number -= num


b = Building('brick', 'red', 0)
white = Building('brick', 'white', 300)
board = Building('board', 'brown', 20)
print(white.number, board.number)
white.plus(50)
board.minus(3)
print(white.number, board.number)