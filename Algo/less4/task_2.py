"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

from math import sqrt
from timeit import timeit
import sys


sys.setrecursionlimit(10000)


# Вариант 1 - "решето"
def eratosthenes_sieve(numbers, simply_number):
    result_numbers = []
    max_number = numbers[-1]
    for i in range(4, max_number, 2):
        numbers[i - 2] = 0
    next_number = 3
    stop_at = sqrt(max_number)
    while next_number <= stop_at:
        for i in range(next_number * 2, max_number, next_number):
            numbers[i - 2] = 0
        next_number += 2
        while next_number <= max_number and numbers[next_number - 2] == 0:
            next_number += 2
    for i in range(2, len(numbers)):
        if numbers[i - 2] != 0:
            result_numbers.append(i)
            if len(result_numbers) == simply_number:
                print(
                    f'{simply_number} - е простое число: {result_numbers[-1]}')
                break


# Вариант 2 - свой алгоритм
def eratosthenes_sieve_alternate(numbers, simply_number, number=2):
    if number > sqrt(max(numbers)):
        print(
            f'{simply_number} - е простое число: {numbers[simply_number - 1]}')
    else:
        numbers = [elem for elem in numbers if elem % number or elem == number]
        return eratosthenes_sieve_alternate(numbers, simply_number, number + 1)


# Вариант 3 - свой алгоритм - оптимизация
def eratosthenes_sieve_alternate_cycle(numbers, simply_number):
    for number in range(2, int(sqrt(max(numbers)))):
        numbers = [elem for elem in numbers if elem % number or elem == number]
    print(f'{simply_number} - е простое число: {numbers[simply_number - 1]}')


if __name__ == '__main__':
    while True:
        try:
            USER_RANGE = int(input(f'Задайте номер простого числа... '))
            break
        except ValueError:
            print('Введенное значение не является целым положительным числом')

    USER_LIST = list(range(2, USER_RANGE ** 2 + 1 if USER_RANGE > 1 else 3))

    print(
        timeit(
            'eratosthenes_sieve_alternate(USER_LIST, USER_RANGE)',
            setup='from __main__ import eratosthenes_sieve_alternate, USER_LIST, USER_RANGE',
            number=100))
    print(
        timeit(
            'eratosthenes_sieve(USER_LIST, USER_RANGE)',
            setup='from __main__ import eratosthenes_sieve, USER_LIST, USER_RANGE',
            number=100))
    print(
        timeit(
            'eratosthenes_sieve_alternate_cycle(USER_LIST, USER_RANGE)',
            setup='from __main__ import eratosthenes_sieve_alternate_cycle, '
            'USER_LIST, USER_RANGE',
            number=100))

"""
Для варианта № 1:
для 10-го числа - 0.0030457999999999874 секунд
для 100-го числа - 0.18686579999999964 секунд
для 1000-го числа (одно повторение) - 0.28928920000000247 секунд

Итак, вариант с решетом Эратосфена однозначно выигрывает у рекурсии.
Особенно на большом числе. Даже пришлось снизить количество повторений со 100 до 1,
так как рекурсия залипает.Так как делал по
классическому варианту решета, то сложность должна быть O(N*log(logN)).

Для варианта № 2:
для 10-го числа - 0.005135600000000018 секунд
для 100-го числа - 1.3976894 секунд
для 1000-го числа (одно повторение) - 15.6388462 секунд

Вобщем, второй вариант - это печально на больших числах.
По сложности получается, что генератор списка - это O(N) и N раз вызывается рекурсия,.
общая сложность - O(N ** 2), хотя вроде реализовано почти по алгоритму решета, но результаты
замеров говорят об обратном. Еще есть подозрение, что sqrt(max(numbers)) вносит свю лепту,
но не знаю, как оценить. Решение по оптимизации - применение цикла вместо рекурсии.

Для варианта № 3:
для 10-го числа - 0.0031831000000002163 секунд
для 100-го числа - 0.7874415000000003 секунд
для 1000-го числа (одно повторение) - 10.5344829 секунд

Третий вариант - оптимизация второго варианта дала прирост на малых числах почти в два раза,
на больших - в 1,5. Тем не менее наблюдается явный проигрыш на больших числах
алгоритму решета.
Сложность варианта № 3 - O(N ** 2), опять же не учел sqrt(max(numbers)).
"""
