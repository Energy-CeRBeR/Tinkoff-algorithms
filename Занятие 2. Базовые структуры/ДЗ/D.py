class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def print_stack(self):
        print(*self.stack)


n = int(input())
a = list(map(int, input().split()))
stack = []
k = 1
index = -1
for i in range(n - 1):
    if a[i] == a[i + 1]:
        k += 1
        if i == n - 2:
            stack.append([a[-1], k])
            if k > 2:
                index = len(stack) - 1
    else:
        stack.append([a[i], k])
        if k > 2:
            index = len(stack) - 1
        k = 1

if k == 1:
    stack.append([a[-1], 1])

if index != -1:
    count = stack.pop(index)[1]
    index -= 1
    while index >= 0 and index + 1 < len(stack):
        if stack[index][0] == stack[index + 1][0]:
            stack[index][1] += stack[index + 1][1]
            stack.pop(index + 1)
            if stack[index][1] > 2:
                count += stack.pop(index)[1]
                index -= 1
        else:
            break

    print(count)
else:
    print(0)
