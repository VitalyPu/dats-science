# Урок 8
# Задание: Игра Лото

'''
== Лото ==

Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны.

Пример карточки:
--------------------------
__  9 43 62 __ __ __ 74 90
 2 __ 27 __ 75 78 __ 82 __
__ 41 56 63 __ 76 __ 86 __
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
'''

import random

class Card:
    def __init__(self, name):
        self.name = name  # Название карточки (для вывода в командную строку).
        self.number_of_values = 15  # Количество полей, которые не будут вычеркнуты.
        self.matrix = []
        # Будущая карточка для игры в лото.

        # Заполняем карточку нулями на месте будущих номеров. Пустые поля остаются со значением None.
        for row in range(0, 3):
            self.matrix.append([None for column in range(0, 9)])

        # Флаг наличия строк с 6 числами. Изначально True для выполнения while.
        six_numbers_in_row = True

        # В каждый из первых шести столбцов добавляется по две позиции (значение 0).
        while six_numbers_in_row:
            self.clear()

            for column in range(0, 6):
                place_for_none = random.randint(0, 2)  # Выбираем позицию, которую оставим нетронутой.

                for row in range(0, 3):
                    if row != place_for_none:
                        self.matrix[row][column] = 0

            six_numbers_in_row = False

            for row in self.matrix:
                if row.count(0) == 6:
                    six_numbers_in_row = True
                    break

        # В последние три столбца добавляется по одному числу (значение 0).
        for column in range(6, 9):
            six_numbers_in_row = True

            while six_numbers_in_row:
                place_for_0 = random.randint(0, 2)

                if self.matrix[place_for_0].count(0) < 5:  # В строку можно добавить число.
                    six_numbers_in_row = False
                    self.matrix[place_for_0][column] = 0

        # Перемешиваем столбцы матрицы.
        for column in range(0, 9):
            new_position = random.randint(0, 8)

            for row in range(0, 3):
                buf = self.matrix[row][column]
                self.matrix[row][column] = self.matrix[row][new_position]
                self.matrix[row][new_position] = buf

        # Позиции для матрицы сгенерированы, заполняем матрицу числами.
        for row in range(0, 3):

            for column in range(0, 9):
                if self.matrix[row][column] == 0:
                    duplicate_detected = True

                    while duplicate_detected:
                        new_value = column * 10 + random.randint(1, 10)

                        # избавляемся от дубликатов в матрице
                        if not [self.matrix[0][column], self.matrix[1][column], self.matrix[2][column]].count(new_value):
                            duplicate_detected = False
                            self.matrix[row][column] = new_value
        # Карточка готова.

    def clear(self):
        # Очистка карточки.

        for row in range(0, 3):
            for column in range(0, 9):
                self.matrix[row][column] = None

    @property
    def is_empty(self):
        # Возвращает True, если из карточки вычеркнуты все цифры.
        return not self.number_of_values

    def output(self):
        # Форматированный вывод карточки с названием.
        title = ' ' + self.name + ' '
        if len(title) <= 24:
            print(title.center(26, '-'))
        else:
            print('-' * 26)

        for y in self.matrix:
            string = ''
            for x in y:
                if not x:
                    string += '   '
                elif x == -1:
                    string += ' - '
                else:
                    string += '{:>2} '.format(str(x))
            print(string)
        print('-' * 26)

    def find(self, value):
        # Возвращает True, если в карточке есть число value, иначе возвращает False.
        for row in self.matrix:
            if row.count(value):
                return True
        return False

    def cross_out(self, value):
        # Вычёркивает значение value из карточки и возвращает его (вычеркнутый элемент заменяется на -1).
        # Если такого значения нет, возвращает None.

        for row in range(0, 3):
            for column in range(0, 9):
                if self.matrix[row][column] == value:
                    self.matrix[row][column] = -1
                    self.number_of_values -= 1
                    return value
        return None


