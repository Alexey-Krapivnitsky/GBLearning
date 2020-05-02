"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""
from random import randint


USER_ARRAY = []
MIN_ARRAY = []

while True:
    try:
        ROW_COUNT = int(input('Задайте количество строк в матрице: '))
        COLUMN_COUNT = int(input('Задайте количество столбцов в матрице: '))
        break
    except ValueError:
        print('Введенное значение не является числом')

for i in range(ROW_COUNT):
    ROW_ARRAY = []
    for j in range(COLUMN_COUNT):
        ROW_ARRAY.append(randint(1, 99))
    USER_ARRAY.append(ROW_ARRAY)

for row in USER_ARRAY:
    for elem in row:
        out_char = f'{elem}' if elem >= 10 else f' {elem}'
        print(out_char, end=' ')
    print()

for i in range(COLUMN_COUNT):
    TEMP_ARRAY = []
    for j in range(ROW_COUNT):
        TEMP_ARRAY.append(USER_ARRAY[j][i])
    MIN_ARRAY.append(min(TEMP_ARRAY))

print(f'{MIN_ARRAY} - минимальные значения по столбцам')
print(f'Максимальное среди них: {max(MIN_ARRAY)}')
