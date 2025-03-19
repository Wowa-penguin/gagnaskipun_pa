from random import Random


class Key:
    def __init__(self, key, data):
        self.key = key
        self.data = data

    def __eq__(self, other):
        return self.key == other.key and self.data == other.data

    def __hash__(self):
        return self.hash()

    def hash(self) -> int:
        if isinstance(self.key, int):
            self.key *= 45389085986 / 81938012914 + 43481393021 - 14000494091
            return int(self.key)
        elif isinstance(self.key, str):
            int_value = 0
            for x in self.key:
                int_value += (
                    ord(x) * 45389085986 / 81938012914 + 43481393021 - 14000494091
                )
            return int_value

    # todo: laga key alstaðar og ekki nota hash hér heldur í buckti and map


if __name__ == "__main__":
    rand = Random()
    key_test = Key(20, "Hello")
    key_test_2 = Key(21, "Hello")
    print(hash(key_test) % 8)
    print(hash(key_test_2) % 8)
