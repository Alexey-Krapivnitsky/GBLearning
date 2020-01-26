import math

my_list = [1, 4, 9, -4, 25, -6, -7, 64, 81, 100, -11, 144, 169, 196, -15]


def sqrt_func(inp_list):
    inp_list = inp_list.copy()
    result_list = [number if number < 0 else math.sqrt(number) for number in inp_list]
    return result_list


print(my_list)
print(sqrt_func(my_list))
print(my_list)
