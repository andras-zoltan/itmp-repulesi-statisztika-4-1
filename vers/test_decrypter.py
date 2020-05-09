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


if __name__ == '__main__':
    unittest.main()
