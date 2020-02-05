# revenue = int(input('Введите значение выручки предприятия: '))
# costs = int(input('Введите значение издержек (затрат) предприятия: '))
revenue = 2873556
costs = 1569872

profit = revenue - costs  # прибыль (или убыток, тут как получится))))

if profit > 0:
    profitability = '%.2f' % ((profit / revenue) * 100)  # рентабельность
    employ_numbers = int(input('Введите, пожалуйста, количество сотрудников Вашего предприятия: '))
    employ_profit = '%.2f' % (profit / employ_numbers)
    result_str = f'\nВаше предприятие работает с прибылью, которая составляет {profit} рублей\n' \
                 f'Рентабельность выручки составляет {profitability} %\n' \
                 f'Прибыль в расчете на одного сотрудника составляет {employ_profit}'
elif profit == 0:
    result_str = f'Ваше предприятие самоокупается, но не приносит прибыли'
else:
    result_str = f'Ваше предприятие работает в убыток, который составляет {abs(profit)} рублей'

print(result_str)
