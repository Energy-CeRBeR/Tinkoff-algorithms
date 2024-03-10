#n = int(input())
#p = list(map(int, input().split()))
import random

for _ in range(10):
    n = random.randint(5, 15)
    p = [0] * (n - 1)
    k = 0
    for i in range(1, n - 1):
        p[i] = random.randint(0, k)
        k += 1
    print(n, p)

    cur_num = 0
    d = {0: 1}
    h = {cur_num: 0}

    ans = [0]
    H = 0
    D = 0
    for i in range(n - 1):
        cur_num += 1
        h_i = h[p[i]] + 1
        h[cur_num] = h_i
        ans.append(h_i)
        H = max(H, h_i)

        if h_i in d:
            d[h_i] += 1
        else:
            d[h_i] = 1
        D = max(D, d[h_i])

    print(H, D)
    print(*ans)
    input()
