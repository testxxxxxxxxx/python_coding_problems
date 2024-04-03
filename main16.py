class Node():

    def __init__(self, value: str, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right


node = Node('a',Node('b',Node('d')),Node('c'))

def solution(node, previosValue):

    if not node or node.value == None:
        return previosValue
    
    print(node.value)
    
    previosValue = node.value
    
    solution(node.left, previosValue)
    solution(node.right, previosValue)

print(solution(node,''))