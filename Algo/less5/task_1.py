"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import Counter
from statistics import mean

while True:
    try:
        company_count = int(input('Введите количество предприятий: '))
        break
    except ValueError:
        print('Введенное значение не является числом!')

company_rating = Counter()

for i in range(1, company_count + 1):
    company_name = input(f'Введите название предприятия № {i}: ')
    while True:
        try:
            quarter_profit = input('Введите прибыль предприятия за каждый квартал через пробел: ').split()
            if len(quarter_profit) < 4:
                raise ValueError
            company_profit = [int(elem) for elem in quarter_profit]
            break
        except ValueError:
            print('Вы подали доход не за все отчетные периоды или предоставлили неверные данные!')
    for elem in company_profit:
        company_rating[company_name] += elem

company_avg_profit = mean(company_rating.values())

print(f'Средняя годовая прибыль всех предприятий: {company_avg_profit}')

lower_profit, upper_profit = [], []

for key, val in company_rating.items():
    lower_profit.append(key) if val < company_avg_profit else upper_profit.append(key)

print(f'Предприятия с прибылью выше среднего значения: {" ".join(upper_profit)}')
print(f'Предприятия с прибылью ниже среднего значения: {" ".join(lower_profit)}')
