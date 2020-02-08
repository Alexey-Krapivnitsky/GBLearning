# структура описания товара
tmp_characteristic = {'название': None, 'цена': None, 'количество': None, 'ед.изм.': None}
# база данных товаров
product_database = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед.изм.': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'ед.изм.': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'ед.изм.': 'шт.'})
]
# аналитическая база
product_analitic = {}

# цикл ввода нового товара
while True:
    if input('Для перехода к аналитике введите "0", для ввода нового товара - нажмите Enter ') == '0':
        break
    else:
        tmp_characteristic['название'] = input('Введите название товара: ')
        tmp_characteristic['цена'] = int(input('Введите стоимость товара: '))
        tmp_characteristic['количество'] = int(input('Введите количество товара: '))
        tmp_characteristic['ед.изм.'] = input('Введите единицу измерения товара: ')
        tmp_as_tuple = len(product_database) + 1, tmp_characteristic
        product_database.append(tmp_as_tuple)

# построение аналитической базы
for every in product_database:
    for key, val in every[1].items():
        if key in product_analitic.keys():
            product_analitic[key].append(val)
        else:
            product_analitic.setdefault(key, [val])

# вывод аналитики
print('\n', product_analitic, '\n')  # только для показа, что действительно аналитика хранится в словаре

for key, val in product_analitic.items():
    print(f'{key} - {val}')
