#1.
'''Create several toy objects with the age category from 1 to 12 years
Print all the existing attributes for the created objects.
Change attributes of the created objects (like color or age_category)

Improved difficulty task:
Create program to automatically sort toys according to the given while object creation.
You give several object name, color, age_category. And with calling a created sort function you return
the toys which fulfill the specified attributes (color, age….)'''

class Age:
    def factory(self, age):
        if 1 <= age <= 3:
            return Baby()
        elif 3 < age <= 5:
            return Toddler()
        elif 5 < age <= 8:
            return Preschool()
        elif 8 < age <= 12:
            return Gradeschooler()


class Baby(Age):
    def category(self):
        print('Category Baby age: 1-3')


class Toddler(Age):
    def category(self):
        print('Category Toddler age: 3-5')


class Preschool(Age):
    def category(self):
        print('Category Preschool age: 5-8')


class Gradeschooler(Age):
    def category(self):
        print('Category Gradeschooler age: 8-12')

t = Age()
a = t.factory(4)
a.category()

#2.
''''Напишите объектно-ориентированную программу, которая показыват строй материалы и их количество
1. Определите класс Building
2. Создайте конструктор с аттрибутами: material, color, number (дефолтное значение - 0)
material будет хранить название материала
color - цвет
number - количество
number <= 0  - напечатать "out of stock" 0 < number < 100 - "warehouse" иначе - "Remote warehouse" '''


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


b = Building('brick', 'red', 0)
print(b.number)
b.calc()



#3.
'''Используя property напишите ООП программу:
создайте класс Celsius в аттрибутом temperature
создайте функции для добавления температуры и взтия (getter и setter)
напишите функцию, которая будет переводить цельсий в фаренгейт'''


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



#4.
'''Создайте класс Человек, который принимает на вход обьект класса Собака.
У класса Собака есть один аттрибут - имя.
у класса человек есть атрибут собака и метод, который дает собаке имя.
Если у человека нет собаки - напечатать, что нет собаки.'''


class Dog:
    def __init__(self):
        self.name = ''


class Human:
    def __init__(self, n, d):
        self.dog_obj = d
        self.name = n
        print(self.dog_obj.name)

    def set_dog_name(self, p):
        self.dog_obj.name = p
        if self.dog_obj.name == '':
            print("This dog does not exist")


dog = Dog()
h = Human('Sasha', dog)
h.set_dog_name('Bob')
print(dog.name)