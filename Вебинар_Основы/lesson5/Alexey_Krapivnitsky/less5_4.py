with open('file5_4.txt', 'r', encoding='utf-8') as f_obj:

    numbers = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    text_row = f_obj.readline()

    while text_row:
        key, val = text_row.strip().split(' - ')
        if key in numbers.keys():
            key = numbers[key]
        with open('file5_4_2.txt', 'a', encoding='utf-8') as result_f_obj:
            result_f_obj.write(f'{key} - {val}\n')
        text_row = f_obj.readline()
