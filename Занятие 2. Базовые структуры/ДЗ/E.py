from collections import deque


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        return self.stack.pop()

    def len(self):
        return len(self.stack)

    def get_elem(self, index):
        return self.stack[index]


def solve():
    answer = []
    stack = Stack()
    dq = deque()
    num = 1
    total = 0
    for val in tr:
        if stack.len() > 0 and val > stack.get_elem(stack.len() - 1):
            print(0)
            return 0

        dq.append(1)
        stack.push(val)
        while stack.len() > 0 and stack.get_elem(stack.len() - 1) == num:
            dq.append(2)
            stack.pop()
            num += 1

    val = dq.popleft()
    count = 1
    while len(dq) > 0:
        if dq[0] == val:
            count += 1
        else:
            total += 1
            answer.append((val, count))
            val = dq[0]
            count = 1
        dq.popleft()

    total += 1
    answer.append((val, count))

    print(total)
    for item in answer:
        print(*item)


n = int(input())
tr = list(map(int, input().split()))
solve()

