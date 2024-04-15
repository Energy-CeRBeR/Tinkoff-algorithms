def max_square(matrix):
    n = len(matrix)
    m = len(matrix[0])

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    max_size = 0
    top_left = (0, 0)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if matrix[i - 1][j - 1] == 1:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                if dp[i][j] > max_size:
                    max_size = dp[i][j]
                    top_left = (i - max_size + 1, j - max_size + 1)

    return max_size * max_size, top_left


n, m = list(map(int, input().split()))
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

square_size, top_left = max_square(matrix)
print(int(square_size ** 0.5))
print(*top_left)
