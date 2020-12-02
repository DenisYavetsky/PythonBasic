#  Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
#  двух аргументов.


def my_func(a, b, c):
    if a > b:
        if b > c:
            return a + b
        else:
            return a + c
    else:
        if a < c:
            return b + c
        else:
            return a + b


my_func(
    int(input('аргумент 1')),
    int(input('аргумент 2')),
    int(input('аргумент 3')),
)

assert my_func(0, 20, 20) == 40
assert my_func(10, 20, 30) == 50
assert my_func(30, 10, 5) == 40
assert my_func(30, 50, 20) == 80
assert my_func(10, 10, 5) == 20
assert my_func(5, 10, 5) == 15
assert my_func(10, 10, 10) == 20
assert my_func(0, 0, 5) == 5
