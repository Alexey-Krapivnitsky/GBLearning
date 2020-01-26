#Вариант 1 кривенький

my_list_1 = [1, 1, 2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
my_set_1 = set(my_list_1)
my_set_2 = set(my_list_2)
my_set_1.difference_update(my_set_2)
my_list_1 = list(my_set_1)
print(my_list_1)

#Вариант 2 count
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
for every in my_list_2:
    while my_list_1.count(every) > 0:
        my_list_1.remove(every)
print(my_list_1)