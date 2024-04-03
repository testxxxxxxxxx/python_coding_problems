class Node():

    def __init__(self, value, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

        
tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))

count = 0

def solution(tree):

    node = tree

    def counter(node):

        global count

        if not node or not node.left or not node.right:
            return
        elif node.value == node.left.value or node.value == node.right.value: 
            count += 1
            counter(node.left)   
            counter(node.right)
            counter(node.left.right)
            counter(node.right.left)

    counter(node)

    return count + 1

print(solution(tree))