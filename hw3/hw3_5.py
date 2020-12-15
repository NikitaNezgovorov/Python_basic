# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
ex = 'q'


def str_to_list(a):
    str_a = a.split(' ')
    int_a = [int(x) for x in str_a]
    return int_a


print('Введите строку чисел, разделенных пробелом.')
result = 0
while True:
    a = input('>>>')
    if ex in a:
        new_list = a[:-2]
        new_result = str_to_list(new_list)
        result += sum(new_result)
        break
    else:
        new_result = str_to_list(a)
        result += sum(new_result)
        print(result)
print(result)





# def sum_numbers(func, array):
#         new_result
#         yield  sum(array) +
