"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""

from random import randrange


START_ARRAY = list(filter(lambda elem: elem != 0,
                          [randrange(elem) * randrange(-1, 2) for elem in range(1, 20)]))
print(START_ARRAY)

MIN_ELEM = min(START_ARRAY)
MIN_COUNT = START_ARRAY.count(MIN_ELEM)

if MIN_COUNT > 1:
    RESULT = f'Наименьший элемент: {MIN_ELEM}, встречается в этом массиве {MIN_COUNT} раза'
else:
    START_ARRAY = [elem for elem in START_ARRAY if elem != MIN_ELEM]
    RESULT = f'Наименьший элемент: {MIN_ELEM}, встречается в этом массиве 1 раз\n' \
             f'Второй наименьший элемент {min(START_ARRAY)}'

print(RESULT)
