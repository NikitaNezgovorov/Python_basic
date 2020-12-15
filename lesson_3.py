"""

Необходимо напечатать на экране YES, NO
если число имеет 3 цифры
"""


def is_some(number: int, count: int) -> bool:
    """ Функуия возвращает является ли число n разрядным
    :param number: int: Число
    :param count: int: Количество цифр в числе
    :return: bool
    """
    return 1 <= (number // 10 ** (count - 1)) < 10

#
#
#
#
# a = {
#     'count': 5,
#     'number': 23456,
# }
#
# b = [23456, 5]
#
# print(is_some(*b))

def my_map(funk, iter_obj):
     for item in iter_obj:
        yield funk(item)


a = my_map(str, [1, 2, 3, 4, 5])

print(type(a))

a = 1
b = 10
c = []

for n in range(a,b+1):
    c.append(n**2)
print(c)

d = [n**2 for n in range(a, b+1)]

print(d)

nums_a = [1, 2, 3, 4, 5]

nums_b = [100, 200, 300, 400, 500]

# result = {1:1 ** 2}

nums_result = {n: n ** 2 for n in nums_a if not n & 1}
print(nums_result)
# n & 1  - побитовые операции.
# numbs_combination = [(n_a, n_b) for n_a in nums_a for n_b in nums_b]
# print(numbs_combination)
#
# result = []
# for n_a in nums_a:
#     for n_b in nums_b:
#         result.append((n_a, n_b))
# print(result)
"""
zip
map
reduce
filter
enumerate
range
sum
min
max
len
"""
a = [1, 2, 3, 4, 5]

# b = print(my_map(str, a))

def my_sum(*args, **kwargs):
    print('kwargs', kwargs)
    print(args)
    result = 0
    for n in args:
        result += n
    return result

# print(my_sum(1, 2, 3, 4, 5, 6, 7,factor=10))

