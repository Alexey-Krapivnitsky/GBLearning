def my_func(a, b, c):
    """
    This function returns the sum of the largest two arguments
    :param a: int
    :param b: int
    :param c: int
    :return: a+c or a+b or b+c
    """
    num_as_list = sorted([a, b, c])
    return sum(num_as_list[1:])


result = my_func(15, 28, -31)
print(result)
