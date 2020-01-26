def report(f_name, f_age, f_city):
    result = '{}, {} лет, проживает в городе {}'.format(f_name, f_age, f_city)
    return result


name = input('Введите имя: ')
age = input('Введите возраст: ')
city = input('Введите город проживания: ')

print(report(name, age, city))
