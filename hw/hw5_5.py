"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import os

file_name = 'hw5_5.txt'
file_path = os.path.join(os.path.dirname(__file__), file_name)
array = "1 2 3 4 6 7 8 8"

with open(file_path, 'w') as file:
    file.write(array)

with open(file_path, 'r') as file:
    numbers = map(int,file.read().split(' '))

print(sum(numbers))