class PouchOfBarrels:
    # Мешочек с бочонками реализовал в виде класса. Знаю, что проще сделать списком,
    # но мне хотелось поэкспериментировать с итератором.

    def __init__(self):
        self.array = list(range(1, 91))  # Список с бочонками.

    @property
    def left(self):
        # Количество оставшихся в мешке бочонков.
        return len(self.array)

    def __iter__(self):
        return self

    def __next__(self):
        # Получение каждого нового значения изымает его из списка.
        if len(self.array):
            return self.array.pop(random.randint(0, len(self.array) - 1))
        raise StopIteration


last_comp_move = False  # Компьютеру даётся право последнего хода, поэтому возможна ничья (False - ничья невозможна).
mistake_chance = 0.7  # Шанс (в процентах), что компьютер сделает неправильный ход (0 - компьютер не ошибается).

# Создаём карточки.
player_card = Card('Ваша карточка')
comp_card = Card('Карточка компьютера')

# Создаём мешочек с бочонками.
barrels = PouchOfBarrels()

print('---Игра начинается---')

# Установка служебных флагов.
player_loss = False  # Флаг поражения игрока.
draw_flag = False  # Флаг ничьи.

for new_barrel in barrels:
    print('\nНовый бочонок: {} (осталось {})'.format(new_barrel, barrels.left))
    player_card.output()
    comp_card.output()

    # Ход игрока.
    if input('Зачеркнуть цифру? (y/n) ') == 'y':
        if player_card.cross_out(new_barrel):
            print('Число {} вычеркнуто из вашей карточки.'.format(new_barrel))
            if player_card.is_empty and not last_comp_move:
                # Игрок побеждает, и компьютеру не даётся право последнего хода.
                break
        else:
            print('Ошибка! Числа {} нет в вашей карточке.'.format(new_barrel))
            player_loss = True
            if not last_comp_move:
                # Игрок ошибается, и компьютеру не даётся право последнего хода.
                break
    else:
        if player_card.find(new_barrel):
            # Игрок пропустил число.
            print('Ошибка! В вашей карточке есть число {}.'.format(new_barrel))
            player_loss = True
            if not last_comp_move:
                # У компьютера нет права последнего хода.
                break

    #Ход компьютера.
    if mistake_chance and random.uniform(0, 99) < mistake_chance:
        # Компьютер совершает ошибку.
        print('Компьютер ошибся! В его карточке {} {}'.format('есть число' if comp_card.find(new_barrel) else 'нет числа', new_barrel))
        if player_loss:
            # Оба игрока ошиблись - ничья.
            draw_flag = True
        # Победитель зависит от значения флагов draw_flag и player_loss.
        break
    else:
        # Компьютер не совершил ошибки.
        if comp_card.cross_out(new_barrel):
            print('Компьютер вычёркивает число {} из своей карточки.'.format(new_barrel))

    if player_card.is_empty and comp_card.is_empty:
        # Если обе карточки пусты - объявляется ничья.
        draw_flag = True
        break
    if player_card.is_empty:
        # Игрок выиграл.
        break
    if comp_card.is_empty:
        # Игрок проиграл.
        player_loss = True
        break
    if player_loss:
        # Игрок проиграл, и у компьютера было право последнего хода, но он не ошибся.
        break

if draw_flag:
    print('Ничья!')
elif player_loss:
    print('Вы проиграли!')
else:
    print('Вы выиграли!')

print('---Конец игры---')

# Честно пишу, что нашел решение из интернета, но без ООП, т.к. сам мучился 8+ часов и не смог написать код. Задание обьективно очень сложное. Не надо давать такие на уроках, пожалуйста. ОЧЕНЬ СЛОЖНО.
# Я новичок и без проблем делал предыдущие задания на 10 баллов каждое, но на это угробил 8+ часов в сумме и от бессилия просто загуглил решение, после чего еще 4 часа разбирался как работает код и переписывал на ООП. На это угробил почти все выходные. Это бесчеловечно давать такие сложные задания.
# Также полностью осознал решение, чтобы совсем небыло скучно, усложнил задание до варианта, когда компьютер может проиграть, т.е. добавил параметр со сложностю игры. Теперь полноценная игра в лото, в которую компьютер тоже может проиграть.
