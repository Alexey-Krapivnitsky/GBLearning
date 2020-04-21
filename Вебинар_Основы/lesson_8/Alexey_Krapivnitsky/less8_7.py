class ComplexNumber:
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
        result = f'{result_real} + {result_imaginary}i' if result_imaginary > 0\
            else f'{result_real} - {abs(result_imaginary)}i'
        return result

    def __mul__(self, other):
        result_real = self.real * other.real - self.imaginary * other.imaginary
        result_imaginary = self.real*other.imaginary + self.imaginary * other.real
        result = f'{result_real} + {result_imaginary}i' if result_imaginary > 0 \
            else f'{result_real} - {abs(result_imaginary)}i'
        return result


if __name__ == '__main__':
    complex_1 = ComplexNumber(5, 2)
    complex_2 = ComplexNumber(-4, 7)
    print(f'Число 1: {complex_1}\nЧисло 2: {complex_2}')

    complex_3 = complex_1 + complex_2
    print(f'Результат сложения: {complex_3}')

    complex_4 = complex_1 * complex_2
    print(f'Результат умножения: {complex_4}')
