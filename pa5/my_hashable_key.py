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
        int_value = 0
        key = self.key
        if isinstance(self.key, int):
            int_value = key * 2654435761
        if isinstance(self.key, str):
            for char in key:
                int_value = (int_value * 31 + ord(char)) % (2**32)
        if isinstance(self.key, tuple):
            for x in self.key:
                if isinstance(x, int):
                    int_value += x * 2654435761
                elif isinstance(x, str):
                    for char in x:
                        int_value += (int_value * 31 + ord(char)) % (2**32)
        return int(int_value)


if __name__ == "__main__":
    rand = Random()
    key_1 = Key("1", "Hello")
    key_1_1 = Key("2", "Hello")
    key_1_2 = Key("3", "Hello")
    key_1_3 = Key("4", "Hello")
    key_1_4 = Key("5", "Hello")
    key_1 = Key("6", "Hello")
    key_2 = Key("7", "Hello")
    key_3 = Key((21, 124, 214, 144), "Hello")
    key_4 = Key(("aouawf", "napifnpiaf", 214, 144), "Hello")
    key_4 = Key(("234", "napi131", 21241, 3), "Hello")
    print(hash(key_1) % (8 * 2))
    print(hash(key_1_1) % (8 * 2))
    print(hash(key_1_2) % (8 * 2))
    print(hash(key_1_3) % (8 * 2))
    print(hash(key_1_4) % (8 * 2))
    print(hash(key_2) % (8 * 2))
    print(hash(key_3) % (8 * 2))
    print(hash(key_4) & (8 * 2))
