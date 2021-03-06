# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
# массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины
# полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.__m_one_sqaure_meter = 25
        self.__height_one_sqaure_meter = 5

    def massa(self):
        '''расчет массы'''
        return self._length * self._width * self.__m_one_sqaure_meter * self.__height_one_sqaure_meter / 1000


r = Road(40, 5000)
print(r.massa())

