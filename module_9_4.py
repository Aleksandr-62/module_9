import random                # Для метода __call__. Для случайного выбора с одинаковой вероятностью для каждого 
from random import choice    # данного в коллекции можете использовать функцию choice из модуля random

#   Lambda-функция
#   Даны 2 строки:

first = 'Мама мыла раму'
second = 'Рамена мало было'

#   Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
#   Здесь ? - место написания lambda-функции.

print(list(map(lambda x, y: x == y, first, second)))

#   Результатом должен быть список совпадения букв в той же позиции:
#   [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
#   Где True - совпало, False - не совпало.


#   Замыкание:
#   Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
#   Внутри этой функции, напишите ещё одну - write_everything(*data_set), где *data_set - параметр принимающий
#   неограниченное количество данных любого типа.
#   Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf8') as file:
            for data in data_set:
                file.write(str(data) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


#   Метод __call__:
#   Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
class MysticBall:
    def __init__(self, *words):
        self.words = words

#   В этом классе также определите метод __call__
#   который будет случайным образом выбирать слово из words и возвращать его
    def __call__(self):
        return random.choice(self.words)


# Вывод результата
first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Странно')
print(first_ball())
print(first_ball())
print(first_ball())
