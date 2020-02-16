from itertools import count, cycle


def infinite(start_val, my_count):
    result = []
    my_gen = (el for el in count(start_val))

    while my_count:
        result.append(next(my_gen))
        my_count -= 1

    return result


def infinite_whit_list(count_val, my_list):
    result = []
    cycle_repeat = len(my_list)

    for num in cycle(my_list):
        if len(result) / cycle_repeat == count_val:
            break
        result.append(num)

    if type(my_list) == str:
        result = ''.join(result)

    return result


if __name__ == '__main__':
    print(*infinite(10, 10))
    print(infinite_whit_list(5, [1, 2, 3, 4, 5]))
    print(infinite_whit_list(5, 'Программа '))
