"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from PyQt5 import QtWidgets, QtGui, QtCore
from collections import deque
from datetime import datetime
from memory_profiler import profile
import json
import sys


class DailyStack:

    def __init__(self):
        self.tasks_for_current_day = deque([], 24)
        self.temp_stack = deque([], 24)

    def push(self, new_task, new_time):
        self.tasks_for_current_day.append((new_time, new_task))
        self.sort_stack()

    def pop(self):
        return self.tasks_for_current_day.popleft()

    @profile
    def get_tasks(self):
        return self.tasks_for_current_day

    @profile
    def sort_stack(self):
        while self.tasks_for_current_day:
            next_elem = self.tasks_for_current_day.pop()
            while self.temp_stack and int(self.temp_stack[-1][0]) > int(next_elem[0]):
                self.tasks_for_current_day.append(self.temp_stack.pop())
            self.temp_stack.append(next_elem)
        while self.temp_stack:
            self.tasks_for_current_day.append(self.temp_stack.popleft())


class Daily(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_data = {}
        self.setFixedSize(600, 600)
        self.setWindowTitle('Ежедневник MyDaily')
        self.setStyleSheet('background-color: Wheat; font-size: 12px;'
                           'font-weight: bold; color: SaddleBrown')
        self.task_date = QtWidgets.QDateEdit()
        self.task_date.setCalendarPopup(True)
        self.task_date.setDate(datetime.today().date())
        self.task_date.setFixedSize(100, 25)
        self.task_date.setStyleSheet('background-color: LightGrey;')
        self.current_daily = DailyStack()
        self.time_list = [str(elem) for elem in range(24)]
        self.task_time = QtWidgets.QComboBox()
        self.task_time.addItems(self.time_list)
        self.task_time.setFixedSize(100, 25)
        self.task_time.setStyleSheet('background-color: LightGrey;')
        self.task_text = QtWidgets.QTextEdit()
        self.task_text.setFixedSize(350, 100)
        self.task_text.setStyleSheet('font-size: 16px; color: Crimson')
        self.task_label = QtWidgets.QLabel('Введите текст мероприятия или задачи сюда: ')
        self.add_btn = QtWidgets.QPushButton('Добавить задачу')
        self.add_btn.setFixedSize(205, 25)
        self.add_btn.setStyleSheet(f'QPushButton {{background-color: LimeGreen; color: Black}} '
                                   f'QPushButton:hover {{background-color: GreenYellow;}}')
        self.pop_btn = QtWidgets.QPushButton('Удалить задачу')
        self.pop_btn.setFixedSize(205, 25)
        self.pop_btn.setStyleSheet(f'QPushButton {{background-color: IndianRed; color: Black}} '
                                   f'QPushButton:hover {{background-color: Red;}}')
        self.report_table = QtWidgets.QTableView()
        self.report_table.setFixedHeight(450)
        self.report_table.setStyleSheet('background-color: AntiqueWhite; font-size: 14px; '
                                        'font-weight: semi-bold; color: Black')
        self.report_table.horizontalHeader().setStyleSheet('::section{background-color: Moccasin;'
                                                           'font-size: 14px; font-weight: bold;'
                                                           'color: DarkGreen}')
        self.report_model = QtGui.QStandardItemModel()
        self.report_model.setHorizontalHeaderLabels(['Время', 'Мероприятие'])
        self.datetime_box = QtWidgets.QFormLayout()
        self.datetime_box.addRow('Выберите дату', self.task_date)
        self.datetime_box.addRow('Выберите время', self.task_time)
        self.left_box = QtWidgets.QVBoxLayout()
        self.left_box.addLayout(self.datetime_box)
        self.left_box.addWidget(self.add_btn)
        self.left_box.addWidget(self.pop_btn)
        self.left_box.addStretch()
        self.tasks_box = QtWidgets.QVBoxLayout()
        self.tasks_box.setAlignment(QtCore.Qt.AlignTop)
        self.tasks_box.addWidget(self.task_label)
        self.tasks_box.addWidget(self.task_text)
        self.tasks_box.addStretch()
        self.ui_box = QtWidgets.QHBoxLayout()
        self.ui_box.addLayout(self.left_box)
        self.ui_box.addLayout(self.tasks_box)
        self.main_box = QtWidgets.QVBoxLayout()
        self.main_box.addLayout(self.ui_box)
        self.main_box.addWidget(self.report_table)
        self.central_screen = QtWidgets.QWidget()
        self.central_screen.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.central_screen.setLayout(self.main_box)
        self.setCentralWidget(self.central_screen)
        self.insert_time()
        self.clear_daily()
        self.set_new_daily()
        self.add_btn.clicked.connect(self.add_to_stack)
        self.pop_btn.clicked.connect(self.pop_from_stack)
        self.task_date.dateChanged.connect(self.set_new_daily)

    def insert_time(self):
        for i in range(len(self.time_list)):
            item_1 = QtGui.QStandardItem(self.time_list[i])
            item_2 = QtGui.QStandardItem(' ')
            self.report_model.insertRow(i, [item_1, item_2])
        self.report_table.setModel(self.report_model)
        self.report_table.setColumnWidth(1, 480)
        self.report_table.verticalHeader().hide()

    def add_to_stack(self):
        self.current_daily.push(self.task_text.toPlainText(),
                                self.task_time.currentData(role=QtCore.Qt.DisplayRole))
        self.task_text.clear()
        self.rewrite_table()
        self.update_load_data()

    @profile
    def pop_from_stack(self):
        if self.current_daily.tasks_for_current_day:
            self.current_daily.pop()
        self.update_load_data()
        self.rewrite_table()

    def rewrite_table(self):
        self.report_model.clear()
        for elem in self.current_daily.get_tasks():
            item_1 = QtGui.QStandardItem(elem[0])
            item_2 = QtGui.QStandardItem(elem[1])
            item_1.setTextAlignment(QtCore.Qt.AlignCenter)
            item_2.setTextAlignment(QtCore.Qt.AlignCenter)
            self.report_model.appendRow([item_1, item_2])
        self.report_model.setHorizontalHeaderLabels(['Время (час.)', 'Мероприятие'])
        self.report_table.setModel(self.report_model)
        self.report_table.setColumnWidth(1, 480)
        self.report_table.verticalHeader().hide()

    @profile
    def update_load_data(self):
        self.load_data[self.task_date.date().toPyDate().strftime('%d.%m.%Y')] = \
            list(self.current_daily.tasks_for_current_day)
        with open('Daily.json', 'w', encoding='utf-8') as daily_book:
            json.dump(self.load_data, daily_book)

    @profile
    def set_new_daily(self):
        try:
            with open('Daily.json', 'r', encoding='utf-8') as daily_book:
                self.load_data = json.load(daily_book)
        except IOError:
            self.update_load_data()
        daily_key = self.task_date.date().toPyDate().strftime('%d.%m.%Y')
        daily_value = list(self.current_daily.tasks_for_current_day)
        if daily_key in self.load_data.keys():
            self.current_daily = DailyStack()
            self.current_daily.tasks_for_current_day = deque(self.load_data[daily_key])
        else:
            self.load_data.setdefault(daily_key, daily_value)
            self.current_daily = DailyStack()
        self.rewrite_table()
        with open('Daily.json', 'w', encoding='utf-8') as daily_book:
            json.dump(self.load_data, daily_book)

    def clear_daily(self):
        if datetime.today().day in range(25, 31):
            temp_keys = []
            with open('Daily.json', 'r', encoding='utf-8') as daily_book:
                self.load_data = json.load(daily_book)
            for key in self.load_data.keys():
                checked_date = datetime.strptime(key, '%d.%m.%Y')
                if checked_date.month == datetime.today().month \
                        and datetime.today().year - checked_date.year == 1:
                    temp_keys.append(key)
            for elem in temp_keys:
                self.load_data.pop(elem)
            with open('Daily.json', 'w', encoding='utf-8') as daily_book:
                json.dump(self.load_data, daily_book)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    NEW_WINDOW = Daily()
    NEW_WINDOW.show()
    sys.exit(app.exec_())

"""
Windows10 Home 64 bit, Python 3.7 32 bit

Провел анализ своего приложения "Ежедневник" 
Содержание json на момент проверки:
{"10.05.2020": [["0", "11"], ["1", "222"], ["6", "1"], ["7", "2"], ["8", "3"]], 
"07.05.2020": [["0", "1"], ["1", "2"], ["3", "3"]], 
"08.05.2020": [["2", "3"], ["3", "4"], ["3", "1"]], 
"09.05.2020": [["3", "1"], ["5", "3"], ["6", "2"]], 
"11.05.2020": [["8", "1"], ["9", "2"], ["10", "3"]]}

Результаты:
C:\Python37\python.exe F:/Работа/фриланс/ежедневник_стек/daily_planner.pyw
Filename: F:/Работа/фриланс/ежедневник_стек/daily_planner.pyw

Line #    Mem usage    Increment   Line Contents
================================================
    22     29.2 MiB     29.2 MiB       @profile
    23                                 def get_tasks(self):
    24     29.2 MiB      0.0 MiB           return self.tasks_for_current_day


Filename: F:/Работа/фриланс/ежедневник_стек/daily_planner.pyw

Line #    Mem usage    Increment   Line Contents
================================================
   150     29.1 MiB     29.1 MiB       @profile
   151                                 def set_new_daily(self):
   152     29.1 MiB      0.0 MiB           try:
   153     29.1 MiB      0.0 MiB               with open('Daily.json', 'r', encoding='utf-8') as daily_book:
   154     29.1 MiB      0.0 MiB                   self.load_data = json.load(daily_book)
   155                                     except IOError:
   156                                         self.update_load_data()
   157     29.1 MiB      0.0 MiB           daily_key = self.task_date.date().toPyDate().strftime('%d.%m.%Y')
   158     29.1 MiB      0.0 MiB           daily_value = list(self.current_daily.tasks_for_current_day)
   159     29.1 MiB      0.0 MiB           if daily_key in self.load_data.keys():
   160     29.1 MiB      0.0 MiB               self.current_daily = DailyStack()
   161     29.1 MiB      0.0 MiB               self.current_daily.tasks_for_current_day = deque(self.load_data[daily_key])
   162                                     else:
   163                                         self.load_data.setdefault(daily_key, daily_value)
   164                                         self.current_daily = DailyStack()
   165     29.2 MiB      0.1 MiB           self.rewrite_table()
   166     29.2 MiB      0.0 MiB           with open('Daily.json', 'w', encoding='utf-8') as daily_book:
   167     29.2 MiB      0.0 MiB               json.dump(self.load_data, daily_book)


Filename: F:/Работа/фриланс/ежедневник_стек/daily_planner.pyw

Line #    Mem usage    Increment   Line Contents
================================================
    26     36.8 MiB     36.8 MiB       @profile
    27                                 def sort_stack(self):
    28     36.8 MiB      0.0 MiB           while self.tasks_for_current_day:
    29     36.8 MiB      0.0 MiB               next_elem = self.tasks_for_current_day.pop()
    30     36.8 MiB      0.0 MiB               while self.temp_stack and int(self.temp_stack[-1][0]) > int(next_elem[0]):
    31     36.8 MiB      0.0 MiB                   self.tasks_for_current_day.append(self.temp_stack.pop())
    32     36.8 MiB      0.0 MiB               self.temp_stack.append(next_elem)
    33     36.8 MiB      0.0 MiB           while self.temp_stack:
    34     36.8 MiB      0.0 MiB               self.tasks_for_current_day.append(self.temp_stack.popleft())


Filename: F:/Работа/фриланс/ежедневник_стек/daily_planner.pyw

Line #    Mem usage    Increment   Line Contents
================================================
    22     36.8 MiB     36.8 MiB       @profile
    23                                 def get_tasks(self):
    24     36.8 MiB      0.0 MiB           return self.tasks_for_current_day


Filename: F:/Работа/фриланс/ежедневник_стек/daily_planner.pyw

Line #    Mem usage    Increment   Line Contents
================================================
   143     36.8 MiB     36.8 MiB       @profile
   144                                 def update_load_data(self):
   145                                     self.load_data[self.task_date.date().toPyDate().strftime('%d.%m.%Y')] = \
   146     36.8 MiB      0.0 MiB               list(self.current_daily.tasks_for_current_day)
   147     36.8 MiB      0.0 MiB           with open('Daily.json', 'w', encoding='utf-8') as daily_book:
   148     36.8 MiB      0.0 MiB               json.dump(self.load_data, daily_book)

   Таким образом, получается, что мое приложение потребляет немного памяти, при этом методы
   дополнительного прироста потребляемой памяти не дают. Вывод - программа эффективна.
"""
