# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, date: str):
        # date format «день-месяц-год»
        self.date = date


    @classmethod
    def get_date_numbers(cls, date):
        numbers = [int(n) for n in date.split('-')]
        return numbers

    @staticmethod
    def date_validation(day, month, year):
        vis = False
        correct = True
        # определение високосного года
        if year in range(1600, 2100):
            if year % 4 == 0:
                vis = True
                if year % 100 == 0 and year % 400 != 0:
                    vis = False
        else:
            correct = False

        days31 = [1, 3, 5, 7, 8, 10, 12]

        if month in range(1, 13):
            if month == 2:
                if vis:
                    if day not in range(1, 30):
                        correct = False
                else:
                    if day not in range(1, 29):
                        correct = False
            else:
                if month in days31:
                    if day not in range(1, 32):
                        correct = False
                else:
                    if day not in range(1, 31):
                        correct = False
        else:
            correct = False

        return correct


a = Data('18-12-2020')
print(Data.get_date_numbers(a.date))
print(a.date_validation(18, 12, 2020))

b = Data('17-4-2010')
print(Data.get_date_numbers(a.date))
print(b.date_validation(17, 4, 2010))

c = Data('31-2-2011')
print(Data.get_date_numbers(a.date))
print(c.date_validation(31, 2, 2011))