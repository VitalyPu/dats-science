# Урок 1
# Задание 2
"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды
и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

# Комментарий: Первый вариант (он красивый, поэтому оставил, да не совсем соотвествует заданию)
raw_seconds = int(input('Введите количество секунд: ', ))
print(f'Время: {int(raw_seconds // 3600)}:{int((raw_seconds // 60) % 60)}:{int(raw_seconds % 60 )}')

# Комментарий: Второй вариант с форматом чч:мм:cc с добавлением нулей для вывода правильного формата
raw_seconds = int(input('Введите количество секунд: ', ))
my_hours = int(raw_seconds // 3600)
my_minutes = int((raw_seconds // 60) % 60)
my_seconds = int(raw_seconds % 60 )
if my_seconds < 10:
    my_seconds = str('0' + str(my_seconds))
if my_minutes < 10:
    my_minutes = str('0' + str(my_minutes))
if my_hours < 10:
    my_hours = str('0' + str(my_hours))
print(f'Время: {my_hours}:{my_minutes}:{my_seconds} ')