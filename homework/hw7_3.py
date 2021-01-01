"""
Реализовать программу работы с органическими клетками.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(),
принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида **\n\n***..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: **\n\n.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: **\n\n***.
"""


class Cell:
    def __init__(self, cell_count):
        self.__cell_count = cell_count

    @property
    def cell_count(self):
        return self.__cell_count

    def __add__(self, other):

        return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):

        new_cell = self.cell_count - other.cell_count
        if new_cell > 0:
            return Cell(new_cell)
        raise ValueError('The difference is less than or equal to zero')

    def __truediv__(self, other):

        return self.__floordiv__(other)

    def __mul__(self, other):

        return Cell(self.cell_count * other.cell_count)

    def __floordiv__(self, other):
        return Cell(self.cell_count // other.cell_count)

    def make_order(self, cells_in_lines: int):
        if not isinstance(cells_in_lines, int):
            raise TypeError('cells_in_lines int type only')
        temp = self.cell_count // cells_in_lines
        temp2 = self.cell_count % cells_in_lines
        result = '\n'.join(['*' * cells_in_lines + '*' * temp2 if idx + 1 == temp and temp2
                            else '*' * cells_in_lines
                            for idx in range(temp)]
                           )
        return result


if __name__ == '__main__':
    c1 = Cell(13)
    c2 = Cell(2)
    c1.make_order(2)
    print(1)