class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
 
 
def findMax(root):
 
    if (root == None):
        return float('-inf')
 
    res = root.value
    leftres = findMax(root.left)
    rightres = findMax(root.right)
    if (leftres > res):
        res = leftres
    if (rightres > res):
        res = rightres
    return res
 
 
if __name__ == '__main__':
    root = Node(15)
    root.left = Node(13)
    root.right = Node(35)
    root.left.right = Node(12)
    root.left.left = Node(9)
    root.right.right = Node(42)
    root.right.right.left = Node(55)
 
  
    print("Maximum element is",
          findMax(root))
 
