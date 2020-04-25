"""
Задание 4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

Подсказка:
Нужно обойтись без ф-ций randint() и uniform()
Использование этих ф-ций = задание не засчитывается

Функцию random() использовать можно
Опирайтесь на пример к уроку
"""

from random import random


while True:
    GENERATION_TYPE = input('Выберите, что Вы хотите сгенерировать:\n'
                            '1 - целое число\n'
                            '2 - вещественное число\n'
                            '3 - символ\n')
    try:
        if GENERATION_TYPE == '1':
            print('Целое число в пределах')
            LEFT = int(input('от: '))
            RIGHT = int(input('до: '))
            RESULT = int(random() * (RIGHT - LEFT + 1)) + LEFT
            break
        elif GENERATION_TYPE == '2':
            print('Вещественное число в пределах')
            LEFT = float(input('от: '))
            RIGHT = float(input('до: '))
            RESULT = random() * (RIGHT - LEFT) + LEFT
            break
        elif GENERATION_TYPE == '3':
            print('Символ в пределах')
            LEFT = input('от: ')
            if LEFT.isalpha() and len(LEFT) == 1:
                LEFT = ord(LEFT)
            else:
                raise ValueError
            RIGHT = input('до: ')
            if RIGHT.isalpha() and len(RIGHT) == 1:
                RIGHT = ord(RIGHT)
            else:
                raise ValueError
            RESULT = chr(int(random() * (RIGHT - LEFT + 1)) + LEFT)
            break
    except ValueError:
        print('Вы ввели недопустимые параметры, попробуйте снова\n')

print(f'Ваш реультат: {RESULT}')
