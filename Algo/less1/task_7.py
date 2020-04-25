"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""

while True:
    try:
        LEN_A = int(input('Введите длину стороны А: '))
        LEN_B = int(input('Введите длину стороны B: '))
        LEN_C = int(input('Введите длину стороны C: '))
        break
    except ValueError:
        print('Вы ввели недопустимые параметры, попробуйте снова\n')

if (LEN_A < LEN_B + LEN_C) and (LEN_B < LEN_A + LEN_C) and (LEN_C < LEN_B + LEN_A):
    if LEN_A == LEN_B and LEN_B == LEN_C:
        TRIANGLE_TYPE = 'Равносторонний'
    elif LEN_A == LEN_B or LEN_B == LEN_C or LEN_A == LEN_C:
        TRIANGLE_TYPE = 'Равнобедренный'
    else:
        TRIANGLE_TYPE = 'Разносторонний'
    print(f'Треугольник существует, тип треугольника - {TRIANGLE_TYPE}')
else:
    print(f'Треугольник не существует')
