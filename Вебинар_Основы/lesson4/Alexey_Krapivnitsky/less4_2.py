def resulting(inp_list):
    result_gen = (el for el in inp_list)
    result = [el for el in inp_list[1:] if el > next(result_gen)]
    return result


if __name__ == '__main__':
    print(resulting([5, 15, 0, 1, 2, 8, 3, 12, 55, 16, 22]))
