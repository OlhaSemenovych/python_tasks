#1. Есть база данных и ее бекап. Они хранятся в файлах csv. Записать в бекап новые данные, вывести на экран только измененные поля.

with open('database_4_new.csv', 'r') as file_base:
    base = file_base.readlines()
    file_base.close()
with open('database_4_backup.csv', 'r') as file_backup:
    backup = file_backup.readlines()
    file_backup.close()
output = []
for i in range(len(backup)):
    if base[i] == backup[i]:
        output.append(backup[i])
    else:
        output.append(base[i])
for s in range(i+1, len(base)):
   output.append(base[i])
print(''.join(output))
with open('database_4_backup.csv', 'w') as file_backup:
    file_backup.write(''.join(output))
    file_backup.close()


#2. For file log_4.txt create log_4.html. First, second and last lines should be ignored. HTML should consist of table: Time | Type of msg | Msg. 

with open('log_4', 'r') as f:
    read_file = f.readlines()
lines = []
for line in read_file:
    lines.append(line.split('  '))
table = '<table style="border:2px black solid">'
for row in lines:
    table = table + '<tr>'
    for cel in row:
        table = table + '<td>' + cel + '</td>'
    table = table + '</tr>'

table = table + '</table>'

print(table)


#3. Создать программу, которая во всех .txt файлах текущей папки удалит новые строки.

with open('new_file.txt', 'r') as f:
    my_lines = f.readlines()
    new_list = []
    for a in my_lines:
        new_symbol = a.replace('\n','-')
        new_list.append(new_symbol)
with open('new_file.txt', 'w') as f:
    for i in new_list:
        f.write(i)
        
        
#4.
'''Зажмите ctrl+print. вы видите аргументы, которые принт принимает на вход
def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
Есть переменные:
a = "hello"
b = "world"
Напечатайте:
1. hello, world
2. hello, world запишите в файл'''

a = "hello"
b = "world"
print(a, b, sep=',', end='\n', file=None)

a = "hello"
b = "world"
print(a, b, sep=',', end='\n', file=None)
with open('some.txt', 'w') as f:
    f.write('hello, world')
    f.close()
    
    
#5. 
''' 1. Write a simple python function with one of the editors (IDLE, Notepad++, PyCharm)
•	Check the 6_mts_detail.txt file
•	Split all file data to header and call log
•	Create function with one argument
•	Argument – it’s service type
•	Function need to return lines with argument service type only'''

with open("6_mts_detail.txt", "r") as f:
    read_file = f.readlines()
data = []
for index, i in enumerate(read_file):
    if index > 7:
        data.append(i.split('\t'))


def filter_by_service(type):
    out = []
    for line in data:
        if line[1] == type:
            out.append(' '.join(line))
    return out


print('\n'.join(filter_by_service('SMS<--')))

