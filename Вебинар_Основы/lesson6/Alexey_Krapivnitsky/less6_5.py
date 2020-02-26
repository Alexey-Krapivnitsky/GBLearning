class Stationery:

    def __init__(self, name):
        self.title = name

    @staticmethod
    def draw():
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self, name):
        super().__init__(name)

    def draw(self):
        print(f'Запуск отрисовки, инструмент - {self.title}')


class Pencil(Stationery):

    def __init__(self, name):
        super().__init__(name)

    def draw(self):
        print(f'Запуск отрисовки, инструмент - {self.title}')


class Handle(Stationery):

    def __init__(self, name):
        super().__init__(name)

    def draw(self):
        print(f'Запуск отрисовки, инструмент - {self.title}')


if __name__ == '__main__':

    my_tool = Stationery('что-то эдакое')
    my_pen = Pen('ручка')
    my_pencil = Pencil('карандаш')
    my_handle = Handle('маркер')

    print(my_tool.title)
    my_tool.draw()

    my_pen.draw()
    my_pencil.draw()
    my_handle.draw()
