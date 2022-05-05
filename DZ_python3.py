# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
    
# import random
print ('Исходная последовательность чисел')
numbers = [3, 5, 3, 8, 8, 2, 5]
new_numbers = []
print (numbers)
k = 0
# while k <= numbers[len(numbers)-1]:
# new_numbers.append(numbers[k])
while k != len(numbers):
    for i in range(len(numbers)):
        if numbers[k] == numbers[i]:
            # numbers.pop(i)
            new_numbers.append(numbers[i])
            # break
            # print (k)
            # print (i)
            # print (new_numbers)
    
    k += 1
print ('Последовательность неповторяющихся элементов')
print (numbers)