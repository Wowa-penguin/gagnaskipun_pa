class IndexOutOfBounds(Exception):
    pass


class NotFound(Exception):
    pass


class Empty(Exception):
    pass


class NotOrdered(Exception):
    pass


class ArrayList:
    def __init__(self):
        self.arr_capacity = 4
        self.arr_count = 0
        self.arr = [None] * self.arr_capacity

    # Time complexity: O(n) - linear time in size of list
    def __str__(self):
        return_string = ""
        for x in range(self.arr_count):
            if x == self.arr_count - 1:
                return_string += f"{self.arr[x]}"
            else:
                return_string += f"{self.arr[x]}, "
        return return_string

    # Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        if self.arr_count == self.arr_capacity:
            self.resize()
        if self.arr_count == 0:
            self.arr[0] = value
        else:
            for x in range(self.arr_count + 1):
                temp_value = self.arr[x]
                self.arr[x] = value
                value = temp_value
        self.arr_count += 1

    # Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if self.arr_count == self.arr_capacity:
            self.resize()
        if index > self.arr_count or index < 0:
            raise IndexOutOfBounds
        for x in range(self.arr_count + 1):
            if x >= index:
                temp_value = self.arr[x]
                self.arr[x] = value
                value = temp_value
        self.arr_count += 1

    # Time complexity: O(1) - constant time
    def append(self, value):
        if self.arr_count == self.arr_capacity:
            self.resize()
        self.arr[self.arr_count] = value
        self.arr_count += 1

    # Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if self.arr_count == self.arr_capacity:
            self.resize()
        if index >= self.arr_count or index < 0:
            raise IndexOutOfBounds
        self.arr[index] = value

    # Time complexity: O(1) - constant time
    def get_first(self):
        if self.arr_count == 0:
            raise Empty
        return self.arr[0]

    # Time complexity: O(1) - constant time
    def get_at(self, index):
        if index is None:
            raise NotFound
        elif index >= self.arr_count or index < 0:
            raise IndexOutOfBounds
        else:
            return self.arr[index]

    # Time complexity: O(1) - constant time
    def get_last(self):
        if self.arr_count == 0:
            raise Empty
        return self.arr[self.arr_count - 1]

    # Time complexity: O(n) - linear time in size of list
    def resize(self):
        self.arr_capacity *= 2
        new_arr = [None] * self.arr_capacity
        for x in range(self.arr_count):
            new_arr[x] = self.arr[x]
        self.arr = new_arr

    # Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        ret = 0
        if index > self.arr_count - 1 or index < 0:
            raise IndexOutOfBounds
        for x in range(self.arr_count):
            if x == index:
                self.arr[x] = None
                ret = x
            if x != 0:
                if self.arr[x] is not None and self.arr[x - 1] is None:
                    self.arr[x - 1] = self.arr[x]
                    self.arr[x] = None
        self.arr_count -= 1
        return ret

    # Time complexity: O(1) - constant time
    def clear(self):
        self.arr = [None] * self.arr_capacity
        self.arr_count = 0

    # Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        if self.arr[0] is None:
            self.prepend(value)
            return
        else:
            for x in range(self.arr_count - 1):
                if self.arr[x] > self.arr[x + 1]:
                    raise NotOrdered

        for x in range(self.arr_count):
            if self.arr[x] > value:
                self.insert(value, x)
                return
        self.append(value)

    # Time complexity: O(n) - linear time in size of list
    # Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        is_ordered = True
        for x in range(self.arr_count - 1):
            if self.arr[x] > self.arr[x + 1]:
                is_ordered = False
        if is_ordered:
            return self.bin_search(value)
        for x in range(self.arr_count):
            if self.arr[x] == value:
                return x
        raise NotFound

    def bin_search(self, value):
        left = 0
        right = self.arr_count - 1
        while left <= right:
            mid = (left + right + 1) // 2
            if self.arr[mid] == value:
                return mid
            elif self.arr[mid] < value:
                left = mid + 1
            else:
                right = mid - 1
        if self.arr[mid] == value:
            return mid
        raise NotFound

    # Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        self.remove_at(self.find(value))


if __name__ == "__main__":
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
