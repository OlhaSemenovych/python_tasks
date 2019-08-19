        
#1.
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
    time.sleep(0.1)
    sys.stdout.write("\r  \r\n")
    start = time.perf_counter()
    if start == 30:
        print("Time is over")
except KeyboardInterrupt:
    print(s)
    
    
#2.
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
