class Node():

    def __init__(self, value: int, left = None, right = None) -> None:

        self.value = value
        self.left = left
        self.right = right

class TreeContructor():

    def __init__(self, nodes: list) -> None:
        self.nodes: list = nodes
        self.nodes.reverse()
        self.root: Node = Node(self.nodes[0])
        self.pointer = self.root
        self.i: int = 0
        self.middle = (len(nodes) - 1) // 2

        self.nodes = self.nodes[1:]

        self.left: list = self.nodes[self.middle:]
        self.right: list = self.nodes[0:self.middle]

    def add(self) -> None:

        self.pointer = self.root

        for i in range(len(self.left) - 1):  

            self.pointer.left = Node(self.left[i])

            self.pointer = self.pointer.left

            if len(self.left[i:]) % 2 != 0:

                self.pointer.left = Node(self.left[i + 2])
                self.pointer.right = Node(self.left[i + 1])

            else:
                self.pointer.left = Node(self.left[i + 1])

            if i + 2 >= len(self.left) - 1 or i + 1 >= len(self.left) - 1:
                break

        self.pointer = self.root

        for i in range(len(self.right)):  

            self.pointer.right = Node(self.right[i])

            self.pointer = self.pointer.right

            if len(self.right[i:]) % 2 != 0:

                self.pointer.left = Node(self.right[i + 2])
                self.pointer.right = Node(self.right[i + 1])
            else:
                self.pointer.right = Node(self.right[i + 1])

            if i + 2 >= len(self.right) - 1 or i + 1 >= len(self.right) - 1:
                break

def showTree(node) -> None:

    if not node:
        return
    
    print(node.value)

    showTree(node.left)
    showTree(node.right)

treeContructor: TreeContructor = TreeContructor([2, 4, 3, 8, 7, 5])

treeContructor.add()

showTree(treeContructor.root)