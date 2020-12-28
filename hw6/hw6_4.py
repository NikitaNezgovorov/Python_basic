"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево)
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
 который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
 При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

"""


class Car:
    def __init__(self, color, name, is_police):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Поехали')

    def stop(self):
        print('СТОП')

    def turn(self, direction):
        if direction in ('право', 'лево'):
            print(f'Поворот на {direction}')
        else:
            raise ValueError('Можно только на лево или право')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):

    def __init__(self, color, name):
        super().__init__(color, name, False)

    def show_speed(self):
        if self.speed >= 60:
            print('Превышение скорости')
        super().show_speed()


class SportCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)


class WorkCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)

    def show_speed(self):
        if self.speed >= 60:
            print('Превышение скорости')
        super().show_speed()


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, True)
