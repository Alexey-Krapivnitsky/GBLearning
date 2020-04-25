"""
Задание 3. По введенным пользователем координатам двух
точек вывести уравнение прямой,
проходящей через эти точки.

Подсказка:
Запросите у пользователя значения координат X и Y для первой и второй точки
Найдите в учебнике по высшей математике формулы расчета:
k – угловой коэффициент (действительное число), b – свободный член (действительное число)
Сформируйте уравнение прямой по формуле: y = kx + b – функция общего вида

Пример:
X1_VAL = 2, Y1_VAL = 3, X2_VAL = 4, Y2_VAL = 5
Уравнение прямой, проходящей через эти точки: y = 1.0x + 1.0
"""

X1_VAL = -4
Y1_VAL = -3
X2_VAL = 2
Y2_VAL = 4
DIFF_X = (X2_VAL - X1_VAL)
DIFF_Y = (Y1_VAL - Y2_VAL)
FREE_TERM = (X1_VAL * Y2_VAL - X2_VAL * Y1_VAL)

print(f'Уравнение прямой, проходящей через точки A({X1_VAL},{Y1_VAL}) и B({X2_VAL},{Y2_VAL}):'
      f'\n {DIFF_Y}x + {DIFF_X}y + ({FREE_TERM}) = 0')
