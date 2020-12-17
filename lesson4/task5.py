# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def generate_random_list():
    return [i for i in range(100, 1001) if i % 2 == 0]


def calculate(sum, el):
    return sum * el


l = generate_random_list()

print(reduce(calculate, l))