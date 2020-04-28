"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""

# Раскомментируйте строку print(comp_number), если не хотите мучиться)))


from random import randint


def guess_the_number(comp_number=0, user_number=0, attempt_count=1):
    if attempt_count == 1:
        comp_number = randint(0, 100)
    # print(comp_number)
    print(f'Попытка № {attempt_count}, осталось попыток {10 - attempt_count}')
    try:
        user_number = int(input('Введите целое неотрицательное число от 0 до 100: '))
    except ValueError:
        print('Введенное значение не соответствует требуемым параметрам')
        guess_the_number(comp_number, user_number, attempt_count)
    else:
        if user_number == comp_number:
            print('Поздравляю, Вы угадали!')
            return
        elif user_number > comp_number:
            print('Ваше число больше загаданного')
        elif user_number < comp_number:
            print('Ваше число меньше загаданного')
        if attempt_count == 10:
            print('Вы исчерпали все попытки')
            return

        attempt_count += 1
        guess_the_number(comp_number, user_number, attempt_count)


if __name__ == '__main__':
    guess_the_number()
