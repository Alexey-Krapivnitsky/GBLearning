import lesson10_1
from lesson10_2 import create_list, list_elem


lesson10_1.create_dir()
input()
# my_list = []
# my_list = None
my_list = create_list()
my_elem = list_elem(my_list)
lesson10_1.delete_dir()

print(my_list, ' ', my_elem)
