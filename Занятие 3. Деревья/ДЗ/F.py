class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def find_min_greater_equal(self, value):
        return self._find_min_greater_equal_recursive(self.root, value)

    def _find_min_greater_equal_recursive(self, node, value):
        if node is None:
            return -1
        if node.value >= value:
            left_result = self._find_min_greater_equal_recursive(node.left, value)
            if left_result != -1:
                return left_result
            return node.value
        return self._find_min_greater_equal_recursive(node.right, value)


bst = BinarySearchTree()

n = int(input())
flag = -2
for _ in range(n):
    query = input().split()
    if query[0] == "+":
        if flag == -2:
            value = int(query[1])
        else:
            value = (flag + int(query[1])) % (10 ** 9)
        bst.insert(value)
        flag = -2
    elif query[0] == "?":
        value = int(query[1])
        result = bst.find_min_greater_equal(value)
        flag = result
        print(result)