"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""

from collections import deque


NUM_1 = deque(list(input('Введите число № 1: ')))
NUM_2 = deque(list(input('Введите число № 2: ')))

print(f'Вы ввели числа: {list(NUM_1)} и {list(NUM_2)}')

MUL_NUM_1 = NUM_1.copy()
MUL_NUM_2 = NUM_2.copy()

while len(NUM_1) != len(NUM_2):
    if len(NUM_1) < len(NUM_2):
        NUM_1.appendleft('0')
    else:
        NUM_2.appendleft('0')

SUM_RESULT = deque()
MUL_TEMP_RESULT = deque()
MUL_RESULT = deque()
remains = 0

while NUM_1:
    TEMP_SUM = int(NUM_1.pop(), 16) + int(NUM_2.pop(), 16) + remains
    remains = 1 if TEMP_SUM > 15 else 0
    SUM_RESULT.appendleft(hex(TEMP_SUM)[-1].upper())
if remains:
    SUM_RESULT.appendleft(str(remains))

del NUM_1
del NUM_2

if remains == 1:
    remains = 0

if len(MUL_NUM_1) < len(MUL_NUM_2):
    MUL_NUM_1, MUL_NUM_2 = MUL_NUM_2, MUL_NUM_1

for i in range(len(MUL_NUM_2)):
    MUL_2 = int(MUL_NUM_2.pop(), 16)
    TEMP_RESULT = deque()
    for j in range(len(MUL_NUM_1)):
        MUL_1 = MUL_NUM_1.pop()
        TEMP_MUL = int(MUL_1, 16) * MUL_2 + remains
        remains = int(hex(TEMP_MUL)[-2], 16) if TEMP_MUL > 15 else 0
        TEMP_RESULT.appendleft(hex(TEMP_MUL)[-1])
        MUL_NUM_1.appendleft(MUL_1)
    if remains:
        TEMP_RESULT.appendleft(hex(remains)[-1])
        remains = 0
    MUL_TEMP_RESULT.appendleft(TEMP_RESULT)

for i in range(len(MUL_TEMP_RESULT)-1):
    if i == 0:
        NUM_1 = MUL_TEMP_RESULT.pop()
        NUM_1.appendleft('0')
        MUL_RESULT = NUM_1
    NUM_2 = MUL_TEMP_RESULT.pop()
    for j in range(i + 1):
        NUM_2.append('0')
    while NUM_2:
        TEMP_SUM = int(MUL_RESULT.pop(), 16) + int(NUM_2.pop(), 16) + remains
        remains = 1 if TEMP_SUM > 15 else 0
        MUL_RESULT.appendleft(hex(TEMP_SUM)[-1].upper())
    if remains:
        MUL_RESULT.appendleft(hex(remains)[-1])
    if MUL_TEMP_RESULT:
        MUL_RESULT.appendleft('0')

print(f'Сумма введенных чисел: {list(SUM_RESULT)}')
print(f'Произведение введенных чисел: {list(MUL_RESULT)}')

"""
Решить задачу классом я не успеваю, но я именно это направление изучил неплохо.
В качестве примеров мои классы для комплексных чисел и для стека:

1) class ComplexNumber:
    def __init__(self, number1, number2):
        self.real = number1
        self.imaginary = number2
        self.complex_number = None

    def __str__(self):
        self.complex_number = f'{self.real} + {self.imaginary}i' if self.imaginary > 0\
            else f'{self.real} - {abs(self.imaginary)}i'
        return f'{self.complex_number}'

    def __add__(self, other):
        result_real = self.real + other.real
        result_imaginary = self.imaginary + other.imaginary
        return ComplexNumber(result_real, result_imaginary)

    def __mul__(self, other):
        result_real = self.real * other.real - self.imaginary * other.imaginary
        result_imaginary = self.real*other.imaginary + self.imaginary * other.real
        return ComplexNumber(result_real, result_imaginary)

2) class DailyStack:

    def __init__(self):
        self.tasks_for_current_day = deque([], 24)
        self.temp_stack = deque([], 24)

    def push(self, new_task, new_time):
        self.tasks_for_current_day.append((new_time, new_task))
        self.sort_stack()

    def pop(self):
        return self.tasks_for_current_day.popleft()

    def get_tasks(self):
        return self.tasks_for_current_day

    def sort_stack(self):
        while self.tasks_for_current_day:
            next_elem = self.tasks_for_current_day.pop()
            while self.temp_stack and int(self.temp_stack[-1][0]) > int(next_elem[0]):
                self.tasks_for_current_day.append(self.temp_stack.pop())
            self.temp_stack.append(next_elem)
        while self.temp_stack:
            self.tasks_for_current_day.append(self.temp_stack.popleft())
"""