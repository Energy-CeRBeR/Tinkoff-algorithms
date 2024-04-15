n = int(input())
costs = list(map(int, input().split()))

dp = [0] * n
dp[0] = costs[0]
if n >= 2:
    dp[1] = costs[1]
    for i in range(2, n):
        dp[i] = costs[i] + min(dp[i - 1], dp[i - 2])

print(dp[n - 1])
