"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def neg_pow(x, y):
    return x ** y


print(neg_pow(2, -3))


def neg_pow2(x, y):
    count = 0
    result = 1
    while count < -y:
        result = result * x
        count += 1
    result = 1 / result
    return result


print(neg_pow2(2, -3))