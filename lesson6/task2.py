# Урок 6
# Задание 2

'''
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.

Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.

Проверить работу метода

Например:
5000м * 20м * 25кг * 5см = 12500 т
'''

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

class RoadMass(Road): # Решил попробовать наследование
    def __init__(self, _length, _width, kilogram, thickness):
        super().__init__(_length, _width) # переопределение конструктора класса
        self.kilogram = kilogram
        self.thickness = thickness

    def mass(self):
        space = self._length * self._width * self.kilogram * self.thickness
        return space

m_lenght = int(input('Введите длину трассы в метрах: '))
m_width = int(input('Введите ширину трассы в метрах: '))
kg = int(input('Введите массу асфальта необходимого для покрытия одного кв метра дороги, в кг: '))
sm = int(input('Введите толщину итоговой трассы в см: '))

asphalt = RoadMass(m_lenght, m_width, kg, sm)
print('\n-------------------')
print(f'Итоговые параметры полотна: {round(asphalt.mass() / 1000)} т. ')