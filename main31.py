class Node():

    def __init__(self, value: int, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

count: int = 0
minS: int = 255
sumN: int = 0
level: int = 0

def minSum(node, i: int = 0, count: int = 0) -> None:

    global level
    global minS
    global sumN

    if not node:
        return
        
    sumN += node.value

    count += 1
    i += 1

    if sumN < minS:
        minS = sumN
        level = count
        sumN = 0

    if i == 2:
        sumN = 0
        i = 0

    minSum(node.left, i, count)
    minSum(node.right, i, count)

node: Node = Node(60, Node(20), Node(30, Node(10), Node(30)))

minSum(node)

print(level)