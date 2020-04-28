"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


def checking_theorem(upper_border, sum_numbers=0, start=1):
    sum_numbers += start
    if start == upper_border:
        print(f'Сумма чисел от одного до {upper_border} равна {sum_numbers}, \n'
              f'выражение n(n+1)/2 равно {int(upper_border * (upper_border + 1) / 2)}')
        return
    else:
        start += 1
        checking_theorem(upper_border, sum_numbers, start)


if __name__ == '__main__':
    checking_theorem(125)
