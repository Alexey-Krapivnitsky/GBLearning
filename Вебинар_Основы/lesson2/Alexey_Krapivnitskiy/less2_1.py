test_as_list = [159, 123.55, 'test', None, False, (15, 25), ['Norm', 'No Norm'], {'key1': 11, 'key2': 22}]

for order_num, every in enumerate(test_as_list, 1):
    print(f'Тип элемента {order_num}: {every} - {type(every)}')
