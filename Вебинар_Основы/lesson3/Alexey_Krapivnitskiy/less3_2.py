def print_user_data(name='', surname='', year_of_birth=1900, city='', e_mail='', **kwargs):
    """
    This function print user data, such as name, surname and other.
    Also print any additional user data with their names if you enter them
    :param name:
    :param surname:
    :param year_of_birth:
    :param city:
    :param e_mail:
    :param kwargs:
    :return: None, print user data string, additional user data string
    """
    if name and surname and year_of_birth and city and e_mail:
        print(f'{name} {surname}, {year_of_birth} года рождения, житель города {city}, е-мэйл: {e_mail}')
    else:
        print('Полностью или частично отсутствуют данные о пользователе')
    if kwargs:
        for key, val in kwargs.items():
            print(f'"{key}" - {val}', end=', ')
        print()


print('no kwargs')
print_user_data('Nik', 'Doubldon', 1955, 'London', 'nikd@mail.com')

print('\nkwargs there is')
print_user_data('Nik', 'Doubldon', 1955, 'London', 'nikd@mail.com',
                car='AudiQ6', fone=88004004040)

print('\nno args, no kwargs')
print_user_data()

print('\nno args, kwargs there is')
print_user_data(adress='Backer Street, 221', hobby='fishing')
