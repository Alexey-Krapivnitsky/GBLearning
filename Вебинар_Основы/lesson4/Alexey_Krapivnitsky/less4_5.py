from functools import reduce


numbers = [num for num in range(100, 1001) if not num % 2]
result = reduce(lambda x, y: x * y, numbers)

print(f'Произведение всех четных чисел от 100 до 1000 равно: {"%.3f" % (int(str(result)[:5]) / len(str(result)))}E '
      f'+ {len(str(result))}')
