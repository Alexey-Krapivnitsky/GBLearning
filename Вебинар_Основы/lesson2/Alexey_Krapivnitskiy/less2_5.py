# rating_as_list = [7, 5, 3, 3, 2]
rating_as_list = []

while True:
    insert_count = False
    # Проверяем значение рейтинга
    try:
        rating = int(input('Введите рейтинговое значение (целое число). Для выхода введите 0: '))
    except ValueError:
        print('Введенное значение не является целым числом')
    else:
        # выходим по нажатию "0"
        if rating == 0:
            break
        # Если список не пустой (ну мало ли)
        if len(rating_as_list) > 0:
            for rait_elem in rating_as_list:
                if rating > rait_elem:
                    # Если введенный рейтинг больше исследуемого элемента,
                    # то вставляем рейтинг перед ним и отмечаем, что вставили элемент в переменной insert_count
                    rating_as_list.insert(rating_as_list.index(rait_elem), rating)
                    insert_count = True
                    break
            # Если ничего не вставляли, то добавляем рейтинг в конец списка
            if not insert_count:
                rating_as_list.append(rating)
        # Если список пустой, то просто добавляем элемент
        else:
            rating_as_list.append(rating)

        print(rating_as_list)
