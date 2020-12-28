from typing import Tuple, List
import random
from copy import copy
from itertools import cycle


class Ui:
    @staticmethod
    def start_game():
        print("Классическая Игра в крестики нолики")

    @staticmethod
    def end_game():
        pass

    @staticmethod
    def hello_user(user: 'User'):
        print(f'{user} c символом {user.symbol} зарегестрирован')

    @staticmethod
    def ask_user():
        while True:
            name = input('Ваше имя в игре? \n>>>')
            if not name:
                print('Необходимо ввести имя')
                continue
            return name

    @staticmethod
    def game_mod():
        ask_str = "Выберите режим игры:\n " \
                  "1 - против компьютера\n " \
                  "2 - против 'Игрока' "
        while True:
            try:
                answer = int(input(ask_str + '/n>>>'))
                if not 2 >= answer > 0:
                    raise ValueError
                return answer
            except ValueError:
                print('Неверный ввод, введите 1 или 2')


class Game:
    def __init__(self):
        self.__board = Board()
        self.__users = []
        self.game_step = 0

    def start_game(self):
        Ui.start_game()
        self.create_users()
        self.__game_cycle()

    def __game_cycle(self):
        for user in cycle(self.__users):
            self.game_step += 1
            user.step(self.__board)
            game_result = self.__board.check()
            # todo Цикл Игры

    def create_users(self):
        game_mode = Ui.game_mode()
        if game_mode == 1:
            user = (User.create_user('X'), User.create_bot('O'))
        else:
            user = (User.create_user('X'), User.create_user('O'))
        self.__users.extend(user)


class Board:

    def __init__(self):
        self.__board = [[0 for _ in range(3)] for _ in range(3)]
        self.__variants = [(n, m) for n in range(3) for m in range(3)]

    def set_step(self, user: 'User', coord: Tuple[int, int]):
        self.__board[coord[0]][coord[1]] = user
        self.__variants.remove(coord)

    @property
    def free_coord(self):
        return copy(self.__variants)

    def check(self):
        for lines in zip(self, zip(*self)):
            for line in lines:
                if self.check_line(line):
                    return True, line[0]
        if self.check_line([self[n][n] for n in range(0, 3)]):
            return True, self[0][0]
        elif self.check_line([self[n][m] for n, m in zip(range(0, 3), range(2, -1, -1))]):
            return True, self[0][-1]

    def check_line(self, line):
        return isinstance(line[0], User) and line.count(line[0]) == len(line)

    def __getitem__(self, item):
        return self.__board[item]


class User:
    __bot_names = (
        'Wally',
        'R2D2',
        'C3PO'
    )

    def __init__(self, name, symbol, is_bot=True):
        self.name = name
        self.symbol = symbol
        self.is_bot = is_bot

    def __str__(self):
        return f'{"Бот" if self.is_bot else "Игрок"} {self.name}'

    @classmethod
    def create_user(cls, symbol: str):
        user = cls(Ui.ask_user(), symbol, False)
        Ui.hello_user(user)
        return user

    @classmethod
    def create_bot(cls, symbol: str):
        user = cls(random.choice(cls.__bot_names), symbol)
        Ui.hello_user(user)
        return user

    def step(self):
        pass


print(1)
