class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findLCA(root, a, b):
    path1 = []
    path2 = []

    if not findPath(root, a, path1) or not findPath(root, b, path2):
        return -1

    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            return path1[i - 1]
        i += 1
    return path1[i - 1]


def findPath(root, val, path):
    path.append(root.data)

    if root.data == val:
        return True

    if ((root.left is not None and findPath(root.left, val, path)) or
            (root.right is not None and findPath(root.right, val, path))):
        return True

    path.pop()
    return False


n = int(input())
node = Node(list(map(int, input().split())))
m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    result = findLCA(node, u, v)
    print(result)