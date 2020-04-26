"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите число: 23
Введите число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5
"""

# Не предусмотрен случай, когда есть числа с равной суммой.
# В таком случае числом с наибольшей суммой считается первое найденное из равных


def largest_amount(numbers_count, max_amount_numbers=0, digit_amount=0, turn_number=1):
    try:
        user_number = int(input(f'Введите число {turn_number}: '))
    except ValueError:
        print('Введенное значение не является целым положительным числом')
        largest_amount(numbers_count, max_amount_numbers, digit_amount, turn_number)
    else:
        temp_amount = search_amount(user_number)
        if temp_amount > digit_amount:
            digit_amount = temp_amount
            max_amount_numbers = user_number
        if turn_number == numbers_count:
            print(f'Максимальная сумма цифр в числе {max_amount_numbers}')
            return
        turn_number += 1
        largest_amount(numbers_count, max_amount_numbers, digit_amount, turn_number)


def search_amount(number, count_sum=0):
    if number <= 0:
        return count_sum
    else:
        count_sum += number % 10
        return search_amount(int((number - number % 10) / 10), count_sum)


if __name__ == '__main__':
    while True:
        try:
            USER_COUNT = int(input(f'Сколько будет чисел?... '))
            break
        except ValueError:
            print('Введенное значение не является целым положительным числом')

    largest_amount(USER_COUNT)
