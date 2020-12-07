# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_input_time = input('Введите время в секундах:\n >>> ')

while not user_input_time.isdigit():
    user_input_time = input('Введите целое число:\n >>> ')

user_input_time = int(user_input_time)

hour = user_input_time // 3600
minute = user_input_time % 3600 // 60
second = user_input_time - (hour * 3600) - (minute * 60)

time = f'{hour}:{minute}:{second}'

print(time)
