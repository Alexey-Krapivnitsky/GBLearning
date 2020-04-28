"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
"""

# Вводимое число захардкорил, так как оно в рекурсии не участвует
# и новых знаний оформление ввода не принесет


def series_sum(user_count, result=1, start=1.0):
    if user_count == 1:
        print(f'Сумма ряда равна {result}')
        return
    next_num = start / -2
    result += next_num
    start /= -2
    user_count += -1
    series_sum(user_count, result, next_num)


if __name__ == '__main__':
    series_sum(3)
