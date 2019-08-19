#1.
'''Напишите программу для фильтрации входного значения:
• Создайте переменную через ввод с клавиатуры
• Создайте блок try, чтобы проверить, что var/15
• Создать инструцкию Except для обработки исключения
• Создайте вложенный в блок исключения try, проверьте
является ли int(var)/15 - числом.
• Для этого блока, создайте исключение для обработки TypeError и ValueError,
напечатайте, что введенные данные являются стрингой
• Создать команду else для верхнего блока try, напечатайте там что-то
• Создайте окончательную инструкцию, напечатайте, что программа отработала
• Запустить код с различными типами ввода данных
'''

input_number = input('Please enter some number:')
try:
    result = input_number / 15
except TypeError:
    print("Keyboard entry is not a number")
    try:
        some_num = int(input_number)/15
    except(TypeError, ValueError):
        print("Data entered is a string")

else:
    print('Text must be printed')
finally:
    print('Process finished')


#2.
'''Создайте программу, которая принимает на вход два числа, и делит их.
В случае, если второе - 0, вывести сообщение, что на ноль делить нельзя.'''

num_1 = int(input('Please enter first number:'))
num_2 = int(input('Please enter second number:'))
try:
    a = num_1 / num_2
    print(a)
except ZeroDivisionError:
    print("It is impossible to divide by zero")
    
    
#3.
''''Напишите программу для фильтрации входного значения:
• Создайте переменную через ввод с клавиатуры
• Создайте блок try, чтобы проверить, что var/15
• Создать инструцкию Except для обработки исключения
• Создайте вложенный в блок исключения try, проверьте
является ли int(var)/15 - числом.
• Для этого блока, создайте исключение для обработки TypeError и ValueError,
напечатайте, что введенные данные являются стрингой
• Создать команду else для верхнего блока try, напечатайте там что-то
• Создайте окончательную инструкцию, напечатайте, что программа отработала
• Запустить код с различными типами ввода данных/'''

input_number = input('Please enter some number:')
try:
    result = input_number / 15
except TypeError:
    print("Keyboard entry is not a number")
    try:
        some_num = int(input_number)/15
    except(TypeError, ValueError):
        print("Data entered is a string")

else:
    print('Text must be printed')
finally:
    print('Process finished')
    

#4. Создайте программу, которая принимает на вход два числа, и делит их. В случае, если второе - 0, вывести сообщение, что на ноль делить нельзя.

a = 1
b = 0

num_1 = int(a)
num_2 = int(b)
try:
    c = num_1 / num_2
    print(c)
except ZeroDivisionError:
    print("It is impossible to divide by zero")

a = 1
b = 0


#5. Выведите на экран элементы словаря с помощью цийла while и блока try/except:

some_dict = {'dict': 1, 'dictionary': 2}
a = iter(some_dict.items())
while True:
    try:
        print(next(a))
    except StopIteration:
        break