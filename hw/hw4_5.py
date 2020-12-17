"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce


def even_numbers(number, next_number):
    return number * next_number


result = reduce(even_numbers, [el for el in range(100, 1001) if el % 2 == 0])

print(result)
