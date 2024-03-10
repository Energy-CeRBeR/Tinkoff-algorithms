n = int(input())
a = list(map(int, input().split()))
m = int(input())

ps = [0] * n
p_xor = [0] * n
s = 0
xor = 0
for i in range(n):
    s += a[i]
    ps[i] = s
    xor ^= a[i]
    p_xor[i] = xor

for _ in range(m):
    query, l, r = map(int, input().split())
    if query == 1:
        s = ps[r - 1] - ps[l - 2] if l > 1 else ps[r - 1]
        print(s)
    else:
        xor = p_xor[r - 1] ^ p_xor[l - 2] if l > 1 else p_xor[r - 1]
        print(xor)
