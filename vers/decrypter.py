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
        raise NotImplementedError()


def main():
    plain_text = Decrypter("caesar.txt").decrypt()


if __name__ == "__main__":
    main()
