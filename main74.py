class Node():

    def __init__(self, value: int, left = None, right = None, parent = None) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.parent = None

count: int = 1
height: int = 0
height0: int = 0
state: bool = False

def countOfNodesLeft(node, i: int = 0) -> None:

    global count, height

    if not node.left:
        return 
    
    if i == 0:
        count = 2
    else:
        count *= 2
        count += 2

    i += 1
    height += 1 
            
    countOfNodesLeft(node.left, i)

def countLastHeight(node) -> None:

    global count, state, height0

    if height0 == height:
            state = True

    if not node:
        return

    if not node.left and height0 != height:
            
        count -= 1

        #height0 = 0

        #print(node.value)

        return

    #if not node.right and height0 != height:

        #count -= 1

        #height0 = 0

        #print(node.value)

        #return

    height0 += 1

    if not state:

        countLastHeight(node.right)
        countLastHeight(node.left)

    return    
    
node: Node = Node(1, Node(2, Node(4, Node(10), Node(11), Node(2)), Node(5, Node(12), Node(13))), Node(3, Node(6, Node(8), Node(9)), Node(7, Node(21))))

countOfNodesLeft(node)
countLastHeight(node)

print(count)