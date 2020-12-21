"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

import os

file_name = 'hw5_1.txt'
file_path = os.path.join(os.path.dirname(__file__), file_name)

with open(file_path, 'a', encoding='UTF-8') as file:
    while True:
        text = input('Введите текст: ')
        file.writelines(text + '\n')
        if not text:
            break

