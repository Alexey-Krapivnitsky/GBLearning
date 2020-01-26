my_list = [15, 25, 16, -8, 24, 36, -12, 100, 120, -60, 45, -9]

result_list = [number for number in my_list if number > 0 and not number % 3 and number % 4]
res = []

for num in my_list:
    if not num % 3:
        print(num % 3)
        print (not 1)
        res.append(num)
print(res)
print(result_list)
