# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def data(name, surname, birth_year, city, email, phone):
    """ Функция выводит строку данные о пользователе
    :param name: str
    :param surname: str
    :param birth_year: int
    :param city: str
    :param email: str
    :param phone: int
    :return: str
    """
    return (f'Имя: {name} Фамилия {surname} год рождения: {birth_year} город проживания: {city} e-mail:{email} '
            f'Телефон {phone}')


print(data('Никита', 'Незговоров', 1990, 'SPB', 'N@gmail.com', 7321))