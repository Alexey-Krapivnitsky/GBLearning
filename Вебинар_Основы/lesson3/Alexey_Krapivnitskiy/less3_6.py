def int_func(int_string):
    return int_string[0].upper() + int_string[1:]


def modified_string(user_list):
    return ' '.join(list(map(int_func, user_list)))


# user_string = input('Введите строку из слов в нижнем регистре, разделенных пробелом: ').split()
# print(modified_string(user_string))

print(modified_string('after you create your repository on github you can customize its settings and content'.split()))
