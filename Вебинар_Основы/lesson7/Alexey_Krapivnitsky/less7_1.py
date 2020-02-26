class Matrix:

    def __init__(self, inp_matrix=None):
        self.matrix = inp_matrix

    def __str__(self):
        out_matrix = '\n'.join(str(line).strip('[]') for line in self.matrix)
        return f'{out_matrix}\n' if out_matrix else 'Отсутствует матрица'

    def __add__(self, other):
        if self.check_matrix(self.matrix, other.matrix):
            result = [list(map(lambda x, y: x + y, el[0], el[1])) for el in zip(self.matrix, other.matrix)]
            return Matrix(result)
        else:
            print('Матрицы разной размерности складывать нельзя!')
            return Matrix([])

    @staticmethod
    def check_matrix(m1, m2):
        my_check = 0
        if len(m1) == len(m2):
            for i in range(len(m1) - 1):
                if len(m1[i]) != len(m2[i]):
                    my_check += 1
        else:
            my_check += 1

        check_status = False if my_check else True

        return check_status


if __name__ == '__main__':

    matrix_A = [
        [1, 1, 1, ],
        [2, 2, 2, ],
        [3, 3, 3, ],
    ]
    matrix_B = [
        [4, 4, 4, ],
        [5, 5, 5, ],
        [6, 6, 6, ]
    ]
    matrix_C = [
        [4, 4, ],
        [5, 5, 5, ],
    ]

    matrix_1 = Matrix(matrix_A)
    matrix_2 = Matrix(matrix_B)

    print(matrix_1)
    print(matrix_2)

    matrix_3 = matrix_1 + matrix_2
    print(matrix_3)

    matrix_4 = matrix_3 + matrix_2
    print(matrix_4)

    matrix_5 = Matrix(matrix_C)
    print(matrix_5)

    matrix_6 = matrix_5 + matrix_2
    print(matrix_6)
