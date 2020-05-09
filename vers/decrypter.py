class Decrypter:
    CAESAR_FILE = "caesar.txt"
    COUNT_XYZ_FILE = "count-x-y-w.txt"
    AFTER_Z_FILE = "after-z.txt"

    __files_paths = ()
    __files_and_contents_dict = {}

    def __init__(self, encrypted_file: str = CAESAR_FILE):
        self.__files_paths = (encrypted_file, self.COUNT_XYZ_FILE, self.AFTER_Z_FILE)
        self.__load_files()

    def decrypt(self) -> str:
        offset = self.count_xyz() + self.avg_z_count() + self.calc_fibonacci_50()

    def count_xyz(self) -> int:
        xyz_text = self.get_text_content(self.COUNT_XYZ_FILE)

        return xyz_text.count('X') + xyz_text.count('Y') - xyz_text.count('W')

    def avg_z_count(self) -> int:
        raise NotImplementedError

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

    def __load_files(self) -> None:
        for file_path in self.__files_paths:
            self.__files_and_contents_dict[file_path] = self.__load(file_path)

    @staticmethod
    def __load(file_path: str) -> str:
        try:
            file = open(file_path, "r", encoding="UTF-8")
            text = ''.join(file.readlines())

            file.close()
        except Exception as ex:
            print("Fájl beolvasás hiba: ", ex)
        else:
            return text

    def get_text_content(self, file_name: str) -> str:
        return self.__files_and_contents_dict.get(file_name)


def main():
    plain_text = Decrypter().decrypt()


if __name__ == "__main__":
    main()
