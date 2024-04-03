class Node():

    def __init__(self, value: int, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

def solution(node) -> None:

    result: list = [[]]

    def left(node, i: int, root = None) -> None:

        if not node:
            result.append([])
            return
        
        if root != None:

            if not node.right:
                result.append([])
                return

            result[i].append(root.value)

        result[i].append(node.value)

        left(node.left, i)

    def right(node, i: int, root = None) -> None:

        if not node:
            result.append([])
            return
            
        if root != None:

            if not node.left:
                result.append([])
                return

            result[i].append(root.value)

        result[i].append(node.value)

        right(node.right, i)

    left(node, 0)
    left(node.right, 1, node)
    right(node.left, 2, node)
    right(node, 3)

    finalResult: list = []

    for i in range(len(result)):

        if result[i] != []:
            finalResult.append(result[i])

    print(finalResult)

node: Node = Node(1, Node(2), Node(3, Node(4), Node(5)))

solution(node)