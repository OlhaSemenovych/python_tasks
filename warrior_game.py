#1.
'''Напишите программу по следующему описанию.
Есть класс Воин с аттрибутами
- имя
- здоровье 100,
и два экземпляра этого класса.
Воины атакуют друг друга по очереди: при каждом ударе
тот кого атакуют теряет здоровье, сила атаки - рандомное число в диапазоне 0-10.
Если это число 0 - атакующий теряет 5 очков.
Когда у кого-то заканчивается здоровье, программа должна вывести имя победителя.
После каждого удара выводится сообщение:
==========================
Бой № ...
nameX атакует, nameX/Y теряет ... очков
-------------
name1 health: ...
name2 health: ...
=========================='''

import random


class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, warrior):
        force_of_attack = random.randint(0, 10)
        print('%s ' % self.name)
        if force_of_attack == 0:
            self.health -= 5
            print('%s  5 ' % self.name)
        else:
            warrior.health -= force_of_attack
            print('%s  %d ' % (warrior.name, force_of_attack))
        print('-----------------')


class Fight:
    def __init__(self, first_warrior, second_warrior):
        self.first_warrior = first_warrior
        self.second_warrior = second_warrior

    def war(self):
        counter = 1
        while self.first_warrior.health > 0 and self.second_warrior.health > 0:
            print('====================')
            print(' ', counter)
            self.first_warrior.attack(self.second_warrior)
            if self.second_warrior.health <= 0:
                print('%s ' % self.first_warrior.name)
                break
                self.second_warrior.attack(self.first_warrior)
            if self.first_warrior.health <= 0:
                print('%s ' % self.second_warrior.name)
                break
            print(' %s %d ' % (self.first_warrior.name, self.first_warrior.health))
            print(' %s %d ' % (self.second_warrior.name, self.second_warrior.health))
            print('====================')
            counter += 1


first_warrior = Warrior('Subzero')
second_warrior = Warrior('Scorpio')
fight = Fight(first_warrior, second_warrior)
fight.war()


#2.
'''Напишите программу по следующему описанию.
Есть класс Воин с аттрибутами
- имя
- здоровье 100,
и два экземпляра этого класса.
Воины атакуют друг друга по очереди: при каждом ударе
тот кого атакуют теряет здоровье, сила атаки - рандомное число в диапазоне 0-10.
Если это число 0 - атакующий теряет 5 очков.
Когда у кого-то заканчивается здоровье, программа должна вывести имя победителя.
После каждого удара выводится сообщение:
==========================
Бой № ...
nameX атакует, nameX/Y теряет ... очков
-------------
name1 health: ...
name2 health: ...
========================== '''

import random


class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, warrior):
        force_of_attack = random.randint(0, 10)
        print('%s атакует' % self.name)
        if force_of_attack == 0:
            self.health -= 5
            print('%s теряет 5 очков' % self.name)
        else:
            warrior.health -= force_of_attack
            print('%s теряет %d очков' % (warrior.name, force_of_attack))
        print('-----------------')


class Fight:
    def __init__(self, first_warrior, second_warrior):
        self.first_warrior = first_warrior
        self.second_warrior = second_warrior

    def war(self):
        counter = 1
        while self.first_warrior.health > 0 and self.second_warrior.health > 0:
            print('====================')
            print('Бой №', counter)
            self.first_warrior.attack(self.second_warrior)
            if self.second_warrior.health <= 0:
                print('%s побеждает' % self.first_warrior.name)
                break
                self.second_warrior.attack(self.first_warrior)
            if self.first_warrior.health <= 0:
                print('%s побеждает' % self.second_warrior.name)
                break
            print('У %s %d здоровья' % (self.first_warrior.name, self.first_warrior.health))
            print('У %s %d здоровья' % (self.second_warrior.name, self.second_warrior.health))
            print('====================')
            counter += 1


first_warrior = Warrior('Subzero')
second_warrior = Warrior('Scorpio')
fight = Fight(first_warrior, second_warrior)
fight.war()

