"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

from random import sample
from time import time
# from timeit import timeit


def running_time(func):
    start_time = time()

    def g(n):
        for i in range(100):
            func(n)
        print(f'Время выполнения равно {time() - start_time} секунд')
    return g


@running_time
# Вариант № 1 - изначальное ДЗ № 6 урока № 3
def min_max_range_sum(user_array):
    min_elem = min(user_array)
    max_elem = max(user_array)
    min_idx = user_array.index(min_elem)
    max_idx = user_array.index(max_elem)

    result = sum(user_array[min_idx + 1:max_idx]) if min_idx < max_idx else \
        sum(user_array[max_idx + 1:min_idx])

    print(f'Сумма элементов между минимальным ({min_elem}) '
          f'и максимальным ({max_elem}) элементами: {result}')


@running_time
# Вариант № 2 - ДЗ № 6 урока № 3 алгоритм с циклами
def min_max_range_sum_alternate(user_array):
    min_elem = user_array[0]
    max_elem = user_array[0]
    result = 0

    for elem in user_array:
        if elem < min_elem:
            min_elem = elem
        if elem > max_elem:
            max_elem = elem
    min_idx = user_array.index(min_elem)
    max_idx = user_array.index(max_elem)

    temp_array = user_array[min_idx + 1:max_idx] if min_idx < max_idx \
        else user_array[max_idx + 1:min_idx]

    for elem in temp_array:
        result += elem

    print(f'Сумма элементов между минимальным ({min_elem}) '
          f'и максимальным ({max_elem}) элементами: {result}')


if __name__ == '__main__':
    USER_ARRAY = sample(range(1, 100000), 10000)
    print(USER_ARRAY)

    min_max_range_sum(USER_ARRAY)
    min_max_range_sum_alternate(USER_ARRAY)

    # print(timeit('min_max_range_sum(USER_ARRAY)',
    #              setup='from __main__ import min_max_range_sum, USER_ARRAY', number=100))

    # print(timeit('min_max_range_sum_alternate(USER_ARRAY)',
    #              setup='from __main__ import min_max_range_sum_alternate, USER_ARRAY', number=100))

"""
Вариант функции № 1:
Результат выполнения по измерению декоратора:
    0.08978772163391113 - 0.10272502899169922 секунд
Результат выполнения по timeit - в среднем 0.0930538 секунд
Сложность алгоритма рассчитать не получилось, так как надо 
смотреть исходники встроенных функций. Но в целом - такой вариант близок к идеальному.

Вариант функции № 2:
Результат выполнения по измерению декоратора:
    0.1825118064880371 - 0.24135446548461914 секунд
Результат выполнения по timeit:
    0.10104749999999998 - 0.1423705 секунд
Большая разница в вычислениях декоратора и модуля timeit
объясняется тем, что в декораторе для количества замеров используется цикл,
что вместе с самой функцией образует вложенный цикл и сложность O(N**2).
Сама функция имеет сложность 2N + 7, т.е. O(N). Но в любом случае скорость
вычислений превышает вариант с использованием встроенных функций min, max и sum
примерно на 50%.
"""
