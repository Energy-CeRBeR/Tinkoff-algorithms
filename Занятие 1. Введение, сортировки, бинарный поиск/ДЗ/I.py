n = int(input())
positions = list(map(int, input().split()))

results = [0] * n
k = 1
print(k, end=" ")
for i in range(n):
    results[positions[i] - 1] = 1
    k += 1
    while results[-1] == 1:
        results.pop()
        k -= 1
        if len(results) == 0:
            break
    print(k, end=" ")
