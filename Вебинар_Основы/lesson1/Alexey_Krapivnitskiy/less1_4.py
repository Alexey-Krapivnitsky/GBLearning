# user_number = input('Введите целое положительное число: ')
user_number = '4387'
num_digit = len(user_number) - 1
max_digit = int(user_number[num_digit])
while num_digit > 0:
    difference = max_digit - int(user_number[num_digit - 1])
    if difference < 0:
        max_digit = int(user_number[num_digit - 1])
    num_digit -= 1
print(f'Максимальная цифра в числе {user_number} - цифра "{max_digit}"')
