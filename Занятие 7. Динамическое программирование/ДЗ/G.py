def ans(left, right):
    if best[left][right] == -1:
        res[left] = res[right] = ""
    if left == right:
        return
    if best[left][right] == -2:
        if left + 1 == right:
            return
        ans(left + 1, right - 1)
    else:
        ans(left, best[left][right])
        ans(best[left][right] + 1, right)
    return


inf = 10 ** 9
s = input()
n = len(s)
dp = [[inf] * (n + 1) for i in range(n + 1)]
best = [[-1] * (n + 1) for j in range(n + 1)]
for i in range(n + 1):
    dp[i][i] = 1

for i in range(n - 1):
    if (s[i] == '(' and s[i + 1] == ')') or (s[i] == '[' and s[i + 1] == ']') or (
            s[i] == '{' and s[i + 1] == '}'):
        dp[i][i + 1] = 0
        best[i][i + 1] = -2

for L in range(2, n + 1):
    for left in range(n - L + 1):
        right = left + L - 1
        if (s[left] == '(' and s[right] == ')') or (s[left] == '[' and s[right] == ']') or (
                s[left] == '{' and s[right] == '}'):
            if dp[left][right] > dp[left + 1][right - 1]:
                dp[left][right] = dp[left + 1][right - 1]
                best[left][right] = -2
        for mid in range(left, right):
            cur = dp[left][mid] + dp[mid + 1][right]
            if dp[left][right] > cur:
                dp[left][right] = cur
                best[left][right] = mid

res = list(s)
ans(0, n - 1)
print(*res, sep="")
