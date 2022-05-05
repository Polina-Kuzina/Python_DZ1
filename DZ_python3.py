# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
    
numbers = [3, 5, 3, 8, 8, 2, 5]
print ('Исходная последовательность чисел')
print (numbers)
new_numbers = []
for i in numbers:
    if i not in new_numbers:
        new_numbers.append(i)
print ('Последовательность неповторяющихся элементов')
print (new_numbers)