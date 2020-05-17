"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
from random import randint
from statistics import median
import timeit


def median_search(user_arr):
    smaller_arr = []
    while len(smaller_arr) < len(user_arr):
        smaller_arr.append(min(user_arr))
        user_arr.remove(min(user_arr))
    if len(smaller_arr) != len(user_arr):
        return max(smaller_arr)
    else:
        return (min(user_arr) + max(smaller_arr)) / 2


USER_ARR = [randint(1, 100) for _ in range(1000)]

print(USER_ARR)
print(f'Проверка с помощью модуля statistics: {median(USER_ARR)}')
print(f'Медиана списка равна: {median_search(USER_ARR)}')

# USER_ARR = [randint(1, 100) for _ in range(1000)]
# print(timeit.timeit("median_search(USER_ARR)",
#                     setup="from __main__ import median_search, USER_ARR", number=1000))

"""
Для проверки времени выполнения специально введена копия пользовательского списка.:
def median_search(user_arr):
    func_arr = user_arr.copy()
    smaller_arr = []
    while len(smaller_arr) < len(func_arr):
        smaller_arr.append(min(func_arr))
        func_arr.remove(min(func_arr))
    if len(smaller_arr) != len(func_arr):
        return max(smaller_arr)
    else:
        return (min(func_arr) + max(smaller_arr)) / 2
Без нее будет ошибка, так как меняется входной список.
Время выполнения на 1000 элементах - в среднем 19.602458600000002 сек, что не очень
хорошо. Без создания копии выполняется намного быстрее (за доли секунды).
"""