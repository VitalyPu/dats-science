
# ------------------------------------7-----------------------------
'''
Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные
о фирме: название, форма собственности, выручка, издержки.

Пример строки файла:
firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл,
вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка:

[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''

import json

profit_dict = {}
aver_dict = {}

cnt = 0
aver = 0
prof = 0

with open('task7_file1.txt', 'r') as my_file:
    for line in my_file:
        comp_name, ownership_type, income, outcome = line.split()
        profit_dict[comp_name] = int(income) - int(outcome)

        if profit_dict.setdefault(comp_name) >= 0:
            prof = prof + profit_dict.setdefault(comp_name)
            cnt += 1

    if cnt != 0:
        aver = prof / cnt
        print('Cредняя прибыль по всем компаниям: ', round(aver))
    else:
        print('Все работают в убыток, среднюю прибыль не считаем')

    aver_dict = {'average_profit': round(aver)}
    profit_dict.update(aver_dict)

    print('--------------------- \n Прибыль по компаниям: \n', profit_dict)


with open('task7_file2.json', 'w') as json_file:
    json.dump(profit_dict, json_file)

    js_string = json.dumps(profit_dict)
    print('Создан файл "task7_file2.json": \n --------------------- \n', js_string)