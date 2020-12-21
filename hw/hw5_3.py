"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

import os

file_name = 'hw5_3.txt'
file_path = os.path.join(os.path.dirname(__file__), file_name)
count = 0
pay_roll_sum = 0
high_rate = []
with open(file_path, 'r', encoding='UTF-8') as file:
    personal_list = file.readlines()

for person in personal_list:
    person_list = personal_list[count].split()
    if int(person_list[1]) > 20000:
        high_rate.append(person_list[0])
    pay_roll_sum += int(person_list[1])
    count += 1

print(f'Список сотрудников с окладом более 20000: {" ".join(high_rate)}')
print(f'Количество сотрудников: {count}')
print(f'Средняя величина дохода: {pay_roll_sum/count}')
