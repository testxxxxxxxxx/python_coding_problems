class Node():

    def __init__(self, value: int = 0, parent = None, left = None, right = None) -> None:
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

class BinaryTree():

    def __init__(self) -> None:
        self.root = None

    def addToNode(self, parentNode , node, values: list, i: int) -> None:

        if i == len(values) - 1:

            return

        node = Node()
        node.value = values[i]
        node.parent = parentNode

        if  i == 0:
            self.root = node

        i += 1

        self.addToNode(node, node.left, values, i)
        self.addToNode(node, node.right, values, i)

binaryTree = BinaryTree()

binaryTree.addToNode(None, None, [1, 2, 3, 4, 5, 6], 0)

def solution(node) -> int:

    return 0

#node: Node = Node(1, None, Node(2, None, Node(3), Node(4, None, Node(3), Node(6))))