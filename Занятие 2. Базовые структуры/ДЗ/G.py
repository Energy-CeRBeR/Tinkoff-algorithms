from collections import deque

n = int(input())
a = []
left_queue = deque()
right_queue = deque()
l1 = l2 = 0
for _ in range(n):
    command = input().split()
    if len(command) > 1:
        number = command[-1]
        if command[0] == "+":
            right_queue.append(number)
            l2 += 1
        else:
            right_queue.appendleft(number)
            l2 += 1
    else:
        print(left_queue.popleft())
        l1 -= 1

    if l1 < l2:
        left_queue.append(right_queue.popleft())
        l2 -= 1
        l1 += 1
