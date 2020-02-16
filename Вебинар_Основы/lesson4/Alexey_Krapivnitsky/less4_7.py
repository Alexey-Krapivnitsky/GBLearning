from itertools import count


def my_gen():
    """
    This function calculates the factorial of each element of an infinite sequence
    :return: number!
    """
    factorial = 1
    for number in count(1):
        factorial *= number
        yield factorial


if __name__ == '__main__':
    n = 1
    for el in my_gen():
        print(f'Факториал {n}: {el}')
        if n == 15:
            break
        n += 1
