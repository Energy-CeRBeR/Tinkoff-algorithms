def components(graph):
    visited = [False] * len(graph)

    def traverse(i):
        visited[i] = True
        stack = [i]
        while stack:
            i = stack.pop()
            yield i
            for j in graph[i]:
                if not visited[j]:
                    visited[j] = True
                    stack.append(j)

    for i in range(1, len(graph)):
        if not visited[i]:
            yield tuple(traverse(i))


n, m = map(int, input().split())
graph = tuple([] for _ in range(n + 1))
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

answer = tuple(components(graph))

print(len(answer))
for c in answer:
    print(len(c))
    print(*sorted(c))

