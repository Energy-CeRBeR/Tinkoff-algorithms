class SegmentTree:
    def __init__(self, array):
        self.array = array
        self.size = len(array)
        self.tree = [0] * (2 * self.size)
        self.build()

    def build(self):
        for i in range(self.size):
            self.tree[self.size + i] = self.array[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        index += self.size
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]

    def query(self, left, right):
        left += self.size
        right += self.size
        result = 0
        while left <= right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 0:
                result += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return result