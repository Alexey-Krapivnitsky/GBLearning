a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
c = int(input('Введите число 3: '))


def max_number(num1, num2, num3):
    result = max(num1, num2, num3)
    return result


print(max_number(a, b, c))
