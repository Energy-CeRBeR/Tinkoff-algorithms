def binary_search(number, arr):
    a = sorted(arr)
    left = 0
    right = len(a)
    middle = (left + right) // 2
    while right > left:
        if a[middle] == number:
            return middle
        if a[middle] < number:
            left = middle + 1
        if a[middle] > number:
            right = middle - 1


class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def back_pop(self):
        self.queue.pop()

    def front_pop(self):
        self.queue.pop(0)

    def get_position(self, q):
        return binary_search(q, self.queue)

    def get_first(self):
        return self.queue[0]


n = int(input())
queue = Queue()
for _ in range(n):
    event = list(map(int, input().split()))
    match event[0]:
        case 1:
            queue.push(event[1])
        case 2:
            queue.front_pop()
        case 3:
            queue.back_pop()
        case 4:
            print(queue.get_position(event[1]))
        case 5:
            print(queue.get_first())

