# Цикл ввода и проверки входного значения
while True:
    try:
        month_number = int(input('Введите порядковый номер месяца (от 1 до 12): '))
    except ValueError:
        print('Введенное значение не является целым числом')
    else:
        if month_number < 1 or month_number > 12:
            print('В году 12 месяцев. Введите число от 1 до 12!')
            continue
        else:
            break

# Решение через список
months = [
    [12, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [9, 1, 11],
]

print('Решение через list:')
if month_number in months[0]:
    print(f'Ваш месяц ({month_number}) - зимний')
elif month_number in months[1]:
    print(f'Ваш месяц ({month_number}) - весенний')
elif month_number in months[2]:
    print(f'Ваш месяц ({month_number}) - летний')
else:
    print(f'Ваш месяц ({month_number}) - осенний')

# Решение через словарь
months_as_dict = {
    1: ['январь', 'зимний'],
    2: ['февраль', 'зимний'],
    3: ['март', 'весенний'],
    4: ['апрель', 'весенний'],
    5: ['май', 'весенний'],
    6: ['июнь', 'летний'],
    7: ['июль', 'летний'],
    8: ['август', 'летний'],
    9: ['сентябрь', 'осенний'],
    10: ['октябрь', 'осенний'],
    11: ['ноябрь', 'осенний'],
    12: ['декабрь', 'зимний'],
}

print('Решение через dict:')
for key in months_as_dict.keys():
    if month_number == key:
        print(f'Ваш месяц {months_as_dict[key][0]} ({month_number}) - {months_as_dict[key][1]}')
