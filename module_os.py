#1. Посчитать количество разных форматов файлов в директории (.py, .txt, .exe etc)

import os

files = os.listdir()
a = iter(files)
i = 0
for item in a:
    if '.py' in item:
        i += 1
    if item is os.path.isdir:
        os.chdir('C:')  #you must specify the directory used to count the files
        if '.py' in item:
            i += 1
print(i)


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
'''Напишите zip.py программу, которая будет создавать зип файл. Программа будет принимать на вход:
1 аргумент - название zip архива
следующие аргументы - файлы, которые будут в этом архиве'''

import zipfile
import os

with zipfile.ZipFile('p.zip', 'w') as zipf:

    directory = os.listdir()
    for item in directory:
        if '.txt' in item:
            zipf.write(item)