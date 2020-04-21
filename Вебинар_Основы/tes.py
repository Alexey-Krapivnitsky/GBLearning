def create_list_from_number(number):
    result = [0, 0, 0, 0]
    for i in range(len(result)):
        current_number = round(number / (10 ** (i+1)) - int(number / (10 ** (i+1))), 2)
        if i != 0:
            mul_mod = -1 if number < 0 else 1
            current_number = (current_number * 100 - mul_mod * ((abs(current_number) * 100) % 10)) / 100
        if abs(current_number) < 0.1:
            current_number = 0
        result[i] = current_number
    return result


print(create_list_from_number(-135.5))

print(list[5])