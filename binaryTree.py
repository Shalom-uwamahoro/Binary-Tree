class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

root = Node(11)
root.left = Node(22)
root.right = Node(32)
root.left.left = Node(42)
root.left.right = Node(52)

print(root.left.value)