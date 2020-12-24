# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовк.'


class Pen(Stationery):
    def draw(self):
        return f'{self.title}, Запуск отрисовки.'


class Pencil(Stationery):
    def draw(self):
        return f'{self.title}, Запуск отрисовки.'


class Handle(Stationery):
    def draw(self):
        return f'{self.title}, Запуск отрисовки. '


a = Pen('Ручка')
b = Pencil('Карандаш')
c = Handle('Маркер')

print(f'{a.draw()}\n{b.draw()}\n{c.draw()}\n')