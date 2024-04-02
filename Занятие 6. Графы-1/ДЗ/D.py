from collections import deque


def is_valid(x, y, n):
    return 1 <= x <= n and 1 <= y <= n


def knight_shortest_path(n, x1, y1, x2, y2):
    dx = [1, 1, 2, 2, -1, -1, -2, -2]
    dy = [2, -2, 1, -1, 2, -2, 1, -1]

    visited = [[False for _ in range(n)] for _ in range(n)]
    path = [[0 for _ in range(n)] for _ in range(n)]

    queue = deque([(x1, y1)])
    visited[x1 - 1][y1 - 1] = True

    while queue:
        x, y = queue.popleft()
        if x == x2 and y == y2:
            break

        for i in range(8):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if is_valid(new_x, new_y, n) and not visited[new_x - 1][new_y - 1]:
                visited[new_x - 1][new_y - 1] = True
                path[new_x - 1][new_y - 1] = (x, y)
                queue.append((new_x, new_y))

    k = 0
    curr_x, curr_y = x2, y2
    while (curr_x, curr_y) != (x1, y1):
        k += 1
        curr_x, curr_y = path[curr_x - 1][curr_y - 1]

    positions = [(x2, y2)]
    curr_x, curr_y = x2, y2
    while (curr_x, curr_y) != (x1, y1):
        curr_x, curr_y = path[curr_x - 1][curr_y - 1]
        positions.append((curr_x, curr_y))

    positions.append((x1, y1))
    positions.reverse()

    return k, positions


n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

k, positions = knight_shortest_path(n, x1, y1, x2, y2)
positions.pop(0)
print(k)
for pos in positions:
    print(*pos)
