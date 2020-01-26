import random


def create_list():
    new_list = []
    for i in range(10):
        new_list.append(random.randint(1, 100))
    return new_list


def list_elem(inp_list):
    if inp_list == [] or inp_list is None:
        new_elem = None
    else:
        new_elem = random.choice(inp_list)
    return new_elem
