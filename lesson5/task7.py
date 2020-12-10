# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
import json

with open('files/file7.txt', 'r', encoding='UTF-8') as f:
    companies = []
    company_plus = {}
    company_minus = {}
    average_profit = {}
    sum_profit = 0
    for line in f.readlines():
        company = line.split()
        # определяем компании с прибылью
        if int(company[2]) > int(company[3]):
            profit = int(company[2]) - int(company[3])
            sum_profit += profit
            company_plus[company[0]] = profit
        else:
            company_minus[company[0]] = int(company[2]) - int(company[3])

    average_profit['average_profit'] = sum_profit
    companies.append(company_plus)
    companies.append(company_minus)
    companies.append(average_profit)

with open('files/file7.json', 'w', encoding='UTF-8') as json_file:
    json.dump(companies, json_file, ensure_ascii=False)


