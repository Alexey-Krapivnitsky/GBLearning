"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""

# Вводимое число захардкорил, так как оно в рекурсии не участвует
# и новых знаний оформление ввода не принесет


def even_odd(user_num, even_count=0, odd_count=0):
    if user_num <= 0:
        print(f'В введенном числе количество четных цифр {even_count}, нечетных - {odd_count}')
        return
    if user_num % 10 % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    even_odd(int((user_num - user_num % 10) / 10), even_count, odd_count)


if __name__ == '__main__':
    even_odd(133000)
