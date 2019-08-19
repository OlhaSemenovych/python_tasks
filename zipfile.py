#1. Напишите zip.py программу, которая будет создавать зип файл. Программа будет принимать на вход: 1 аргумент - название zip архива, следующие аргументы - файлы, которые будут в этом архиве.

import zipfile
import os

with zipfile.ZipFile('p.zip', 'w') as zipf:

    g = os.listdir()
    for a in g:
        if '.txt' in a:
            zipf.write(a)