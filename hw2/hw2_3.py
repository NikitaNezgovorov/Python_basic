# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
print('*' * 20)
print('Решение через list')

while True:
    month = input('Введите номер месяца: ')
    if month.isdigit():
        month = int(month)
        if month in range(1, 13):
            break
        else:
            print('Ошибка. Число должно быть от 1 до 12')
    else:
        print('Ошибка. Введите число')

calender = [['Зима', [12, 1, 2]], ['Весна', [3, 4, 5]], ['Лето', [6, 7, 8]], ['Осень', [9, 10, 11]]]

season = 0
for i in calender:
    if month in calender[season][1]:
        print(calender[season][0])
    season += 1

# Решение через Dict

print('*' * 20)
print('Решение через dict')
while True:
    month = input('Введите номер месяца: ')
    if month.isdigit():
        month = int(month)
        if month in range(1, 13):
            break
        else:
            print('Ошибка. Число должно быть от 1 до 12')
    else:
        print('Ошибка. Введите число')


calender = {
    'Зима': [12, 1, 2],
    'Весна': [3, 4, 5],
    'Лето': [6, 7, 8],
    'Осень': [9, 10, 11]
}
for i in calender:
    if month in calender.get(i):
        print(i)
