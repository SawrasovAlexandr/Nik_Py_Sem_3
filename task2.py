# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from functions import get_random_list

numbers = get_random_list(1, 11, 11)
print('Исходный список:', numbers)
length = len(numbers) // 2 + len(numbers) % 2
prods = [(numbers[i-1] * numbers[-1 * i]) for i in range(1, length + 1)]
print('Произведения пар чисел:', prods)