# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные
# типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Storage:
    width: int
    length: int
    quantity_goods: int
    model: str
    max_volume_Storage: int

    def get_goods(self, quantity_goods=0, name_office_equipment='name_Office_equipment', model='model'):
        pass

    def to_info_of_goods(self):
        print('выдать инфу о товарах на складе')
        pass

    def output_goods(self):
        print('Выдать товары со склада')
        pass


class Office_equipment:
    def __init__(self, brand='manufacturer', name_equipment='принтер', model='model',
                 year_production=2021, guarantee=3, country_of_manufacture='China'):
        self.brand = brand
        self.name_equipment = name_equipment
        self.model = model
        self.year_production = year_production
        self.guarantee = guarantee
        self.country_of_manufacture = country_of_manufacture

    def __str__(self):
        return f"{self.brand} {self.name_equipment} {self.model} {self.year_production}"


class Printer(Office_equipment):
    def to_print(self, smth='smth'):
        return f'to print {smth}'

    pass


class Scanner(Office_equipment):
    def to_scan(self, smth='smth'):
        return f'to scan {smth}'

    pass


class Xerox(Office_equipment):
    def to_copier(self, smth='smth'):
        return f'to copier {smth}'

    pass


hp_laserjet = Printer()
kyocera_2040 = Scanner()
xerox = Xerox()
print(hp_laserjet)
print(hp_laserjet.to_print())
print(kyocera_2040.to_scan())
print(xerox.to_copier())
print(xerox.year_production)
