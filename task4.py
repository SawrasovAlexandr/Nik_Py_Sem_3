# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from functions import get_int

num = get_int('Введите число: ')
bin = ''
while num != 0:    
    bin = str(num % 2) + bin
    num //= 2
print('Двоичное представление ввеленного числа:', bin)

