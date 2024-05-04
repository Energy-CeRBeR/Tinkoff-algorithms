n, m = map(int, input().split())

edges = []
for _ in range(m):
    b, e, w = map(int, input().split())
    edges.append((b, e, w))

edges.sort(key=lambda x: x[2])

parent = [i for i in range(n+1)]
rank = [0] * (n+1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root == y_root:
        return

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

total_weight = 0
for edge in edges:
    b, e, w = edge
    if find(b) != find(e):
        total_weight += w
        union(b, e)

print(total_weight)