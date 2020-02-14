import timeit
import random


code1 = """
def my_func(a, b, c):
    num_as_list = sorted([a, b, c])
    return sum(num_as_list[1:])


result = my_func(15, 28, -31)
print(result)"""

code2 = """
def my_func(a, b, c):
    elements = [a, b, c]
    elements.remove(min(elements))
    return sum(elements)


result = my_func(15, 28, -31)
print(result)"""

list_1 = random.sample(list(range(1, 10000000)), 1000000)
list_2 = list.copy(list_1)

print (str(timeit.timeit(f"sorted({list_1})", number=1)))
print (str(timeit.timeit(f"min({list_2})", number=1)))

# print (str(timeit.timeit(f"sorted({random.sample(list(range(1, 10000000)), 1000000)})", number=1)))
# print (str(timeit.timeit(f"min({random.sample(list(range(1, 10000000)), 1000000)})", number=1)))

print (str(timeit.timeit(code1, number=1)))
print (str(timeit.timeit(code2, number=1)))