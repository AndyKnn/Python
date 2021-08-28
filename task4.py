# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
# color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны
# сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних
# классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    speed: float
    color: str
    name: str
    is_police: bool

    def go(self):
        return print('Поехали')

    def stop(self):
        return print('Стоп')

    def turn(self, direction):
        self.direction = direction
        return self.direction

    def show_speed(self, speed):
        self.speed = speed
        print(self.speed)


class PoliceCar(Car):
    is_police = True
    name = 'FORD'
    color = 'White and black'
    speed = 100.0


class TownCar(Car):
    is_police = False
    name = "BMW"
    color = "Black"
    speed: float

    def show_speed(self, speed):
        self.speed = speed
        if self.speed > 60:
            print(f"Превышение скорости!! Автомобиль: {TownCar.name} движется со скоростью {self.speed} км в час")
        print(f"Скорость движения {TownCar.name}: {self.speed} км в час")


class WorkCar(Car):
    is_police = False
    name = 'Kamaz'
    color = 'Orange'
    speed: float

    def show_speed(self, speed):
        self.speed = speed
        if self.speed > 40.0:
            print(f"Превышение скорости!!  Автомобиль: {WorkCar.name} движется со скоростью {self.speed} км в час")
        else:
            print(f"Скорость автомобиля {WorkCar.name}: {self.speed} км в час")


class SportCar(Car):
    is_police = False
    name = 'Ferrari'
    color = 'Red'
    speed = 180.0


tc = TownCar()
pc = PoliceCar()
sc = SportCar()
wc = WorkCar()

pc.go()
print(f"Автомобиль: {wc.name}, цвет: {wc.color}, направление движения: {wc.turn(direction='left')}")
print(f"{pc.name} полицейский автомобиль? (True/False): {pc.is_police}")
wc.show_speed(speed=80)
tc.stop()
