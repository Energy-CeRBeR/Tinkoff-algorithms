def height(node):
    if node is None:
        return 0
    else:
        return max(height(node.left), height(node.right)) + 1



n, r = map(int, input().split())
roots = dict()

for i in range(n):
    roots[i] = list(map(int, input().split()))

print(roots)

flag = 1
for parent, children in roots.items():
    if children[0] < parent < children[1]:
        ...
