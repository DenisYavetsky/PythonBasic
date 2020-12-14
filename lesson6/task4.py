# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
# выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return (f'{self.name} едет со скоростью {self.speed}км/ч')

    def stop(self):
        return (f'{self.name} остановилась. Скорость 0 км/ч')

    def turn(self, direction):
        return (f'{self.name} повернула на{direction}')

    def show_speed(self):
        return (f'Скорость {self.name} равна {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)
        self.max_speed = 60

    def show_speed(self):
        if self.speed < self.max_speed:
            return (f'Скорость {self.name} равна {self.speed}. Превышения нет')
        else:
            return (f'Скорость {self.name} равна {self.speed}. Превышение !!!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)
        self.max_speed = 100

    def show_speed(self):
        if self.speed < self.max_speed:
            return (f'Скорость {self.name} равна {self.speed}. Превышения нет')
        else:
            return (f'Скорость {self.name} равна {self.speed}. Превышение !!!')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)
        self.max_speed = 40

    def show_speed(self):
        if self.speed < self.max_speed:
            return (f'Скорость {self.name} равна {self.speed}. Превышения нет')
        else:
            return (f'Скорость {self.name} равна {self.speed}. Превышение !!!')


class PoliceCar(Car):
    pass


a = TownCar(55, 'black', 'KIA', False)
print(a.go())
print(a.turn('лево'))
print(a.show_speed())
print(a.stop())

b = TownCar(65, 'red', 'OPEL', False)
print(b.go())
print(b.turn('право'))
print(b.show_speed())
print(b.stop())

c = WorkCar(55, 'orange', 'KAMAZ', False)
print(c.go())
print(c.turn('лево'))
print(c.show_speed())
print(c.stop())

d = SportCar(100, 'Yellow', 'ferrari', False)
print(d.go())
print(d.turn('лево'))
print(d.show_speed())
print(d.stop())

e = PoliceCar(200, 'blue', 'Octavia', True)
print(e.go())
print(e.turn('право'))
print(e.show_speed())
print(e.stop())