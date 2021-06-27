# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# - Не решил
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, serial_num, brand="", model=""):
        self.serial_num = serial_num
        self.brand = brand
        self.model = model
        self.group = self.brand + " " + self.model

    def group_name(self):
        return f'{self.group}'

    def __radd__(self, other):
        if not isinstance(other, Product):
            return self
        return self + other

    def __str__(self):
        return f"Тип: {self.__class__.__name__} {self.brand} {self.model}, серийный номер: {self.serial_num}"

    @abstractmethod
    def do_some_work(self):
        pass


class Printer(Product):
    def __init__(self, serial_num, brand, model, print_method=''):
        super().__init__(serial_num, brand, model)
        self._print_method = print_method

    def __str__(self):
        return f"{self.brand} {self.model}. S/N {self.serial_num}"

    def do_some_work(self):
        print(f"{self.group} Printing a document")


class Scanner(Product):
    def __init__(self, serial_num, brand, model, scanning_speed, scan_format):
        super().__init__(serial_num, brand, model)
        self.scanning_speed = scanning_speed
        self.format_paper = scan_format

    def __str__(self):
        return f"{self.brand} {self.model}. S/N {self.serial_num}"

    def do_some_work(self):
        print(f"{self.group} Scanning")


class Copier(Product):
    def __init__(self, serial_num, brand, model, copy_speed):
        super().__init__(serial_num, brand, model)
        self.copy_speed = copy_speed

    def __str__(self):
        return f"{self.brand} {self.model}. S/N {self.serial_num}"

    def do_some_work(self):
        print(f"{self.group} Copying")


class Warehouse:
    dict_products = {'Printer': [], 'Scanner': [], 'Copier': []}
    department_products = {'Printer': [], 'Scanner': [], 'Copier': []}

    @classmethod
    def add(cls, *products, from_user=False):
        if not from_user:
            for product in products:
                cls.dict_products[str(product.__class__.__name__)].append(product)
                print(product, 'Получено на склад.')
        else:
            for product in products:
                cls.department_products[str(product.__class__.__name__)].remove(product)
                cls.dict_products[str(product.__class__.__name__)].append(product)
                print(product, 'Получено на склад.')

    @classmethod
    def rem_wh_add_dep(cls, product):
        cls.dict_products[str(product.__class__.__name__)].remove(product)
        cls.department_products[str(product.__class__.__name__)].append(product)
        print(product, 'Получен со склада.')

    def __str__(self):
        string = '\n'.join(map(str, sum(self.dict_products.values(), [])))
        string = 'Устройств на складе:\n' + string if string else 'На складе нет устройств'
        string_dep = '\n'.join(map(str, sum(self.department_products.values(), [])))
        string_dep = 'Устройств в департаменте:\n' + string_dep if string_dep else 'Устройств в департаменте:'
        return string + '\n' + string_dep


def main():
    printer_1 = Printer(123, 'HP', 'L1200', 'Laser')
    copy_machine_1 = Copier(124, 'Xerox', 'XX20XX', 100)
    scanner_1 = Scanner(125, 'HP', '1234', 100, 'A3')
    print(printer_1)
    printer_1.do_some_work()
    copy_machine_1.do_some_work()
    scanner_1.do_some_work()
    print(Warehouse())
    Warehouse.add(printer_1)
    Warehouse.add(scanner_1)
    Warehouse.add(copy_machine_1)
    print(Warehouse())
    Warehouse.rem_wh_add_dep(printer_1)
    print(Warehouse())


if __name__ == '__main__':
    main()
