def div_func(a, b):
    """
    This function dividies two numbers:
    :param a: dividend
    :param b: divider
    :return: a / b
    """
    try:
        return a / b
    except ZeroDivisionError:
        print('На ноль делить нельзя!')


# while True:
#
#     while True:
#         try:
#             dividend = int(input('Введите первое число: '))
#             divider = int(input('Введите второе число: '))
#         except ValueError:
#             print('Введенное значение не является числом')
#         else:
#             print(f'Вы ввели {dividend} и {divider}')
#             break
#
#     result = div_func(dividend, divider)
#     if result:
#         print(f'Результат деления введенных чисел:  {"%.2f" % result}')
#
#     if input('Продолжить? (Y/N): ').upper() == 'N':
#         break

result2 = div_func(3, 0)
result3 = div_func(15, 5)
result4 = div_func(20, -5)
print(result3, result4)
