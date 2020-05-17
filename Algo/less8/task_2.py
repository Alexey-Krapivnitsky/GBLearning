"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
import timeit


def merge_sort(user_arr):
    if len(user_arr) == 1:
        return
    mid_point = len(user_arr) // 2
    left_arr = user_arr[:mid_point]
    right_arr = user_arr[mid_point:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    left_index, right_index, scratch_index = 0, 0, 0
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            user_arr[scratch_index] = left_arr[left_index]
            left_index += 1
        else:
            user_arr[scratch_index] = right_arr[right_index]
            right_index += 1
        scratch_index += 1

    for i in range(left_index, len(left_arr)):
        user_arr[scratch_index] = left_arr[i]
        scratch_index += 1

    for i in range(right_index,len(right_arr)):
        user_arr[scratch_index] = right_arr[i]
        scratch_index += 1

    return user_arr


USER_ARR = [50 * random.random() for _ in range(10)]

print(USER_ARR)
print(merge_sort(USER_ARR))

print(timeit.timeit("merge_sort(USER_ARR)",
                    setup="from __main__ import merge_sort, USER_ARR", number=1000))


"""
Исходный список:
[17.884394638850537, 7.244612750981555, 0.469983819750891, 31.453743881089647, 8.920325109717314]
На выходе:
[0.469983819750891, 7.244612750981555, 8.920325109717314, 17.884394638850537, 31.453743881089647]
Время выполнения:
0.009848799999999998
Время выполнения для 1000 элементов:
4.1451395
По сравнению с пузырьковой сортировкой для 1000 элементов временной показатель не очень хороший.
(Для пузырьковой в среднем 0.32781420000000006 сек.)
"""