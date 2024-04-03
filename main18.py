class Node():

    def __init__(self, value: int, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

node: Node = Node(5, Node(4, Node(3), Node(6)), Node(6, Node(4, Node(3, Node(2, Node(1), Node(3, Node(2), Node(4))), Node(5)), Node(5)), Node(7)))

maxCount: int = 0
count: int = 0

def solution(node) -> None:

    global maxCount
    global count

    if not node:
        return
    
    if node.left and node.left.value < node.value and node.right.value > node.left.value:
        count += 2

        if count > maxCount:
            maxCount = count
    else:
        count = 0

    solution(node.left)
    
    solution(node.right)

solution(node)

print(maxCount)