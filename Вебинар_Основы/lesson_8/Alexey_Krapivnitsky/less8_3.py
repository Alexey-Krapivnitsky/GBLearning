class CheckTypeError(ValueError):
    pass


class CheckList:

    result = []

    @classmethod
    def check_val(cls, val):
        try:
            float(val)
        except ValueError:
            raise CheckTypeError('Введена строка или буква, необходимо вводить число')
        else:
            cls.result.append(val)


if __name__ == '__main__':
    while True:
        user_val = input('Введите значение: ')
        if user_val == 'stop':
            print(CheckList.result)
            break
        else:
            try:
                interim_val = CheckList.check_val(user_val)
            except CheckTypeError as e:
                print(f'Ошибка ввода: {e}')
