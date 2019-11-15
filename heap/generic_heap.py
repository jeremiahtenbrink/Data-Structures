class Heap:
    def __init__(self, comparator = lambda x, y: x < y):
        self.storage = []
        self.priority = []
        self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        self.priority.append(len(self.storage) - 1)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        self.storage[0], self.storage[len(self.storage) - 1] = \
            self.storage[len(self.storage) - 1], self.storage[0]
        self.priority[0], self.priority[len(self.storage) - 1] = \
            self.priority[len(self.storage) - 1], self.priority[0]
        self._sift_down(0)
        self.priority.pop()
        return self.storage.pop()

    def get_priority(self):
        return self.priority[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2

        larger = self.comparator(self.storage[index], self.storage[parent_index])

        if index > 0 and larger:
            self.storage[index], self.storage[parent_index] = \
                self.storage[parent_index], self.storage[index]
            self.priority[index], self.priority[parent_index] = \
                self.priority[parent_index], self.priority[index]
            self._bubble_up(parent_index)

    def _sift_down(self, index):
        index_left = index * 2 + 1
        index_right = index * 2 + 2

        index_largest = index

        if index_left < len(self.storage) - 1:
            compar = self.comparator(self.storage[index], self.storage[index_left])
            if (compar):
                index_largest = index_left

        if index_right < len(self.storage) - 1:
            compar = self.comparator(self.storage[index_largest], self.storage[index_right])
            if compar:
                index_largest = index_right

        if index != index_largest:
            self.storage[index_largest], self.storage[index] = \
                self.storage[index], self.storage[index_largest]
            self.priority[index_largest], self.priority[index] = \
                self.priority[index], self.priority[index_largest]
            self._sift_down(index_largest)
