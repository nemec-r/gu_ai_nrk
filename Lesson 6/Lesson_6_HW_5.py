#5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title, draw):
        self.title = title
        self.draw = draw

    def draw_on(self):
        print(f'{self.title} с помощью {self.draw}')

class Pen(Stationery):
    def __init__(self, title='Пишем', draw='Pen'):
        super().__init__(title, draw)

class Pencil(Stationery):
    def __init__(self, title='Рисуем', draw='Pencil'):
        super().__init__(title, draw)

class Handle(Stationery):
    def __init__(self, title='Разукрашиваем', draw='Handle'):
        super().__init__(title, draw)

pen_1 = Pen()
pen_1.draw_on()

pencil_1 = Pencil()
pencil_1.draw_on()

handle_1 = Handle()
handle_1.draw_on()