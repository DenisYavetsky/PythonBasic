# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
# уроках по ООП.


# отделы
departments = {'Кадры': [], 'Финансисты': [], 'Программисты': []}


class Warehouse:
    def __init__(self, destination: str, square: int, num_row: int, num_row_places: int):
        self.destination = destination
        # максимальное количество рядов и мест
        self.square = square
        self.num_row = num_row
        self.num_row_places = num_row_places
        self.equipment = {}

    def put_on_warehouse(self, equipment, row, place):
        if self.equipment.get(str(row) + '_' + str(place)):
            return f'Место зянято'
        # если помещаем технику из отдела на склад то удаляем ее из отдела
        for department in departments:
            for val in departments[department]:
                if val == equipment.name:
                    departments[department].pop()
        self.equipment[str(row) + '_' + str(place)] = equipment.name
        return f'Добавлен на склад на ряд {row} место {place}'

    def get_from_warehouse(self, row, place, department):
        if self.equipment.get(str(row) + '_' + str(place)):
            departments[department].append(self.equipment[str(row) + '_' + str(place)])
            # выдаем технику и удаляем ключ
            del(self.equipment[(str(row) + '_' + str(place))])
        else:
            return f'Место пусто'

    @property
    def get_warehouse_param(self):
        return f'Рядов {self.num_row}, мест в ряде {self.num_row_places}'

    @property
    def list_equipment_on_warehouse(self):
        return self.equipment


class OfficeEquipment:
    def __init__(self, name, inventory_number):
        self.inventory_number = inventory_number
        self.name = name

    def __str__(self):
        return f'{self.name}, {self.inventory_number}'

    @classmethod
    def list_departments_on_office(cls):
        return f'{departments}'


class Printer(OfficeEquipment):
    '''Принтер'''
    def __init__(self, print_type, max_format, name, inventory_number):
        if type(name) == str and type(inventory_number) == int and type(max_format) == str and type(print_type) == str:
            super().__init__(name, inventory_number)
            # тип печати: матричная, струйная, лазерная
            self.print_type = print_type
            # формат бумаги
            self.max_format = max_format
        else:
            print('Неверный тип переданных данных')


class Scanner(OfficeEquipment):
    '''Сканер'''
    def __init__(self, max_format, name, inventory_number):
        if type(name) == str and type(inventory_number) == int and type(max_format) == str:
            super().__init__(name, inventory_number)
            # формат бумаги
            self.max_format = max_format
        else:
            print('Неверный тип переданных данных')


class Xerox(OfficeEquipment):
    '''Ксерокс'''
    def __init__(self, connection_type, name, inventory_number):
        super().__init__(name, inventory_number)
        # wifi or ethernet
        self.connection_type = connection_type


# Проверяем работу
# Склад
a = Warehouse('Moscow', 15, 6, 15)

# Оргтехника
b = Printer('Matrix', 'A3', 'Принтер HP2300', 123)
c = Scanner('A3', 'Сканер HP222', 124)
d = Xerox('wi-fi', 'Epson-2000', 125)

# поместить на склад
a.put_on_warehouse(b, 5, 1)
a.put_on_warehouse(c, 5, 2)
a.put_on_warehouse(d, 5, 6)

# Список в отделах
print(departments)
# Список на складе
print(a.list_equipment_on_warehouse)

# Выдать со склада в отдел
a.get_from_warehouse(5, 1, 'Кадры')
a.get_from_warehouse(5, 2, 'Финансисты')

# Список в отделах
print(departments)
# Список на складе
print(a.list_equipment_on_warehouse)

# Забрать на склад из отдела
a.put_on_warehouse(c, 1, 2)

# Список в отделах
print(departments)
# Список на складе
print(a.list_equipment_on_warehouse)




