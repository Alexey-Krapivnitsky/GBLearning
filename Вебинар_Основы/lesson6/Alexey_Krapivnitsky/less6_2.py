from functools import reduce


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_resulting(self, weight, thickness):
        road_parameters = [self._length, self._width, weight, thickness]
        my_check = list(filter(lambda x: type(x) == str and not x.isdigit(), road_parameters))
        if my_check:
            print('One or more of the entered values is not a number')
        else:
            asphalt_mass = reduce(lambda res, el: res * el,
                                  list(map(float, road_parameters)), 1)
            result = round(asphalt_mass, 3) / 1000
            return result


if __name__ == '__main__':
    new_road = Road(5000, 20)
    my_asphalt_mass = new_road.get_resulting('25', 5)
    if my_asphalt_mass:
        print(f'The required weight of asphalt - {my_asphalt_mass} tons')
