# Урок 1, задание 5
# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите
# численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

cash = int(input('Введите значение выручки\n'))
cost = int(input('Введите значение издержек\n'))

dif = cash - cost
if dif > 0:
    print('Фирма работает с прибылью в размере: ' + str(dif))
    print('Рентабельность в размере: ' + str(dif / cash))
    peoples = int(input('Сколько сотрудников в комании?\n'))
    print('Прибыль фирмы в расчете на одного сотрудника: ' + str(dif / peoples))
else:
    print('Фирма работает с убытком в размере: ' + str(dif))