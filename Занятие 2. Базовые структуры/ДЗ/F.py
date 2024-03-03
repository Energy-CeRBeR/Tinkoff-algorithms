import sys

n = int(input())
queue = dict()
k = offset = 0
for _ in range(n):
    event = list(map(int, sys.stdin.readline().split()))
    match event[0]:
        case 1:
            queue[event[1]] = k + offset
            k += 1
        case 2:
            queue.pop(next(iter(queue)))
            offset += 1
            k -= 1
        case 3:
            queue.popitem()
            k -= 1
        case 4:
            print(queue[event[1]] - offset)
        case 5:
            print(next(iter(queue)))