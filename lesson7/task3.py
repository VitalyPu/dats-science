# Урок 7
# Задание 3

'''
Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).

В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()),
вычитание (__sub__()),
умножение (__mul__()),
деление (__truediv__()).

Данные методы должны применяться только к клеткам и выполнять
увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток.
При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.

Метод должен возвращать строку вида *****\n*****\n*****...,
где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например,
количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.

Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.

Подсказка: подробный список операторов для перегрузки доступен по ссылке.
'''


class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        result = f'Итого:  {self.quantity * "*"}'
        return result

    def __add__(self, second_cell):
        result = Cell(self.quantity + second_cell.quantity)
        return result

    def __sub__(self, second_cell):
        if ((self.quantity - second_cell.quantity) > 0):
            result = self.quantity - second_cell.quantity
        else:
            result = 'Отрицательное значение, нельзя, ата-та!'
        return result

    def __mul__(self, second_cell):
        result = Cell(int(self.quantity * second_cell.quantity))
        return result

    def __truediv__(self, second_cell):
        result = Cell(round(self.quantity // second_cell.quantity))
        return result


    def make_order(self, row_cells):
        row_in_line = ''

        for i in range(int(self.quantity / row_cells)):
            row_in_line += f'{"*" * row_cells} \\n'

        row_in_line += f'{"*" * (self.quantity % row_cells)}'
        return row_in_line


print('----------------------Ввод данных--------------------------------------------')
num_cells1 = input('Введите количество * для первой строки: ')
num_cells2 = input('Введите количество * для второй строки: ')

print('----------------------Вывод данных-----------------------------------------')
cells1 = Cell(num_cells1)
cells2 = Cell(num_cells2)
print(cells1)
print(cells2)

print('------------------------Сумма клеток-----------------------------------')
print(cells1 + cells2)

print('------------------------Разность клеток-----------------------------------')
print(cells2 - cells1)
print(cells1 - cells2) # для отладки

print('------------------------Деление клеток-----------------------------------')
print(cells1 / cells2) # для отладки
print(cells2 / cells1)

print('--------------------------Проверка make order---------------------------------------')
divider = int(input('Введите по сколько разбивать клетки в строке: '))

print(cells1.make_order(divider))
print(cells2.make_order(divider))
print('--------------------------Конец ---------------------------------------')