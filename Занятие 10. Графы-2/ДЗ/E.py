import heapq

def dijkstra(graph, n, start):
    distance = [float('inf')] * n
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        dist, node = heapq.heappop(pq)

        if dist > distance[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distance

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    start, end, weight = map(int, input().split())
    graph[start - 1].append((end - 1, weight))
    graph[end - 1].append((start - 1, weight))

distances = dijkstra(graph, n, 0)
print(*distances)
