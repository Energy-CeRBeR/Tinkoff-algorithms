class Heap:
    def __init__(self):
        self.heap = list()

    def inset(self, item):
        self.heap.append(item)
        self.go_up(len(self.heap) - 1)

    def go_up(self, child_index):
        parent_index = (child_index - 1) // 2
        if child_index <= 0:
            return
        elif self.heap[child_index] > self.heap[parent_index]:
            self.heap[child_index], self.heap[parent_index] = self.heap[parent_index], self.heap[child_index]
            self.go_up(parent_index)

    def go_down(self, parent_index):
        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2
        largest = parent_index
        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index
        if largest != parent_index:
            self.heap[parent_index], self.heap[largest] = self.heap[largest], self.heap[parent_index]
            self.go_down(largest)

    def extract(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        result = self.heap.pop(-1)
        self.go_down(0)

        return result


n = int(input())
heap = Heap()
for _ in range(n):
    query = list(map(int, input().split()))
    if query[0] == 0:
        heap.inset(query[1])
    else:
        mx = heap.extract()
        print(mx)
