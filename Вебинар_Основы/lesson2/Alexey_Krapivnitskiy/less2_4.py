# user_string = input('Введите строку из нескольких слов, разделенных пробелами: ')
user_string = 'Я гулял по набережной и встретил Черезабороногузадерищенко'
tmp_as_list = user_string.split()

for number, word in enumerate(tmp_as_list, 1):
    print(number, word[:10])

