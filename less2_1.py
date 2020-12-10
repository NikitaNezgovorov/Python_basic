"""
Неизменяемые типы

int
float
bool

None

str
tuple
frozenset
Изменяемые типы
list

dict
set

"""

some = 'asdfgsdgsdgsdfgsdgsdg'

for char in some:
    print(char)

idx = 0
while idx < len(some):
    item = some[idx]
    print(item)
    idx +=1


some_list = [1, 2, 3, 'some string', True, 22.3]

some_dict = {
    'one': 12313,
    'two': 14234234,
    'user_name': 'some_name',
    'user_age': 22,
}

