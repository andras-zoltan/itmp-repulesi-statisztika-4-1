class Decrypter:

    def __init__(self, src: str):
        self.__str = str

    def decrypt(self) -> str:
        raise NotImplementedError()

    def count_xyz(self) -> int:
        raise NotImplementedError()

    def avg_z_count(self) -> int:
        raise NotImplementedError()

    def calc_fibonacci_50(self) -> int:
        n = 50

        return self.calculate_fibonacci(n)

    @staticmethod
    def calculate_fibonacci(n):

        if n <= 1:
            return n

        prev = 0
        fibonacci = 1

        for i in range(n - 1):
            fibonacci += prev
            prev = fibonacci - prev

        return fibonacci


def main():
    plain_text = Decrypter("caesar.txt").decrypt()


if __name__ == "__main__":
    main()
