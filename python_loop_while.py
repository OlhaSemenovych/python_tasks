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

#2. Выведите на экран элементы словаря с помощью цийла while и блока try/except:

some_dict = {'dict': 1, 'dictionary': 2}
a = iter(some_dict.items())
while True:
    try:
        print(next(a))
    except StopIteration:
        break