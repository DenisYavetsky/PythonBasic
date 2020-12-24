# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый,
# зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.

import time


class TrafficLight:

    def __init__(self):
        self.__color = 'RED'

    def change_state(self):
        ''' меняет состояние '''
        if self.__color == 'RED':
            print(self.__color)
            time.sleep(7)
            self.blinking('RED')

        self.__color = 'YELLOW'
        print(self.__color)

        time.sleep(2)
        if self.__color == 'YELLOW':
            self.__color = 'GREEN'

        if self.__color == 'GREEN':
            print(self.__color)
            time.sleep(5)
            self.blinking('GREEN')

    def blinking(self, color):
        ''' мигает пре смене состояния '''
        count = 0
        while count < 5:
            self.__color = color if self.__color == '' else ''
            print(self.__color)
            time.sleep(0.5)
            count += 1


c = TrafficLight()
# Red -> blinking-Red -> Yellow -> Green -> blinking Green -> off
c.change_state()




