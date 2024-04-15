from collections import deque


class MaxQuery:
    def __init__(self):
        self.data = deque()
        self.max_values = deque()

    def add_element(self, value):
        self.data.append(value)
        i = len(self.max_values) - 1
        while self.max_values and self.max_values[i] < value:
            self.max_values[i] = value
        self.max_values.append(value)

    def remove_element(self):
        if self.data[0] == self.max_values[0]:
            self.max_values.popleft()
        return self.data.popleft()

    def get_max(self):
        return self.max_values[0]

    def print_dq(self):
        print(self.max_values)


n, k = map(int, input().split())
cost = [0] + list(map(int, input().split())) + [0]

dp = [0] * (n + 1)
dq = MaxQuery()
dq.add_element(0)
counter = 1
for i in range(1, n + 1):
    print(dp)
    dp[i] = cost[i - 1] + dq.get_max()
    dq.add_element(dp[i])
    if i > k:
        dq.remove_element()

    dq.print_dq()

mx = dp[n]
i = n - 1
res = [n]

while i > 0:
    if dp[i] == mx:
        res.append(i)
        mx -= cost[i - 1]
    i -= 1

print(dp[n])
print(len(res) - 1)
print(*reversed(res))
