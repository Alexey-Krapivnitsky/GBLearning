import time


class TrafficLight:
    __color = []

    def get_color(self):
        return self.__color

    def __set_color(self, colors):
        self.__color = colors

    def running(self, colors):
        self.__set_color(colors)
        if self.__color == ['red', 'yellow', 'green']:
            traffic_timer = dict(zip(self.__color, [7, 2, 10]))
            for key, val in traffic_timer.items():
                for i in range(val):
                    time.sleep(1)
                    print(f'{str(key).upper()} - {i + 1} sec.')
            print('STOP Traffic Light')
        else:
            print('This mode of operation is not provided for traffic lights')


if __name__ == '__main__':
    my_traffic_light = TrafficLight()
    my_colors = ['red', 'yellow', 'green']
    my_traffic_light.running(my_colors)
