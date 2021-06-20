#4.Реализуйте базовый класс Car.
#у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def drivin(self, go_on):
        self.go_on = go_on
        print(f'{self.name} едет {go_on}')

    def turning_right(self, turn_right='направо'):
        print(f'{self.name} едет {self.go_on} и повернула {turn_right}')

    def speed_on(self, show_speed):
        print(f'Скорость {self.name} составляет {show_speed}')

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(self, speed, color, name)
        if speed > 60:
            print(f'{self.name} едет со скоростью {self.speed} и превышает допустимую 60')

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(self, speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(self, speed, color, name)
        if speed > 40:
            print(f'Внимание! {self.name} едет со скоростью {speed} и превышает допустимую 40')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        is_police = True
        super().__init__(self, speed, color, name)

auto_sport = SportCar(60,'Sport car','black')
auto_sport.drivin('вперед')
auto_sport.turning_right()
auto_sport.speed_on(80)

auto_workcar = WorkCar(55, 'Work car','yellow')
auto_workcar.drivin('вперед')
auto_workcar.turning_right()




