# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123]


import random


def generate_random_list():
    return [random.randint(1, 101) for _ in range(20)]


def modify(example_list):
    new_list = []
    for i, a in enumerate(example_list[1:]):
        if a > example_list[i]:
            new_list.append(a)
    return new_list


example_list = generate_random_list()

print(example_list)
print(modify(example_list))


assert modify([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]) == [12, 44, 4, 10, 78, 123]

