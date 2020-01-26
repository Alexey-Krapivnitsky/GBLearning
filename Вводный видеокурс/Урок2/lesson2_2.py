number = int(input('Введите целое число: '))
while number not in range(1, 10):
	print('Число должно быть больше 0, но меньше 10')
	number = int(input('Введите целое число: '))
print('Число {0} в необходимом диапазоне, квадрат числа равен {1}'.format(number, number ** 2))
