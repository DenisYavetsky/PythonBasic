# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class MyDivisionByZero(Exception):
    def __str__(self):
        return f'Нельзя делить на ноль'


try:
    first = int(input('Введите делимое: '))
    second = int(input('Введите делитель: '))
    if second == 0:
        raise MyDivisionByZero
    print(first/second)

except MyDivisionByZero as e:
    print(e)
