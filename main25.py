class Node():

    def __init__(self, value: int, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

result: list = []
leftResult: list = []
rightResult: list = []

def pathLeft(node, root0, root = None) -> None:

    global result, leftResult, rightResult

    if not node:
        result.append(leftResult)
        result.append(rightResult)
        root = root0
        leftResult = []
        rightResult = []
        return
        
    if root != None:
        leftResult.append(root.value)
        rightResult.append(root.value)

    if node.left:
        leftResult.append(node.left.value)
    
    if node.right:
        rightResult.append(node.right.value)

    pathLeft(node.left, root)
    pathLeft(node.right, root)

def pathRight(node, root0, root = None) -> None:

    global result, leftResult, rightResult

    if not node or not node.left or not node.right:
        result.append(leftResult)
        result.append(rightResult)
        root = root0
        #leftResult = []
        rightResult = []
        return
        
    if root != None:
        leftResult.append(root.value)
        rightResult.append(root.value)
        rightResult.append(node.value)

    #if node.left:
        #leftResult.append(node.left.value)

    if node.right:
        rightResult.append(node.right.value)

    pathLeft(node.left, root)
    pathRight(node.right, root)

node: Node = Node(1, Node(2), Node(3, Node(4, Node(1), Node(6)), Node(5)))

pathLeft(node, node, node)
#pathRight(node.left, node, node)
pathLeft(node.left, node, node)
pathLeft(node.right, node, node)
#pathRight(node, node, node)

print(result)