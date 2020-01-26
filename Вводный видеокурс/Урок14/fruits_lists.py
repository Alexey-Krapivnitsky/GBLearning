fruit_list1 = ['Яблоко', 'Груша', 'Банан', 'Киви', 'Манго']
fruit_list2 = ['Дуриан', 'Банан', 'Мандарин', 'Яблоко', 'Апельсин', 'Лимон', 'Киви']

match_fruit_list = [fruit for fruit in fruit_list1 if fruit in fruit_list2]

print(match_fruit_list)
