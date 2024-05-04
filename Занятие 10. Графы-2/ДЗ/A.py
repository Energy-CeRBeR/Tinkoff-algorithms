n, m = map(int, input().split())

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.size = [1] * (n+1)
        self.min_element = [i for i in range(n+1)]
        self.max_element = [i for i in range(n+1)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]
            self.min_element[y_root] = min(self.min_element[x_root], self.min_element[y_root])
            self.max_element[y_root] = max(self.max_element[x_root], self.max_element[y_root])
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
            self.min_element[x_root] = min(self.min_element[x_root], self.min_element[y_root])
            self.max_element[x_root] = max(self.max_element[x_root], self.max_element[y_root])
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
            self.size[x_root] += self.size[y_root]
            self.min_element[x_root] = min(self.min_element[x_root], self.min_element[y_root])
            self.max_element[x_root] = max(self.max_element[x_root], self.max_element[y_root])

disjoint_set = DisjointSet(n)

for _ in range(m):
    operation = input().split()
    if operation[0] == 'union':
        disjoint_set.union(int(operation[1]), int(operation[2]))
    elif operation[0] == 'get':
        x = int(operation[1])
        root = disjoint_set.find(x)
        print(disjoint_set.min_element[root], disjoint_set.max_element[root], disjoint_set.size[root])