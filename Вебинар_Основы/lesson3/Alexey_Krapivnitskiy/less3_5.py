def sum_inp_list(inp_list):
    """
    This function resive list of string type numbers.
    It then converts the resulting values to digit (int type)
    and returns their amount, as well as the program completion flag
    :param inp_list: list of numbers
    :return:
    """
    if inp_list[-1].upper() == 'N':
        inp_list.pop()
        return sum(list(map(lambda x: int(x), inp_list))), True
    else:
        return sum(list(map(lambda x: int(x), inp_list))), False


result = 0
print('Вводите числа, разделяя их пробелом.\n'
      'Для подсчета суммы нажмите Enter.\n'
      'Для выхода введите "N"\n')

while True:
    numbers = input('Числа: ').split()
    if numbers:
        next_numbers, exit_flag = sum_inp_list(numbers)
        result += next_numbers
        print(f'Сумма всех введенных чисел: {result}')
        if exit_flag:
            break
    else:
        print('Вы ничего не ввели')
