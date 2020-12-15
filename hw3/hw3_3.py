# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    """
    :param a: int
    :param b: int
    :param c: int
    :return: int
    """
    numbers = (a, b, c)
    return sum(numbers) - min(numbers)


print(my_func(9, 5, 6))

my_func2 = lambda a, b, c: max(a + b, a + c, b + c)\

print(my_func2(9, 5, 5))