def floydWarshall(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def find_city(dist):
    mn = 10 ** 28
    ans = 0
    for i in range(n):
        mx = max(dist[i])
        if mx < mn:
            ans = i + 1
            mn = mx

    return ans


n, m = list(map(int, input().split()))
INF = 10 ** 28
graph = [[INF if i != j else 0 for j in range(n)] for i in range(n)]

for i in range(m):
    u, v, w = list(map(int, input().split()))
    graph[u - 1][v - 1] = w
    graph[v - 1][u - 1] = w

res = floydWarshall(graph)
answer = find_city(res)
print(answer)
