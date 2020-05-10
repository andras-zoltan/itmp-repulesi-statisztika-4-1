import re


class Decrypter:
    CAESAR_FILE = "caesar.txt"
    COUNT_XYZ_FILE = "count-x-y-w.txt"
    AFTER_Z_FILE = "after-z.txt"

    __files_paths = ()
    __files_and_contents_dict = {}

    def __init__(self, encrypted_file: str = CAESAR_FILE):
        self.__files_paths = (encrypted_file, self.COUNT_XYZ_FILE, self.AFTER_Z_FILE)
        self.__load_files()

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

    def decrypt(self) -> str:
        offset = self.calc_offset()

        encrypted_text = (self.get_text_content(self.CAESAR_FILE))
        print("encrypted_text:")
        print("-" * 20)
        print(encrypted_text)

        plain_text = self.decrypt_text(encrypted_text, offset)
        print("plain text:")
        print("-" * 20)
        print(''.join(plain_text))

    def calc_offset(self):
        return self.count_xyz() + self.avg_z_count() + self.calc_fibonacci_50()

    @staticmethod
    def decrypt_text(encrypted_text: str, offset: int):
        return list(map(
            lambda letter: Decrypter.__decrypt_letter(letter, offset) if re.match('[a-z]|[A-Z]', letter) else letter,
            encrypted_text))

    @staticmethod
    def __decrypt_letter(letter: str, offset: int) -> str:
        if 'A' <= letter <= 'Z':
            return chr(
                ord(letter) - offset if (ord(letter) - offset) >= ord('A') else ord(
                    'Z') - ord('A') + ord(letter) - offset + 1)

        if 'a' <= letter <= 'z':
            return chr(
                ord(letter) - offset if (ord(letter) - offset) >= ord('a') else ord('z') - ord('a') + ord(
                    letter) - offset + 1)

        raise AttributeError('A megadott karakter nem dekódolható!!!')

    def count_xyz(self) -> int:
        xyz_text = self.get_text_content(self.COUNT_XYZ_FILE)

        return xyz_text.count('X') + xyz_text.count('Y') - xyz_text.count('W')

    def avg_z_count(self) -> int:
        avg_z_text = self.get_text_content(self.AFTER_Z_FILE)

        pattern = re.compile('Z\d')
        all_matches = pattern.findall(avg_z_text)

        return sum(list(map(lambda match: int(match[1:]), all_matches))) // len(all_matches)

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

    def get_text_content(self, file_name: str) -> str:
        return self.__files_and_contents_dict.get(file_name)


def main():
    plain_text = Decrypter().decrypt()


if __name__ == "__main__":
    main()
