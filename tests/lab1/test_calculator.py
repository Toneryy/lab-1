from unittest import TestCase
from tests.lab1.calculator import calculator


class CalculatorTestCase(TestCase):
    def test_1(self) -> None:
        self.assertEqual(calculator('СТОП'), 'Вы закончили работу с калькулятором!')

    def test_2(self) -> None:
        self.assertEqual(calculator('5+6'), '11')

    def test_3(self) -> None:
        self.assertEqual(calculator('5/'), 'Неизвестный ввод')

    def test_4(self) -> None:
        self.assertEqual(calculator('выпривпр'), 'Вы ввели не 2 числа, программа будет запущена заново')

    def test_5(self) -> None:
        self.assertEqual(calculator('sin'),
                          'Вы ввели больше 1 числа, либо операции для данного числа не существует, программа будет запущена заново')

    def test_6(self) -> None:
        self.assertEqual(calculator('sin()'),
                          'В функции sin(), cos(), tg(), ctg(), sqrt() нужно передать один аргумент!')

    def test_7(self) -> None:
        self.assertEqual(calculator('ctg(225'), '1.0000000000000004')

    def test_8(self) -> None:
        self.assertEqual(calculator('5(76-5)'), 'Вы ввели не 2 числа, программа будет запущена заново')

    def test_9(self) -> None:
        self.assertEqual(calculator('6541654654654654646*64516'), '422041391699699699141336')

    def test_10(self) -> None:
        self.assertEqual(calculator('ctg(180)'), '-8165619676597685.0')

    def test_11(self) -> None:
        self.assertEqual(calculator('sqrt(-4*8)'), 'Нельзя вычислить квадратный корень из отрицательного числа!')

    def test_12(self) -> None:
        self.assertEqual(calculator('sqrt(-)'), 'Вы ввели больше 1 числа, либо отрицательное число, программа будет запущена заново')

    def test_13(self) -> None:
        self.assertEqual(calculator('500/0'), 'Нельзя делить на ноль!')

    def test_14(self) -> None:
        self.assertEqual(calculator('15*sqrt(225)-666*sin(0)'), 'Вы ввели больше 1 числа, либо операции для данного числа не существует, программа будет запущена заново')
