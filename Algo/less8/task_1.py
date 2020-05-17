"""
1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import hashlib


USER_STRING = input("Введите строку из маленьких латинских букв: ")

print(f'Строка {USER_STRING} имеет длину {len(USER_STRING)} сиволов.')

subs_set = set()

for i in range(len(USER_STRING)):
    for j in range(len(USER_STRING) - 1 if i == 0 else len(USER_STRING), i, -1):
        subs_set.add(hashlib.sha1(USER_STRING[i:j].encode('utf-8')).hexdigest())

print("Количество различных подстрок в этой строке:", len(subs_set))

"""
Введите строку из маленьких латинских букв: papa
Строка papa имеет длину 4 сиволов.
Количество различных подстрок в этой строке: 6
"""