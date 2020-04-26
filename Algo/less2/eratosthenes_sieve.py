from math import sqrt


def eratosthenes_sieve(numbers, number=2):
    if number > sqrt(max(numbers)):
        return numbers
    else:
        numbers = [elem for elem in numbers if elem % number or elem == number]
        return eratosthenes_sieve(numbers, number + 1)


if __name__ == '__main__':
    while True:
        try:
            USER_RANGE = int(input(f'Задайте предел поиска простых чисел... '))
            break
        except ValueError:
            print('Введенное значение не является целым положительным числом')

    USER_LIST = list(range(2, USER_RANGE+1))
    print(eratosthenes_sieve(USER_LIST))
