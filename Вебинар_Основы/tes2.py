def info(**kwargs):
    print(", ".join(kwargs.keys()))
    for name, age in kwargs.items():
        print("%s - %d" % (name, age))


info(Рич=14, Сильва=9, Фигаро=12)