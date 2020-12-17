# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, m):
        self.m = m

    @staticmethod
    def __check_dimension(m1, m2):
        ''' проверяет размерность матириц при сложении '''
        if len(m1) == len(m2):
            for i, m in enumerate(m1):
                if len(m) != len(m2[i]):
                    return False
            return True
        else:
            return False

    def __str__(self):
        new_str = ''
        for row in self.m:
            for el in row:
                new_str += str(el) + ' '
            new_str += '\n'
        return f'{new_str}'

    def __add__(self, other):
        if Matrix.__check_dimension(self.m, other.m):
            res = []
            c = []
            for i, row in enumerate(self.m):
                c = [x + y for x, y in zip(row, other.m[i])]
                res.append(c)
            Matrix(res)
            return Matrix(res)
        else:
            print('Размерность матриц не совпадает')


#matr = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
# или
matr1 = [[x+3*y for x in range(1, 4)] for y in range(0, 3)]
matr2 = [[4*x+3*y for x in range(1, 3)] for y in range(0, 3)]
matr3 = [[x+3*y for x in range(1, 4)] for y in range(0, 3)]

m1 = Matrix(matr1)
m2 = Matrix(matr2)
m3 = Matrix(matr3)

print(m1)
print(m2)
print(m3)

m = m1 + m3
print(m)