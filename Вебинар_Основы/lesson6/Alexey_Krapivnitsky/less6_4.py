from random import randint


class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.max_speed = speed
        self.is_police = is_police

    def get_attr(self):
        cop = 'Police' if self.is_police else ''
        car_description = f'{cop}Car "{self.name}", color - {self.color}, maximum speed - {self.max_speed}'
        return car_description

    @staticmethod
    def go():
        print('let`s go')

    @staticmethod
    def stop():
        print('stopped')

    @staticmethod
    def turn(direction):
        print(f'turned {direction}')

    def show_speed(self, speed):
        print(f'The current speed is equal to {speed} kmph')


class TownCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self, speed):
        if speed > 60:
            print(f'The current speed is equal to {speed} kmph\n'
                  f'Overspeed by {speed - 60} kmph')
        else:
            print(f'The current speed is equal to {speed} kmph')


class WorkCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self, speed):
        if speed > 40:
            print(f'The current speed is equal to {speed} kmph\n'
                  f'Overspeed by {speed - 40} kmph')
        else:
            print(f'The current speed is equal to {speed} kmph')


class SportCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self, speed):
        print(f'The current speed is equal to {speed} kmph')


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, is_police=True)

    def show_speed(self, speed):
        print(f'The current speed is equal to {speed} kmph')


if __name__ == '__main__':

    car_1 = TownCar('Chevrolet', 'white', 170)
    car_2 = TownCar('Lada Granta', 'orange', 140)
    car_3 = WorkCar('KAMAZ', 'green', 100)
    car_4 = SportCar('Lamborghini', 'red', 320)
    car_5 = PoliceCar('Ford', 'white', 200)

    for obj in [car_1, car_2, car_3, car_4, car_5]:
        print(obj.get_attr())
        obj.go()
        current_speed = randint(20, 140)
        obj.show_speed(current_speed)
        direct = 'left' if obj in [car_2, car_4] else 'right'
        obj.turn(direct)
        obj.stop()
        print()
