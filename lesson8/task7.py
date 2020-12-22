# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class MyComplex:
    def __init__(self, imaginary, real):
        self.imaginary = imaginary
        self.real = real

    def __add__(self, other):
        return MyComplex(self.imaginary + other.imaginary, self.real + other.real)

    def __mul__(self, other):
        return MyComplex(self.imaginary * other.imaginary - self.real * other.real, self.imaginary * other.real + self.real * other.imaginary)

    def __str__(self):
        return f'{self.imaginary} + {self.real}j'


a = MyComplex(2, 1)
b = MyComplex(3, 4)

print(a+b)
print(a*b)

