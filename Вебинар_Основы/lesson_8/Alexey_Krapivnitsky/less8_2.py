class ZeroError(Exception):
    pass


class CheckZero:

    def __init__(self, x, y):
        self.result = 0
        self.x = x
        self.y = y
        self.check_div()

    def __str__(self):
        return f'{self.result}' if self.result else '0'

    def check_div(self):
        try:
            self.result = self.x / self.y
        except ZeroDivisionError:
            raise ZeroError('На ноль делить нельзя')
        else:
            return self.result


if __name__ == '__main__':
    # dividend = float(input('Введите делимое: '))
    # divisor = float(input('Введите делитель: '))
    dividend = 5
    divisor = 0

    try:
        print(CheckZero(dividend, divisor))
    except ZeroError as e:
        print(f'Ошибка деления - {e}')
