n = int(input())
a = list(map(int, input().split()))

dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)

mx = max(dp)
print(mx)

ans = []
i = n - 1
while mx > 0:
    if dp[i] == mx:
        ans.append(a[i])
        mx -= 1
    i -= 1

ans.reverse()
print(*ans)
