import random
class Car:
    __population = []

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
        # self.vin = vin
        self.__population.append(self)

    def get_population(self):
        return tuple(self.__population)

class CarFactory:
    def __init__(self, brand, colors, name):
        self.brand = brand
        self.colors = colors
        self.name = name

    def create_car(self, count):

        return [Car(random.choice(self.colors), self.brand) for _ in range(count)]

car1 = Car('White', 'Ford')
car2 = Car('Black', 'Tesla')

factory = CarFactory('Ford', ['White', 'Red', 'Blue'], 'FordFactory')

cars = factory.create_car(10)

print(1)
factory.colors.append('Black')

cars2 = factory.create_car(10)