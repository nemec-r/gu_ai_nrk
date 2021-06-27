# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexValue:
    def __init__(self, complex_value):
        self.complex_value = complex_value

    def __add__(self, other):
        return complex(self.complex_value) + complex(other.complex_value)

    def __sub__(self, other):
        return complex(self.complex_value) - complex(other.complex_value)

    def __mul__(self, other):
        return complex(self.complex_value) * complex(other.complex_value)


complex_value_1 = ComplexValue('1+2j')
complex_value_2 = ComplexValue('2-3j')
print(complex_value_1 + complex_value_2)
print(complex_value_1 * complex_value_2)


