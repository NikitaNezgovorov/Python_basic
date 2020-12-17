from sys import argv
from lesson4_1 import is_queen_gambit as isqg

if len(argv) != 7:
    print('Ошибка ввода параметров')
    exit()

params = {}

variables = []
name = ''
for param in argv[1:]:
    try:
        param = int(param)
        variables.append(param)
    except ValueError:
        name = param
        variables = []
    if len(variables) == 2:
        params[name] = variables

ask = ('NO', 'YES')

print(ask[isqg(**params)])
