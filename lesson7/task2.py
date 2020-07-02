# Урок 7
# Задание 2

'''
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
'''


class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_square_coat(self):
        return (f'Предварительная площадь на coat: {round(self.size / 6.5 + 0.5, 1)}')

    def get_square_jacket(self):
        return (f'Предварительная площадь на jacket: {round(self.height * 2 + 0.3, 1)}')

    @property
    def get_square_all(self):
        return str(f'Необходимая площадь ткани, общая: {round((self.size / 6.5 + 0.5) + (self.height * 2 + 0.3), 1)}')


class ClothesCoat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_coat = round(self.size / 6.5 + 0.5, 1)

    def __str__(self):
        return f'Итоговая площадь на coat: {self.square_coat}'


class ClothesJacket(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_jacket = round(self.height * 2 + 0.3, 1)

    def __str__(self):
        return f'Итоговая площадь на jacket: {self.square_jacket}'


# Ввод данных
context = input('Введите какая одежда должна быть сшита. 1 - Jacket, 2 - Coat: ')
size = int(input('Введите какой размер у одежды: '))
height = int(input('Введите какая длина у одежды: '))
print('------------------------')

# Вызов и вывод данных
print('Считаем сколько ткани нужно: \n------------------------')
if (int(context) == 1):
    jacket = ClothesJacket(size, height)
    print(jacket)
    print(jacket.get_square_jacket())
    print(jacket.get_square_all)

elif (int(context) == 2):

    coat = ClothesCoat(size, height)
    print(coat)
    print(coat.get_square_coat())
    print(coat.get_square_all)
else:
    print('Вы ввели пока несуществующий тип одежды, перезапустите программу снова')

print('------------------------')