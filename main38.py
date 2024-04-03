class Node():

    def __init__(self, value: int, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

sumPath: int = 0

def left(node) -> None:

    global leftResult

    if not node:
        return 

    if node.left:

        leftResult.append(node.left.value)

    elif node.right:

        leftResult.append(node.right.value)

    left(node.left)

def right(node) -> None:

    global rightResult

    if not node:
        return
    
    if node.right:

        rightResult.append(node.right.value)

    elif node.left:

        rightResult.append(node.left.value)

    right(node.right)

def leftRight(node) -> None:

    global leftRightResult

    if not node:
        return 
    
    if node.left:

        leftRightResult.append(node.left.value)

    elif node.right:

        leftRightResult.append(node.right.value)

    leftRight(node.right)

def rightLeft(node) -> None:

    global rightLeftResult

    if not node:
        return 
    
    if node.left:

        rightLeftResult.append(node.left.value)

    elif node.right:

        rightLeftResult.append(node.right.value)

    rightLeft(node.left)

def findMin() -> list:

    global leftResult, rightResult, leftRightResult, rightLeftResult

    maxSum: int = max(sum(leftResult), sum(rightResult), sum(leftRightResult), sum(rightLeftResult))
    minSum = maxSum
    minList: list = []
    sumResult = 0
    minCount: int = min(len(leftResult), len(rightResult), len(leftRightResult), len(rightLeftResult))

    if leftResult[0:minCount] in leftRightResult[0:minCount]:
        sumResult = sum(leftRightResult)

        if sumResult < minSum:
            minSum = sumResult
            minList = leftRightResult

    if leftResult[0:minCount] in rightLeftResult[0:minCount]:

        sumResult = sum(rightLeftResult)

        if sumResult < minSum:
            minSum = sumResult
            minList = rightLeftResult

    sumResult = sum(leftResult)

    if sumResult < minSum:
        minSum = sumResult
        minList = leftResult

    sumResult = sum(rightResult)

    if sumResult < minSum:
        minSum = sumResult
        minList = rightResult

    return minList

node: Node = Node(10, Node(5, None, Node(2)), Node(5, None, Node(1, Node(-1))))

results: list = []
leftResult: list = [node.value]
rightResult: list = [node.value]
leftRightResult: list = [node.value]
rightLeftResult: list = [node.value]

left(node)
right(node)
leftRight(node.left)
rightLeft(node.right)

print(findMin())