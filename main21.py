class Node():

    def __init__(self, value: int, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

def solution(node) -> None:

    if not node:
        return 
    
    print(node.value)

    solution(node.left)
    solution(node.right)

node: Node = Node(1, Node(2), Node(3, Node(4), Node(5)))

solution(node)