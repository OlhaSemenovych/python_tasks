#1
'''Создать скрипт, который с помощью аргпарсера будет принимать ссылку,
название файла для сохранения, параметр --to-file, который в случае наличия его в строке
записывает в файл log.txt лог выполнения, иначе - пишет лог в консоль.
Ссылка и файл для сохранения - обязательные параметры (если они не переданы,
должен выводиться help и сообщение, что чего-то не хватает). Если все хорошо -
в файл записываетя контент страницы, которую нужно скачать по ссылке.'''

import argparse
import requests
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--link', required=True, help="Something don't write!")
parser.add_argument('--name', help='an integer for the accumulator')
parser.add_argument('--to_file', required=True, action = 'store_true', help="Something don't write!")
args = parser.parse_args()

if args.to_file:
    ff = open('1.txt', 'r')
else:
    ff = sys.stdout()

    print('downloading', ff == file)

r = requests.get('args.link')
print(r.text)
with open('args.name', 'w') as f:
    f.write(r.text)

ff.close()

#2. http://httpbin.org/ - A simple HTTP Request & Response Service. Отправьте несколько запросов post, get.

import requests

r = requests.get('http://httpbin.org/')
print(r.text)