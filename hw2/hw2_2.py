# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


some_list = list(input('Введите символы: '))

ind = 0

for i in range(len(some_list) // 2):
    some_list[ind], some_list[ind + 1] = some_list[ind + 1], some_list[ind]
    ind += 2

print(some_list)
