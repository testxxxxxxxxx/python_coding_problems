class Node():

    def __init__(self, value: int, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

def removeLeaps(node, count: int = 0) -> int:

    if not node:
        return count // 2

    if (node.left and node.left.value == 0) and not node.right.left and not node.left.left:
        node.left = None
        count += 1
    
    if node.right and node.right.value == 0 and not node.right.left and not node.right.right:
        node.right = None
        count += 1

    return removeLeaps(node.left, count) + removeLeaps(node.right, count)

def showTree(node) -> None:

    if not node:
        return
    
    print(node.value)

    showTree(node.left)
    showTree(node.right)

node: Node = Node(0, Node(1), Node(0, Node(1, Node(0), Node(0)), Node(0)))

count: int = 1

showTree(node)

print('______')

while count != 0:

    count = removeLeaps(node)

showTree(node)