# Урок 6
# Задание 5

'''
Реализовать класс Stationery (канцелярская принадлежность).

Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).

В каждом из классов реализовать переопределение метода draw.

Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'



class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Мы рисуем {self.title}. Запуск отрисовки Ручкой!'



class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Мы рисуем {self.title}. Запуск отрисовки Карандашом!'



class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Мы рисуем {self.title}. Запуск отрисовки Маркером!'

paint_type = input('Напишите, что хотите нарисовать: ').title()
print('-----Старт-----')

pen_print = Pen(paint_type)
print(pen_print.draw())

pencil_print = Pencil(paint_type)
print(pencil_print.draw())

handle_print = Handle(paint_type)
print(handle_print.draw())

print('-----Конец-----')