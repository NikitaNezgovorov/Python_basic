# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_str = input('Введите неслколько слов через пробел: ')

for ind, word in enumerate(user_str.split()):
    print(ind+1, word[:10])
