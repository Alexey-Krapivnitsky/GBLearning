with open('file5_1.txt', 'w', encoding='utf-8') as f_obj:
    while True:
        user_string = input('Введите строку (для завершения введите пустую строку): ')
        if user_string:
            f_obj.write(f'{user_string}\n')
        else:
            break
