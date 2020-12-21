"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текст файл.
"""
import os

file_name = 'hw5_4.txt'
new_file_name = 'new_hw5_4.txt'

words = {
    'One': 'Первый',
    'Two': 'Второй',
    'Three': 'Третий',
    'Four': 'Четвертый',
}

file_path = os.path.join(os.path.dirname(__file__), file_name)
new_file_path = os.path.join(os.path.dirname(__file__), new_file_name)

with open(file_path, 'r', encoding='UTF-8') as file:
    for line in file:
        english_line = line.split()
        russian_line = line.replace(english_line[0], words.get(english_line[0]))
        with open(new_file_path, 'a', encoding='UTF-8') as new_file:
            new_file.write(russian_line)
