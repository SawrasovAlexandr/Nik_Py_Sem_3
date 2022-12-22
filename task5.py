# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

from functions import get_int

def fibo(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fibo(number - 1) + fibo(number - 2)

def nega(number):
    if number == -1:
        return 1
    if number == -2:
        return -1
    return nega(number + 2) - nega(number + 1)

num = get_int('Введите число:')
negafi = [nega(i) for i in range(-1 * num, 0)]
bonaci = [fibo(i) for i in range(num + 1)]
negafibonaci = negafi + bonaci
print(negafibonaci)