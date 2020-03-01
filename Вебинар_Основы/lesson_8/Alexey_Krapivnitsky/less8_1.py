import re


class MyDate:
    int_date = 0
    int_month = 0
    int_year = 0

    def __init__(self, user_date):
        self.my_date = user_date

    def __str__(self):
        return f'Input date - {self.my_date}, date - {self.int_date}, month - {self.int_month}, year - {self.int_year}'

    @property
    def my_date(self):
        return self.__date if self.__date else f'Date is not valid'

    @my_date.setter
    def my_date(self, user_date):
        self.__date = self.validate_date(user_date)

    @classmethod
    def transform_to_number(cls, user_date):
        valid_date = cls.validate_date(user_date)
        cls.int_date, cls.int_month, cls.int_year = list(map(int, valid_date.split('-')))if valid_date else [0, 0, 0]
        return cls(user_date)

    @staticmethod
    def validate_date(user_date):
        date_template = re.compile(r'^[0-3][0-9]-[01][0-9]-[12][09][0-9][0-9]$')
        if date_template.search(user_date):
            return user_date
        else:
            return None


if __name__ == '__main__':
    date_1 = MyDate('11-01-2019')
    print(date_1, '\n')
    date_2 = MyDate('11.01.2019')
    print(date_2, '\n')
    date_3 = MyDate.transform_to_number('12-02-2020')
    print(date_3, '\n')
    date_4 = MyDate.transform_to_number('22/02/2020')
    print(date_4, '\n')
