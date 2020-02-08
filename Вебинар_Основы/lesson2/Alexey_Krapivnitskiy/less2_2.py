# Используемые переменные
test_as_list = []  # Исходный список
result_as_list = []  # Результарующий список
tmp_as_list = []  # Временный список для обмена значениями
tmp_count = 0

# Цикл создания исходного списка
while True:
    try:
        digit = abs(int(input('Введите количество элементов списка: ')))  # Задаем длину списка
    except ValueError:
        print('Введенное значение не является целым числом')
    else:
        list_length = digit
        while list_length > 0:
            next_elem = input(f'Введите значение элемента с индексом {digit - list_length}: ')
            # Для создания разных типов данных в списке проверяем введенное значение
            if next_elem.isdigit():
                next_elem = int(next_elem)
            test_as_list.append(next_elem)
            list_length -= 1
        break
# Выводим исходный список
print(test_as_list)

finish_val = digit - 1 if digit % 2 > 0 else digit  # если длина списка нечетная - приводим к четной

# Цикл обмена значениями
while tmp_count < finish_val:
    tmp_as_list = test_as_list[tmp_count:tmp_count+2]
    tmp_as_list = list(reversed(tmp_as_list))
    result_as_list.extend(tmp_as_list)
    tmp_count += 2

# Если длина списка нечетная, добавляем в результирующий список последний элемент исходного списка
if digit % 2 > 0:
    result_as_list.append(test_as_list[-1])

# Выводим результирующий список
print(result_as_list)
