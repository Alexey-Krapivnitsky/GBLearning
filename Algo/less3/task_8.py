"""
Задание_8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.

1-я строка:
3
3
3
3
2-я строка:
3
3
3
3
3-я строка:
3
3
3
3
4-я строка:
3
3
3
3
5-я строка:
3
3
3
3

[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
"""
ROW_COUNT = 0
COLUMN_COUNT = 0
USER_ARRAY = []

print('Заполните матрицу целыми числами')

while ROW_COUNT < 5:
    COLUMN_COUNT = 0
    ROW_ARRAY = []
    print(f'{ROW_COUNT + 1}-я строка')
    while COLUMN_COUNT < 4:
        try:
            ROW_ARRAY.append(int(input()))
            COLUMN_COUNT += 1
        except ValueError:
            print('Введенное значение не является числом')
    ROW_ARRAY.append(sum(ROW_ARRAY))
    USER_ARRAY.append(ROW_ARRAY)
    ROW_COUNT += 1

for elem in USER_ARRAY:
    print(elem)
