# Урок 6
# Задание 4

'''
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).

А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.

При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn_right(self):
        print(f'{self.name} повернула направо')

    def turn_left(self):
        print(f'{self.name} повернула налево')

    def show_speed(self):
        print(f'Скорость авто {self.name} составила {self.speed}')



class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского авто {self.name} составила {self.speed}')

        if (self.speed > 40):
            print(f'Скорость городской машины {self.name} выше, чем можно ездить в городе. Гоняешъ!')
        else:
            print(f'Скорость рабочей машины {self.name} в пределах городского режима')



class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость машины {self.name} составила {self.speed}')
        if (self.speed) > 60:
            print(f'Скорость рабочей машины {self.name} выше, чем разрешено в городе! Гоняешь!')
        else:
            print(f'Скорость рабочей машины {self.name} в пределах городского режима')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if (self.is_police == True):
            print(f'{self.name} полицейский авто')
        else:
            print(f'{self.name} не полицейский авто')



print('Введите параметры авто \n -------------------- ')
speed = int(input('Введите скорость авто: '))
color = input('Введите цвет авто: ')
name = input('Введите марку авто: ')
auto_type = input('введите тип авто: Спортивная - 1, Городская - 2, Рабочая - 3, Полицейская 4: ')


if (auto_type == '1'):
    auto = SportCar(speed, color, name, False)
elif (auto_type == '2'):
    auto = TownCar(speed, color, name, False)
elif (auto_type == '3'):
    auto = WorkCar(speed, color, name, False)
elif (auto_type == '4'):
    auto = PoliceCar(speed, color, name, True)
else:
    print('Ошибка! Нет такого типа авто')


print('------Инфо о машине----')
print('Марка авто: ', auto.name)
print('Цвет авто: ', auto.color)
print('Полицейский авто :', auto.is_police)
print(auto.show_speed())

print('------Поехали!----')
print(auto.go())
print(auto.show_speed())
print(auto.turn_left())
print(auto.stop())

print('------Проверка варнингов------')
auto = WorkCar(70, color, name, False) # для отладки
print(auto.show_speed()) # для отладки
auto = TownCar(50, color, name, False) # для отладки
print(auto.show_speed()) # для отладки

# Проблемка. Не понимаю, почему возвращается None.
# Можете пояснить откуда она в выводе?
# Всегда при вызове метода класса .auto.show_speed()
# Голову сломал :/