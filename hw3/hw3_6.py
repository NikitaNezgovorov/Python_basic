# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_funk(user_word):
    return ''.join((user_word[0].upper(), user_word[1:]))


def text_capitalize(user_string):
    str_list = user_string.split(' ')
    new_list = []
    for new_str in str_list:
        new_list.append(int_funk(new_str))

# или


def text_capitalize2(user_string):
    return ' '.join(map(int_funk, user_string.split(' ')))


print(text_capitalize2('text new hello my You hi'))



