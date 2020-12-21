"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import os
import json

file_name = 'hw5_7.txt'
file_path = os.path.join(os.path.dirname(__file__), file_name)
json_file_path = os.path.join(os.path.dirname(__file__), 'hw5_7.json')
profit_result = 0
count = 0
firms = {}
avg_result_dict = {}

with open(file_path, 'r', encoding='UTF-8') as file:
    for firm in file:
        name = firm.split(' ')[0]
        profit = int(firm.split(' ')[2]) - int(firm.split(' ')[3])
        firms[name] = profit
        if profit > 0:
            profit_result += profit
            count += 1
avg_result_dict['average_profit'] = (profit_result / count)

firms_list = [firms, avg_result_dict]

with open(json_file_path, 'w') as write_f:
    json.dump(firms_list, write_f)
