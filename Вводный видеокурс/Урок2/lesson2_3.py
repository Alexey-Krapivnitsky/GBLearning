pacient = dict.fromkeys(["Имя", "Фамилия", "Возраст", "Вес"])
print('Введите Ваши данные:\n')
for every in pacient:
    pacient[every] = input(every + ': ')
if int(pacient['Возраст']) in range(0,31):
    health_condition = "ваше состояние хорошее" if int(pacient['Вес']) in range(50,121) else "вам еще не поздно заняться собой"
elif int(pacient['Возраст']) in range(31,41):
    health_condition = "вам срочно требуется заняться собой" if int(pacient['Вес']) not in range(50,121) else "вы стараетесь следить за собой"
elif int(pacient['Возраст']) >= 41:
    health_condition = "вам рекомендуется обратиться к врачу" if int(pacient['Вес']) not in range(50,121) else "вы все еще следите за собой, хотя вам это уже и не надо"
else: health_condition = "возможно вам не хватает витаминов ))))"
print('Пациент {0} {1}, {2}'.format(pacient['Фамилия'], pacient['Имя'], health_condition))
