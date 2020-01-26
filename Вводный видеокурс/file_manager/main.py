import sys
from structure import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_directory
from guess_the_number import game

save_info('Старт')

command_list = ['create_file', 'create_folder', 'delete', 'copy', 'list', 'help', 'change_dir', 'play']

try:
    command = sys.argv[1]
    if command not in command_list:
        raise NameError
except IndexError:
    print('Отсутствует команда')
except NameError:
    print('Неизвестная команда')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла или папки')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Отсутствует название копируемого или нового файла')
        else:
            copy_file(name, new_name)
    elif command == 'change_dir':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название каталога для перехода')
        else:
            change_directory(name)
    elif command == 'play':
        game()
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')
        print('change_dir - изменение рабочего каталога, введите путь')
        print('play - поиграть в "Угадай число"')

save_info('Конец')
