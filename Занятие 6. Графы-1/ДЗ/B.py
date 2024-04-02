def has_cycle(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        if node in rec_stack:
            return 1
        if node in visited:
            return 0

        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return 1

        rec_stack.remove(node)
        return 0

    for node in graph:
        if dfs(node):
            return 1

    return 0


n, m = map(int, input().split())

gr = dict()
for _ in range(m):
    u, v = map(int, input().split())
    if u in gr:
        gr[u].append(v)
    else:
        gr[u] = [v]

ans = has_cycle(gr)
print(ans)
