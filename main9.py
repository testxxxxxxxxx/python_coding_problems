class Node():

    def __init__(self, value: bool = True, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

node: Node = Node(False, Node(False, Node(False), Node(False)),Node(False, Node(False), Node(False)))        

class TreeNode():

    def __init__(self) -> None:
        pass

    def is_locked(self, node: Node) -> bool:
        value: bool = node.value

        return not value

    def lock(self, node) -> bool | None:
        
        if not node:
            return
        if node.value != True and node.left.value != True and node.right.value != True:

            self.lock(node.left)
            self.lock(node.right)

            node.value = True
            
            return True

        return False
    
    def unlock(self, node: Node) -> bool:
        return False
    