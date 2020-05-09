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

        fib_50 = self.calculate_fibonacci(n)
        return self.subtract_min_max(fib_50)

    @staticmethod
    def calculate_fibonacci(n: int) -> int:

        if n <= 1:
            return n

        prev = 0
        fibonacci = 1

        for i in range(n - 1):
            fibonacci += prev
            prev = fibonacci - prev

        return fibonacci

    @staticmethod
    def subtract_min_max(num: int) -> int:
        num_to_str = str(num)
        min_value, max_value = int(num_to_str[0]), int(num_to_str[len(num_to_str) - 1])
        return max_value - min_value


def main():
    plain_text = Decrypter("caesar.txt").decrypt()


if __name__ == "__main__":
    main()
