import json


def firm_average(file_obj):
    try:
        name, f_type, revenue, expenses = file_obj.readline().split()
        return {name: int(revenue) - int(expenses)}
    except ValueError:
        return


if __name__ == '__main__':
    with open('file5_7.txt', 'r', encoding='utf-8') as f_obj:
        firms = {}
        firm = firm_average(f_obj)
        while firm:
            firms.update(firm)
            firm = firm_average(f_obj)

    result = [firms, {'average_profit': sum([val for val in firms.values() if val > 0])}]

    with open('file5_7_2.json', 'w') as json_obj:
        json.dump(result, json_obj)
