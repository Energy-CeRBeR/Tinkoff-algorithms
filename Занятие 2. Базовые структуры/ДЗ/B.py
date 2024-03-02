from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))
d = deque()
for i in range(n):
    if i >= k and d[0] == i - k:
        d.popleft()
    while len(d) > 0 and a[d[-1]] >= a[i]:
        d.pop()
    d.append(i)
    if i >= k - 1:
        print(a[d[0]], end=" ")
