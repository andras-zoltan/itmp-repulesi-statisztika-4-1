import unittest
from decrypter import Decrypter


class TestDecrypter(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.__decrypter = Decrypter("caesar.txt")

    def test_calculate_fibonacci(self):
        self.assertEqual(Decrypter.calculate_fibonacci(0), 0)
        self.assertEqual(Decrypter.calculate_fibonacci(1), 1)
        self.assertEqual(Decrypter.calculate_fibonacci(5), 5)
        self.assertEqual(Decrypter.calculate_fibonacci(7), 13)
        self.assertEqual(Decrypter.calculate_fibonacci(9), 34)

        self.assertEqual(Decrypter.calculate_fibonacci(50), 12586269025)

    def test_subtract_min_max(self):
        self.assertEqual(Decrypter.subtract_min_max(Decrypter.calculate_fibonacci(7)), 2)
        self.assertEqual(Decrypter.subtract_min_max(Decrypter.calculate_fibonacci(9)), 1)

    def test_calc_fibonacci_50(self):
        self.assertEqual(self.__decrypter.calc_fibonacci_50(), 4)


if __name__ == '__main__':
    unittest.main()
