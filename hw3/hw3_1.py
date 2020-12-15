# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(dividend, divider):
    """ Функция деления одного числа на другое
    :param dividend: int: Делимое
    :param divider: int: Делитель
    :return: float
    """
    try:
        return dividend / divider
    except ZeroDivisionError:
        print('Делить на ноль пока нельзя!')


def is_digit(num):
    if num.isdigit():
        return True
    else:
        try:
            float(num)
            return True
        except ValueError:
            return False


while True:
    num1 = input('Введите делимое: ')
    num2 = input('Введите делитель: ')
    if is_digit(num1) and is_digit(num2):
        num1 = float(num1)
        num2 = float(num2)
        break
    else:
        print('Вы ввели не число')

print(division(num1, num2))
