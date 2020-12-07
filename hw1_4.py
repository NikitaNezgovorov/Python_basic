# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = input('Введите целое пложительное число:\n >>> ')

while not number.isdigit():
    number = input('Введите целое пложительное число:\n >>> ')

digit_count = 0
max_number = 0

while len(number) > digit_count:
    new_number = int(number[digit_count])
    if new_number > max_number:
        max_number = new_number
    digit_count += 1

print(f'Самая большая цифра числа {number} - "{max_number}"')
