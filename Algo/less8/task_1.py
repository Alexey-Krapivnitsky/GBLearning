"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
from random import randint
import timeit


def bubble_sort_1(user_arr):
    cycle_count = 0
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(1, len(user_arr)):
            if user_arr[i] < user_arr[i-1]:
                user_arr[i], user_arr[i-1] = user_arr[i-1], user_arr[i]
                not_sorted = True
        cycle_count += 1
    if cycle_count > 1:
        print(cycle_count)
    return user_arr


def bubble_sort_2(user_arr):
    cycle_count = 0
    not_sorted = True
    while not_sorted:
        sort_count = 0
        not_sorted = False
        for i in range(1, len(user_arr)):
            if user_arr[i] < user_arr[i-1]:
                user_arr[i], user_arr[i-1] = user_arr[i-1], user_arr[i]
                sort_count += 1
                not_sorted = True
        cycle_count += 1
        if sort_count == 0:
            break
    if cycle_count > 1:
        print(cycle_count)
    return user_arr


USER_ARR = [randint(-100, 100) for _ in range(10)]
USER_ARR_2 = [randint(-100, 100) for _ in range(10)]
# print(USER_ARR)
# print(bubble_sort_1(USER_ARR))
# print(USER_ARR_2)
# print(bubble_sort_1(USER_ARR_2))

# замеры 10
print(timeit.timeit("bubble_sort_1(USER_ARR)",
                    setup="from __main__ import bubble_sort_1, USER_ARR", number=1000))
print(timeit.timeit("bubble_sort_2(USER_ARR_2)",
                    setup="from __main__ import bubble_sort_2, USER_ARR_2", number=1000))

USER_ARR = [randint(-100, 100) for _ in range(100)]
USER_ARR_2 = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("bubble_sort_1(USER_ARR)",
                    setup="from __main__ import bubble_sort_1, USER_ARR", number=1000))
print(timeit.timeit("bubble_sort_2(USER_ARR_2)",
                    setup="from __main__ import bubble_sort_2, USER_ARR_2", number=1000))

USER_ARR = [randint(-100, 100) for _ in range(10000)]
USER_ARR_2 = [randint(-100, 100) for _ in range(10000)]


# замеры 1000
print(timeit.timeit("bubble_sort_1(USER_ARR)",
                    setup="from __main__ import bubble_sort_1, USER_ARR", number=1000))
print(timeit.timeit("bubble_sort_2(USER_ARR_2)",
                    setup="from __main__ import bubble_sort_2, USER_ARR_2", number=1000))

"""
Результаты замеров в порядке увеличения списка:
для bubble_sort_1
0.0016344000000000011
0.014258300000000002
0.32781420000000006

для bubble_sort_2
0.0016519000000000013
0.015078600000000004
0.32373730000000006

Таким образом, несмотря на отсечку сортировки условием, 
увеличения эффективности не наблюдается. При замере количества проходов по циклу
(ввел дополнительную переменную cycle_count) получается, что количество проходов примерно одинаково:
для bubble_sort_1
6
93
952
для bubble_sort_2
5
87
975
Вывод: значительного увеличения эффективности введение дополнительного условия не дает.

Для дополнительной проверки сделал замеры на 10000 элементах:
9879
20.2807562
9890
21.017153299999997
"""
