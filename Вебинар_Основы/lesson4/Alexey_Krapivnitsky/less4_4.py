from random import randint


start_val = [randint(1, 100) for i in range(50)]
my_counter = 0

print('Исходный список: ')
for el in start_val:
    print(el, end=', ')
    my_counter += 1
    if not my_counter % 10:
        print()

end_val = [el for el in start_val if start_val.count(el) == 1]
repeat_val = set([el for el in start_val if start_val.count(el) > 1])

print('\n Результирующий список: \n', *end_val, '\n', 'Повторяющиеся значения: \n', *repeat_val)
