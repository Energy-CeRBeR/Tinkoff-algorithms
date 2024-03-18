class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def is_balanced(node):
    if node is None:
        return True
    lh = height(node.left)
    rh = height(node.right)
    if abs(lh - rh) <= 1 and is_balanced(node.left) and is_balanced(node.right):
        return True
    return False

def is_avl_tree(root):
    if root is None:
        return True
    return is_balanced(root) and is_avl_tree(root.left) and is_avl_tree(root.right)

def is_right_subtree_valid(node):
    if node is None:
        return True
    if node.right and node.right.key <= node.key:
        return False
    return is_right_subtree_valid(node.left) and is_right_subtree_valid(node.right)

def is_left_subtree_valid(node):
    if node is None:
        return True
    if node.left and node.left.key >= node.key:
        return False
    return is_left_subtree_valid(node.left) and is_left_subtree_valid(node.right)

n, r = map(int, input().split())

nodes = [Node(i) for i in range(n)]
for i in range(n):
    li, ri = map(int, input().split())
    if li != -1:
        nodes[i].left = nodes[li]
    if ri != -1:
        nodes[i].right = nodes[ri]

if is_avl_tree(nodes[r]) and is_right_subtree_valid(nodes[r]) and is_left_subtree_valid(nodes[r]):
    print(1)
else:
    print(0)
