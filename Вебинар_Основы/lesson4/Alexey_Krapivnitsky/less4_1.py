import sys


def input_param():
    """
    This function allows the user to enter values
    :return: the list of values
    """
    inp_text = [
        'Введите количество отработанных часов: ',
        'Введите значение часовой ставки: ',
        'Введите размер премии: '
    ]
    int_param = {'work_hours': None, 'rate': None, 'prize': None}
    text_index = 0

    for key in int_param.keys():
        while True:
            try:
                int_param[key] = float(input(inp_text[text_index]))
                break
            except ValueError:
                if not int_param['prize']:
                    break
                else:
                    print('Введенное значение не является числом')
        text_index += 1

    return [val for val in int_param.values()]


def payroll_calc():
    """
    This function calculates wages
    :return: wages value
    """
    if len(sys.argv) > 1:
        try:
            parameters = [float(el) for el in sys.argv[1:]]
            if len(parameters) < 3:
                parameters.append(0)
        except ValueError:
            print(f'Один из введенных параметров не является числом, попробуйте снова')
            return
    else:
        parameters = input_param()
        print(parameters)

    return parameters[0] * parameters[1] + parameters[2] if parameters[2] else parameters[0] * parameters[1]


if __name__ == '__main__':
    payroll = payroll_calc()
    print(f'Заработная плата сотрудника составляет {"%.2f" % payroll} рублей') if payroll \
        else print('Расчет невозможен')
