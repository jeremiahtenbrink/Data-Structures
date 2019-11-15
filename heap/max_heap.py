class Heap():
    def __init__(self):
        self.storage = []
        self.size = 0
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self.size += 1
        self._bubble_up(self.size - 1)

    def delete(self):
        max = self.storage[0]
        self.storage[self.size - 1], self.storage[0] = self.storage[0], self.storage[self.size - 1]
        self.size -= 1
        self.storage.pop()
        self._sift_down(0)
        return max

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return self.size

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2

        if index > 0 and self.storage[index] > self.storage[parent_index]:
            self.storage[index], self.storage[parent_index] = self.storage[
                                                            parent_index], \
                                                        self.storage[index]
            self._bubble_up(parent_index)

    def _sift_down(self, index):
        index_left = 2 * index + 1
        index_right = 2 * index + 2

        index_largest = index

        if index_left < self.size and self.storage[index_left] > self.storage[index]:
            index_largest = index_left
        if index_right < self.size and self.storage[index_right] > self.storage[
            index_largest]:
            index_largest = index_right

        if index != index_largest:
            self.storage[index_largest], self.storage[index] = self.storage[index], \
                                                         self.storage[
                                                             index_largest]
            self._sift_down(index_largest)
