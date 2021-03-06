# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'

    # Тут вопрос. Если я вызываю этот метод из дочерних классов то все ок. Но если вызвать из родителя то все падает.
    # Как сделать корректнее??? чтобы оставить метод get_square в классе clothes. Можно конечно повесить исключения, но
    # вопрос именно в корректности
    @property
    def get_square(self):
        if self.type == 'coat':
            sq = self.v / 6.5 + 0.5
        elif self.type == 'costume':
            sq = 2 * self.h + 0.3
        else:
            return None
        return f'Расход ткани {round(sq, 2)} ед'


class Coat(Clothes):
    def __init__(self, name, v):
        Clothes.__init__(self, name)
        self.type = 'coat'
        self.v = v

    def __str__(self):
        return f'{self.name}, {self.type}'


class Costume(Clothes):
    def __init__(self, name, h):
        Clothes.__init__(self, name)
        self.type = 'costume'
        self.h = h

    def __str__(self):
        return f'{self.name}, {self.type}'


c = Coat('Пальто', 50)
c1 = Costume('Костюм', 180)

print(c.get_square)
print(c1.get_square)