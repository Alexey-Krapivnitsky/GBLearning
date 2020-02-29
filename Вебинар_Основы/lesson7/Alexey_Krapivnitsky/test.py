def print_statistics(arr):
    mediana = None
    number = None
    if not len(arr):
        print('Список пустой или не предоставлен')
    else:
        arr = sorted(arr)
        number = len(arr)
        number1 = (number - 1) // 2
        if number % 2 == 0:
            mediana = (arr[number1] + arr[number1 + 1]) / 2
        else:
            mediana = arr[number1]

        print(f'Длина списка - {number}, Среднее - {sum(arr) / number}, '
              f'Минимальное значение - {min(arr)}, Максимальное значение - {max(arr)}, '
              f'Медиана списка - {mediana}')


print_statistics([5, 3, 4, 8])
print_statistics([5, 4, 3, 8, 9])
print_statistics([22])
print_statistics([])