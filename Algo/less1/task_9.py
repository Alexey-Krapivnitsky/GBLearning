"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
while True:
    try:
        NUMB_1 = int(input('Введите число 1: '))
        NUMB_2 = int(input('Введите число 2: '))
        NUMB_3 = int(input('Введите число 3: '))
        break
    except ValueError:
        print('Вы ввели недопустимые параметры, попробуйте снова\n')

RESULT = 0

if NUMB_1 == NUMB_2 and NUMB_2 == NUMB_3:
    print('Все числа равны')
else:
    if NUMB_2 > NUMB_1 > NUMB_3 or NUMB_2 < NUMB_1 < NUMB_3:
        RESULT = NUMB_1
    elif NUMB_1 > NUMB_2 > NUMB_3 or NUMB_1 < NUMB_2 < NUMB_3:
        RESULT = NUMB_2
    elif NUMB_1 > NUMB_3 > NUMB_2 or NUMB_1 < NUMB_3 < NUMB_2:
        RESULT = NUMB_3
    print(f'Среднее число из введенных - {RESULT}')
