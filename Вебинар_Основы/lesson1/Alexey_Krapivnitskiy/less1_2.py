# user_time = int(input('Введите время в секундах: '))
user_time = 21753

# вычисляем количество часов, минут и секунд
user_hour = user_time // 3600
user_minute = (user_time % 3600) // 60
user_second = (user_time % 3600) % 60

# формирование склонения часов, минут и секунд
if user_hour in [1]:
    hour_symbol = 'час'
elif user_hour in [2, 3, 4]:
    hour_symbol = 'часа'
else:
    hour_symbol = 'часов'
if user_minute in [1, 21, 31, 41, 51]:
    min_symbol = 'минута'
elif user_minute in [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54]:
    min_symbol = 'минуты'
else:
    min_symbol = 'минут'
if user_second in [1, 21, 31, 41, 51]:
    sec_symbol = 'секунда'
elif user_second in [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54]:
    sec_symbol = 'секунды'
else:
    sec_symbol = 'секунд'

# Вывод результата
print(f'Вы ввели {user_hour} {hour_symbol} {user_minute} {min_symbol} {user_second} {sec_symbol}')
