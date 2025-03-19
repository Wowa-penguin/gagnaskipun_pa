from random import Random
from bucket_sll import Bucket
from error import NotFoundException


class HashMap:
    def __init__(self):
        self.array_size = 8
        self.array: list[Bucket] = [Bucket() for _ in range(self.array_size)]
        self.array_items = 0

    def insert(self, key, data):
        if self.array_items >= int(self.array_size * 1.20):
            self.rebuild()
        array_key = hash(key) % self.array_size
        self.array[array_key].insert(key, data)
        self.array_items += 1

    def update(self, key, data):
        array_key = hash(key) % self.array_size
        if self.array[array_key].contains(key):
            self.array[array_key].update(key, data)
        else:
            raise NotFoundException

    def find(self, key):
        array_key = hash(key) % self.array_size
        if self.array[array_key].contains(key):
            return self.array[array_key].find(key)
        raise NotFoundException

    def contains(self, key):
        array_key = hash(key) % self.array_size
        if self.array[array_key].contains(key):
            return True
        return False

    def remove(self, key):
        array_key = hash(key) % self.array_size
        self.array[array_key].remove(key)
        self.array_items -= 1

    def __setitem__(self, key, data):
        try:
            self.update(key, data)
        except NotFoundException:
            self.insert(key, data)

    def __getitem__(self, key):
        return self.find(key)

    def __len__(self):
        return self.array_size

    def rebuild(self):
        self.array_items = 0
        self.array_size *= 2
        old_array = self.array
        self.array = [Bucket() for _ in range(self.array_size)]
        for x in old_array:
            try:
                temp_node = x.head
                while temp_node.next:
                    if temp_node.next:
                        self.insert(temp_node.next.key, temp_node.next.data)
                        temp_node = temp_node.next
            except AttributeError:
                pass


if __name__ == "__main__":
    hash_map = HashMap()
    hash_map.insert(("Hello", "bæ"), "Hallo sonur")
    rand = Random()
    keys = []
    # for _ in range(50):
    #     key_test = rand.randint(0, 1248284120841)
    #     hash_map.insert(key_test, str(rand.randint(0, 199912424)))
    #     keys.append(key_test)
    # # print(keys)
    print(hash_map.find(("Hello", "bæ")))

    # print(hash("Hello"))
    print("done")
