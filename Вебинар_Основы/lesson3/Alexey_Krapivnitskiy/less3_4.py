def my_func(x, y):
    return x**y


def my_func2(x, y):
    z = x
    for i in range(abs(y)-1):
        z *= x
    return 1/z


result = my_func(0.2, -10)
result2 = my_func2(0.2, -10)

print(result)
print(result2)
