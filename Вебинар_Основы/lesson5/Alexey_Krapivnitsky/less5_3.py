with open('staff.txt', 'r', encoding='utf-8') as f_obj:
    employees = {key: int(val) for key, val in
                 [row.strip(' руб.').split(', ') for row in f_obj.read().splitlines()]
                 }

poor_employees = {key: val for key, val in employees.items() if val < 20000}

print(f'Средний оклад всех сотрудников: {sum(employees.values()) / len(employees)} рублей')

print('Сотрудники, имеющие оклад менее 20000 рублей:')
for idx, (key, val) in enumerate(poor_employees.items(), 1):
    print(f'{idx}) {key} - {val} рублей')
