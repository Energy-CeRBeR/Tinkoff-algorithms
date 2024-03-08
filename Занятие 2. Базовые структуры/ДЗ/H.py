class Stack:
    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        return self.stack.pop()

    def empty(self):
        return len(self.stack) == 0

    def top(self):
        return self.stack[-1][0]

    def print_stack(self):
        print(*self.stack)

    def sort(self):
        return self.stack.sort()

    def get_last(self):
        return self.stack[-1][1]


def prefix_amounts(arr):
    result = [arr[0]]
    for i in range(1, len(arr)):
        result.append(result[i - 1] + arr[i])
    return result


def get_prev_smaller(arr):
    stack = Stack()
    stack2 = Stack()
    l = len(arr)
    result = [[-1, l] for _ in range(n)]
    for i in range(l):
        while not stack.empty() and stack.top() >= arr[i]:
            stack.pop()
        if not stack.empty():
            result[i][0] = stack.get_last()
        else:
            result[i][0] = -1

        while not stack2.empty() and stack2.top() >= arr[l - i - 1]:
            stack2.pop()
        if not stack2.empty():
            result[l - i - 1][1] = l - stack2.get_last() - 1
        else:
            result[l - i - 1][1] = l

        stack.push((arr[i], i))
        stack2.push((arr[l - i - 1], i))

    return result


n = int(input())
a = list(map(int, input().split()))
segments = get_prev_smaller(a)
ps = prefix_amounts(a)
mx = -10 ** 28
for i in range(n):
    num = a[i]
    x = segments[i][0]
    y = segments[i][1]
    if x != -1:
        m = (ps[y - 1] - ps[x]) * num
    else:
        m = ps[y - 1] * num

    mx = max(mx, m)

print(mx)
