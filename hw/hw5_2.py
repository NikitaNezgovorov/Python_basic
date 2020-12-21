"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

import os

file_name = 'hw5_2.txt'
file_path = os.path.join(os.path.dirname(__file__), file_name)
line = 0

with open(file_path, 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    print(f'Количество строк в файле {file_name}: {len(lines)}')
    for word in lines:
        words_in_line = lines[line].split()
        print(f'Количество слов в строке {line + 1}: {len(words_in_line)}')
        line += 1
