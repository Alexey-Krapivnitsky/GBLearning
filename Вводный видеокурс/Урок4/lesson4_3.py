my_list_1 = [2, 2, 5, 12, 8, 2, 12]

for every in my_list_1:
    if my_list_1.count(every) > 1:
        while my_list_1.count(every) > 0:
            my_list_1.remove(every)
print(my_list_1)
