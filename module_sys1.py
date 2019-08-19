#1.
'''3. Создать ползунок загрузки а ля
->10
-->20
------------>100
Использвать sys stdout'''

import sys
import time

for i in range(1,101):
  if i % 10 == 0:
    print('-' * (i // 10) + '>' + str(i))
  time.sleep(0.1)
  

#2.
'''1. Написать программу, которая при запуске из терминала, если введен аргумент replace
будет заменять имена файлов в указанной папке. Если введен аргумент copy - создает копию файла (дописывает в конце (1)).
Например, у вас есть 10 фото в формате IMG00...IMG09,
если replace: нужно заменить на дату, когда фото было сделано
(https://pypi.org/project/ExifRead/ or PIL)
если copy: в папке будет 20 файлов IMG00 IMG00(1) и тд.'''

import os
import sys
import exifread
import shutil

if len(sys.argv) != 3:
    print('Error: please pass exactly two arguments')
    exit(1)
if sys.argv[1] != 'replace' and sys.argv[1] != 'copy':
    print("Error: argument 1 must be 'copy' or 'replace'")
    exit(2)
if not os.path.isdir(sys.argv[2]):
    print("Error: argument 2 must be directory path")
    exit(3)

if sys.argv[1] == 'replace':
    for old_file_name in os.listdir(sys.argv[2]):
        old_file_path = sys.argv[2] + '\\' + old_file_name
        items = old_file_name.split('.')
        files = open(old_file_path, 'rb')
        tags = exifread.process_file(files)
        datetime_image = tags['Image DateTime']
        new_file_name = sys.argv[2] + '\\' + str(datetime_image).replace(':', '_') + '.jpg'
        shutil.copy(old_file_path, new_file_name)

if sys.argv[1] == 'copy':
    for old_file_name in os.listdir(sys.argv[2]):
        old_file_path = sys.argv[2] + '\\' + old_file_name
        items = old_file_name.split('.')
        new_file_name = sys.argv[2] + '\\' + '.'.join(items[:-1]) + '(1)' + '.jpg'
        shutil.copy(old_file_path, new_file_name)
        
        
#3.
'''Напишите программу, которая будет считать 1+2+3+... пока
не произойдет одну из двух вещей:
- пройдет 30 секунд и программа не вывалится с сообщением, что прошло
слишком много времени
- вы вызываете KeyboardInterrupt и программа печатает, число, которое она успела посчитать'''

import sys
import time

try:
    a = 0
    s = 0
    while a < 101:
        s += a
        a = a+1
        print(a, end='+')
    sys.stdout.write("%d\r" % a)
    sys.stdout.flush()
    time.sleep(40)
    sys.stdout.write("\r  \r\n")
    start = time.perf_counter()
    if start == 30:
        print("Time is over")
except KeyboardInterrupt:
    print(s)