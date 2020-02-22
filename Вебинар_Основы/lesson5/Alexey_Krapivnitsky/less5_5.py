from random import randint


with open('file5_5.txt', 'w', encoding='utf-8') as f_obj:
    for i in range(1, 21):
        f_obj.write(f'{randint(-101, 101)} ')

with open('file5_5.txt', 'r', encoding='utf-8') as f_obj:
    result = sum(list(map(int, f_obj.readline().split())))

print(f'Сумма чисел в файле {f_obj.name} равна: {result}')