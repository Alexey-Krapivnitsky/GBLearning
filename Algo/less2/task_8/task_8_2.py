"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'
"""


def digit_count(numbers_count, user_digit, user_digit_count=0, turn_number=1):
    try:
        user_number = int(input(f'Введите число {turn_number}: '))
    except ValueError:
        print('Введенное значение не является целым положительным числом')
        digit_count(numbers_count, user_digit, user_digit_count, turn_number)
    else:
        user_digit_count += search_digit(user_number, user_digit)
        if turn_number == numbers_count:
            print(f'Число {user_digit} встречается в введенной '
                  f'последовательности чисел {user_digit_count} раз')
            return
        turn_number += 1
        digit_count(numbers_count, user_digit, user_digit_count, turn_number)


def search_digit(number, digit, count_sum=0):
    if number <= 0:
        return count_sum
    else:
        if digit == number % 10:
            count_sum += 1
        return search_digit(int((number - number % 10) / 10), digit, count_sum)


if __name__ == '__main__':
    while True:
        try:
            USER_COUNT = int(input(f'Сколько будет чисел?... '))
            SEARCHED_DIGIT = int(input(f'Какую цифру будем искать?... '))
            break
        except ValueError:
            print('Введенное значение не является целым положительным числом')

    digit_count(USER_COUNT, SEARCHED_DIGIT)
