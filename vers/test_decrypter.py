import unittest
from decrypter import Decrypter


class TestDecrypter(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.__decrypter = Decrypter()

    def test_files_load(self) -> None:
        self.assertTrue(len(self.__decrypter.get_text_content('caesar.txt')) > 0)
        self.assertTrue(len(self.__decrypter.get_text_content('count-x-y-w.txt')) > 0)
        self.assertTrue(len(self.__decrypter.get_text_content('after-z.txt')) > 0)

    def test_calculate_fibonacci(self) -> None:
        self.assertEqual(Decrypter.calculate_fibonacci(0), 0)
        self.assertEqual(Decrypter.calculate_fibonacci(1), 1)
        self.assertEqual(Decrypter.calculate_fibonacci(5), 5)
        self.assertEqual(Decrypter.calculate_fibonacci(7), 13)
        self.assertEqual(Decrypter.calculate_fibonacci(9), 34)

        self.assertEqual(Decrypter.calculate_fibonacci(50), 12586269025)

    def test_subtract_min_max(self) -> None:
        self.assertEqual(Decrypter.subtract_min_max(Decrypter.calculate_fibonacci(7)), 2)
        self.assertEqual(Decrypter.subtract_min_max(Decrypter.calculate_fibonacci(9)), 1)

    def test_calc_fibonacci_50(self) -> None:
        self.assertEqual(self.__decrypter.calc_fibonacci_50(), 4)

    def test_count_xyz(self) -> None:
        self.assertEqual(self.__decrypter.count_xyz(), 8)


if __name__ == '__main__':
    unittest.main()
