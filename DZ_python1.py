# Вычислить число Пи c заданной точностью d
import math
d = input('Задайте точность числа пи: ')
d1 = len(d) - 2
a = round(math.pi, d1)
print(a)