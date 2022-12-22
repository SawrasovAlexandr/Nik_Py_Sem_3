# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

numbers = [round(random.uniform(0, 10), 2) for _ in range(11)]
print(numbers)
decim = [round(i - int(i), 2) for i in numbers]
min = max = decim[0]
for i in decim:
    if i == 0: continue
    elif i < min: min = i
    elif i > max: max = i
print(min, max)
print('Разность максимальной и минимальной дробных частей равна:', max - min)
