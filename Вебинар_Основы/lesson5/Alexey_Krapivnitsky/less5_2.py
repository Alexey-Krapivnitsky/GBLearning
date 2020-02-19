with open('file5_2.txt', 'r', encoding='utf-8') as f_obj:
    my_text_as_list = [row for row in f_obj.read().splitlines() if row]

print(f'В файле {f_obj.name} - {len(my_text_as_list)} строк, исключая пустые:\n')

for idx, row in enumerate(my_text_as_list, 1):
    result_row = ' '.join([each_word.strip(" ,!:.") for each_word in row.split()])
    print(f'В строке {idx} ({result_row}) количество слов - {len(row.split())}')
