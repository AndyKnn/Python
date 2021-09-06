# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class Complex:

    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary

    def __str__(self):
        return f'{self.real} + i{self.imag}' if self.imag >= 0 else f'{self.real} - i{abs(self.imag)}'

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)


c1 = Complex(1, 1)
c2 = Complex(2, -4)
print(f'c1 = {c1}, c2 = {c2}')
print(f'c1 + c2 = {c1 + c2}')
print(f'c1 * c2 = {c1 * c2}')
