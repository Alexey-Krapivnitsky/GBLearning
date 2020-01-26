def calculation(number):
    if number != 13:
        number = number ** 2
    else:
        raise ValueError('Ошибка значения!')
    return number


user_number = int(input('Введите число от 1 до 100: '))
try:
    print(calculation(user_number))
except ValueError:
    print('Введенное число - чертова дюжина. Для ввода запрещено!')
