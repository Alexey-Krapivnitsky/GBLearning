"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""

from random import sample


START_ARRAY = sample(range(-100, 100), 10)
MIN_ELEM = min(START_ARRAY)
MAX_ELEM = max(START_ARRAY)
MIN_IDX = START_ARRAY.index(MIN_ELEM)
MAX_IDX = START_ARRAY.index(MAX_ELEM)

print(f'Начальный массив {START_ARRAY}\n'
      f'Минимальный элемент массива {MIN_ELEM} на позиции {MIN_IDX},\n'
      f'Максимальный элемент массива {MAX_ELEM} на позиции {MAX_IDX}\n')

START_ARRAY[MIN_IDX], START_ARRAY[MAX_IDX] = MAX_ELEM, MIN_ELEM

print(f'Итоговый массив {START_ARRAY}')
