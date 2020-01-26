import os


def create_dir():
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), f'dir_{i}')
        os.mkdir(new_path)


def delete_dir():
    for i in range(1, 10):
        os.rmdir(os.path.join(os.getcwd(), f'dir_{i}'))
