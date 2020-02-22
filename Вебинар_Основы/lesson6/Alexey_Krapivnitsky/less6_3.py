class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage=0, bonus=0):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Employee {self.name} {self.surname}')

    def get_total_income(self):
        total_income = sum(self._income.values())
        return total_income


if __name__ == '__main__':

    worker_1 = Position('Ivan', 'Ivanov', 'manager', 25000, 5500)
    worker_2 = Position('John', 'Robinson', 'engineer', 53000)
    worker_3 = Position('Alexander', 'Schliemann', 'gastarbaiter')

    print(worker_1.name, worker_1.surname, worker_1.position)
    print(worker_2.name, worker_2.surname, worker_2.position)
    print(worker_3.name, worker_3.surname, worker_3.position)

    worker_1.get_full_name()
    salary1 = worker_1.get_total_income()
    print(salary1)

    worker_2.get_full_name()
    salary2 = worker_2.get_total_income()
    print(salary2)

    worker_3.get_full_name()
    salary3 = worker_3.get_total_income()
    print(salary3)
