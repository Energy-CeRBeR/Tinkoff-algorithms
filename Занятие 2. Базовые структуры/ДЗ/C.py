class Stack:
    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        return self.stack.pop()


def solve(x, y, operation):
    match operation:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case _:
            return


a = list(map(str, input().strip().split()))
stack = Stack()
answer = 0
for item in a:
    if item.isdigit():
        stack.push(int(item))
    else:
        b = stack.pop()
        a = stack.pop()
        result = solve(a, b, item)
        stack.push(result)

print(stack.pop())
