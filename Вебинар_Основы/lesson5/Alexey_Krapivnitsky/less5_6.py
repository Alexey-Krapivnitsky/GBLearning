result = {}

with open('file5_6.txt', 'r', encoding='utf-8') as f_obj:
    numbers = {key: val for key, val in
               [row.split(':') for row in f_obj.read().splitlines()]
               }
for key, val in numbers.items():
    lesson_val = []
    new_val = ''
    for char in val:
        if not char.isdigit() and new_val:
            lesson_val.append(int(new_val))
            new_val = ''
        elif char.isdigit():
            new_val += char
    result.update({key: sum(lesson_val)})

print('Сведения о часах по учебным дисциплинам: ', result)
