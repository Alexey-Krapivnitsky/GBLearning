def random_finder(number=1):
    computer_number = 50
    tries = 1
    low = 1
    high = 100
    # Цикл отгадывания
    while computer_number != number:
        if computer_number > number:
            high = computer_number
# Задаем загаданное число верхней границей интервала
# Продолжаем делить полученный интервал наполовину.
            computer_number = computer_number - ((high-low)//2)
            print(computer_number, number, (high-low))
        elif computer_number < number:
            low = computer_number
# Задаем загаданное число нижней границей интервала
            computer_number = computer_number + ((high-low)//2)
            print(computer_number, number)
        tries += 1
    return tries


random_finder()
