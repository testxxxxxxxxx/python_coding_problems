class Node():

    def __init__(self, value: str, weight: int, parent = None, left = None, right = None, center = None) -> None:
        self.value = value
        self.weight = weight
        self.parent = parent
        self.left = left
        self.right = right
        self.center = center

def findMax(values: list) -> tuple:

    maxLength: int = 0
    index: int = -1

    for i in range(len(values)):

        if values[i] != None:

            if values[i] > maxLength:
                maxLength = values[i]
                index = i

    return (maxLength, index)

def solution(node) -> None:

    keys: list = []
    values: list = []
    paths: list = [[]]
    it: int = 0

    def insertToArr(node, treeHeight: int = 1, previousNode: str = node.parent.value) -> None:

        if not node:
            return
        
        if node.parent.value != previousNode:
            treeHeight += 1

        #if i > 0:
            #keys.append((node.parent.value, node.value))
        values.append((node.weight, treeHeight))

        previousNode = node.parent.value

        insertToArr(node.left, treeHeight, previousNode)
        insertToArr(node.center, treeHeight, previousNode)
        insertToArr(node.right, treeHeight, previousNode)

    insertToArr(node)
    
    left: int = 0
    count: int = 0
    left: int = 0
    lastHeight: int = 1
    graterPath: list = []

    for i in range(1 ,len(values)):

        if values[left][1] < values[i][1]:
            if count == 0:
                paths[it].append(values[left][0])
            paths[it].append(values[i][0])
            lastHeight = values[i][1]
            count += 1

        elif lastHeight > values[i][1]:
            paths[it].append(values[left][0])
            paths.append([])
            it += 1
            count = 0
        else:
            paths[it].append(values[left][0])
            paths.append([])
            it += 1
            left += 1
            count = 0

    results: list = []

    for i in paths:

        if len(i) > 1:
            graterPath.append(i)   

    for i in range(len(graterPath)):

        left: int = graterPath[i][0]
        sumResults: int = 0

        for j in range(len(graterPath[i]) - 1):

            for x in graterPath[i]:

                res: int = left

                sumResults += res

                res += graterPath[i][j + 1]

            results.append(sumResults)
            sumResults = 0

    print(results)



maxLength: int = 0
sumLength: int = 0
previousNode: str = ''
results: list = []

node: Node = Node('a', 0, Node('a', 0),Node('b', 3, Node('a', 0)),Node('d', 8, Node('a', 0),Node('e', 2, Node('d', 8), Node('g', 1, Node('e', 2)), Node('h', 1, Node('e', 2))), Node('f', 4, Node('d', 8))),center=Node('c', 5, Node('a', 0)))

solution(node)