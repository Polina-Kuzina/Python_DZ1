# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 1 до 100, можно создать свой генератор случайных чисел или использовать готовый) 
# многочлена и записать в файл многочлен степени k.

import random
from random import randint
k = int(input('Задайте степень k: '))
numbers = []
for i in range(k+1):
    numbers.append(randint(1, 100))
print(numbers)
file_numbers = 'numbers4.txt'
with open(file_numbers, 'a') as data:
    for i in range(k-1):
        data.write(f'{numbers[i]}*x^{k-i} + ')
    data.write(f'{numbers[k-1]}*x + {numbers[k]} = 0')    
# print(data)