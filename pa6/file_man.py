class FileMan:
    def __init__(self, path: str):
        self.path = path

    def reed_file(self) -> list:
        ret_lis = []
        with open(self.path, "r", encoding="utf-8") as conn:
            word = conn.read()
            word_list = word.split("\n")
        for w in word_list:
            new_word = w.strip()
            ret_lis.append(new_word)
        return ret_lis

    def write_file(self, new_word: str) -> None:
        with open(self.path, "a", encoding="utf-8") as conn:
            conn.write(new_word + "\n")


if __name__ == "__main__":
    word_3 = FileMan("words/3letter.txt")
