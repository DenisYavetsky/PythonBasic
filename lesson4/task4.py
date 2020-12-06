# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

import random


def generate_random_list():
    return [random.randint(1, 21) for _ in range(50)]


def modify(example_list):
    return [i for i in example_list if example_list.count(i) < 2]


example_list = generate_random_list()

print(example_list)
print(modify(example_list))


assert modify([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]) == [23, 1, 3, 10, 4, 11]