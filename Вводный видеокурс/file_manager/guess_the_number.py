import random


def game():
    comp_number = random.randint(0, 100)
    comp_number_min = 1
    comp_number_max = 100
    human_answer = None

    print('Здравствуй, человек! Я готов сразиться с тобой!\nЗагадай число от 1 до 100 и запиши его на бумажке\n'
          'Для подсказок мне нажимай " < " (мое число меньше твоего), " > " (мое число больше твоего) или " = " (я угадал)'
          'Если ты готов, то я начинаю...\n\n'
          )

    while human_answer != '=':
        print(f'Мое число {comp_number}')
        human_answer = input('Твоя подсказка: ')
        if human_answer == '<':
            if comp_number == 99:
                comp_number = 100
            else:
                comp_number_min = comp_number
                comp_number = comp_number_min + (comp_number_max - comp_number_min)//2
        elif human_answer == '>':
            comp_number_max = comp_number
            comp_number = comp_number_min + (comp_number_max - comp_number_min)//2
        if (comp_number_max - comp_number_min) <= 2:
            comp_number_min = 1
            comp_number_max = 100
    print('\nТы лузер. А я выиграл!!!')
    input('Нажмите любую кнопку для выхода ')
