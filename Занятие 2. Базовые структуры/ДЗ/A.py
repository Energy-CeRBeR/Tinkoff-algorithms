class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, item):
        self.stack.append(item)
        if len(self.min_stack) == 0:
            self.min_stack.append(item)
            return
        self.min_stack.append(min(self.min_stack[-1], item))

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def get_min(self):
        return self.min_stack[-1]


n = int(input())
stack = Stack()
for _ in range(n):
    data = list(map(int, input().split()))
    if len(data) == 2:
        stack.push(data[1])
    else:
        operation = int(data[0])
        if operation == 2:
            stack.pop()
        else:
            mn = stack.get_min()
            print(mn)

