"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

from random import randrange


START_ARRAY = [randrange(elem) for elem in range(1, 20)]
print(START_ARRAY)

MAX_COUNT = max(START_ARRAY, key=lambda elem: START_ARRAY.count(elem))

print(f'В заданном массиве чаще всего встречается число {MAX_COUNT}, '
      f'количество повторений - {START_ARRAY.count(MAX_COUNT)}')
