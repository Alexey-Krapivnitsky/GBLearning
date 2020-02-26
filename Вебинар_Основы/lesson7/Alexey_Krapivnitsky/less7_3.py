class Cell:

    def __init__(self, number=0):
        self.cell_slot_count = number

    def __add__(self, other):
        result = self.cell_slot_count + other.cell_slot_count
        return Cell(result)

    def __sub__(self, other):
        result = self.cell_slot_count - other.cell_slot_count
        return Cell(result) if result > 0 \
            else f'Разность ячеек заданных клеток отрицательна ({result}). Вычитание клеток невозможно'

    def __mul__(self, other):
        result = self.cell_slot_count * other.cell_slot_count
        return Cell(result)

    def __truediv__(self, other):
        try:
            result = int(round(self.cell_slot_count / other.cell_slot_count))
            return Cell(result)
        except ZeroDivisionError:
            print('Отсутствует вторая клетка для деления')

    def __str__(self):
        return f'В клетке {self.cell_slot_count} ячеек'

    def make_order(self, line_count):
        for i in range(1, self.cell_slot_count + 1):
            print('*', end='')
            if i % line_count == 0:
                print()


if __name__ == '__main__':
    cell_1 = Cell(25)
    cell_2 = Cell(10)
    cell_3 = Cell(40)

    cell_4 = cell_1 + cell_2
    print(f'cell_4 = cell_1 + cell_2: {cell_4}')

    cell_5 = cell_2 - cell_1
    print(f'cell_5 = cell_2 - cell_1: {cell_5}')

    cell_6 = cell_3 - cell_2
    print(f'cell_6 = cell_3 - cell_2: {cell_6}')

    cell_7 = cell_2 * cell_3
    print(f'cell_7 = cell_2 * cell_3: {cell_7}')

    cell_8 = cell_3 / cell_1
    print(f'cell_8 = cell_3 / cell_1: {cell_8}')

    print(f'cell_4.make_order(11) (Количество ячеек - {cell_4.cell_slot_count}):')
    cell_4.make_order(11)
    print(f'\ncell_1.make_order(6) (Количество ячеек - {cell_1.cell_slot_count}):')
    cell_1.make_order(6)
