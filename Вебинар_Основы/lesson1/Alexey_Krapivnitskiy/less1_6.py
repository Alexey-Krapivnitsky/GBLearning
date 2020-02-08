# start_length = int(input('Введите Ваш начальный результат, км: '))
# wishful_length = int(input('Введите Ваш желаемый результат, км: '))
start_length = 2
wishful_length = 3

current_length = start_length  # текущая длина дистанции
day_count = 1

while current_length < wishful_length:
    # print(f'День {day_count} - {"%.2f" % current_length} км')  # ежедневный результат
    current_length += current_length / 10
    day_count += 1
print(f'Желаемого результата {wishful_length} километров Вы достигнете на {day_count} день')
