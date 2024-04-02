from collections import defaultdict


def solve(graph, order):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    for node in order:
        if in_degree[node] != 0:
            return "NO"
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1

    return "YES"


n, m = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = [v]
    else:
        graph[u].append(v)

input_list = list(map(int, input().split()))

ans = solve(graph, input_list)
print(ans)
