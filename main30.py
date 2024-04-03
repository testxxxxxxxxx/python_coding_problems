class Node():

    def __init__(self, value: int, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

def solution(s, t) -> bool:

    result: list = []

    def leftAndRight(node) -> None:

        if not node:
            return

        result.append(node.value)

        leftAndRight(node.left)
        leftAndRight(node.right)

    leftAndRight(s)

    resultS: list = result

    result = []

    leftAndRight(t)

    resultT: list = result
    it: int = 0

    for i in range(len(resultS)):

        if resultS[i:len(resultT) + it] == resultT:
            return True
        
        it += 1

    return False

s: Node = Node(1, Node(2), Node(3, Node(4), Node(5)))
t: Node = Node(3, Node(4), Node(5))
#t: Node = Node(1, Node(2), Node(3, Node(4), Node(5)))

print(solution(s, t))