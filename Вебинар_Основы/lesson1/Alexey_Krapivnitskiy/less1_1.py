user_time = int(input('Введите время в секундах: '))
user_hour = user_time // 3600
user_minute = (user_time % 3600) // 60
user_second = (user_time % 3600) % 60
print(f'Вы ввели {user_hour} часов {user_minute} минут {user_second} секунд')