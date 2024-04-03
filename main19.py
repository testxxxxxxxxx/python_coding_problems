class Node():

    def __init__(self, value: int, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

node = Node(5, Node(4, Node(3), Node(5)), Node(6))

maxSumLeft: int = 0
sumsLeft: int = 0

def solution(node) -> int:

    def left(node, sums0: int = 0, maxSum: int = 0) -> int:

        if not node:
            return maxSum
        
        sums0 += node.value

        if sums0 > maxSum:
            maxSum = sums0
        else:
            sums0 = 0    
        
        return left(node.left, sums0, maxSum)

    def right(node, sums0: int = 0, maxSum: int = 0) -> int:

        if not node:
            return maxSum
        
        sums0 += node.value

        if sums0 > maxSum:
            maxSum = sums0
        else:
            sums0 = 0    
        
        return right(node.right, sums0, maxSum)
    
    def leftRight(node, sums0: int = 0, maxSum: int = 0) -> int:

        if not node:
            return maxSum

        sums0 += node.value

        if sums0 > maxSum:
                maxSum = sums0
        else:
            sums0 = 0    
        
        return leftRight(node.right, sums0, maxSum)
    
    def rightLeft(node, sums0: int = 0, maxSum: int = 0) -> int:

        if not node:
            return maxSum
        
        sums0 += node.value

        if sums0 > maxSum:
            maxSum = sums0
        else:
            sums0 = 0    
        
        return rightLeft(node.left, sums0, maxSum)
    
    sumLeft: int = left(node.left)
    sumRight: int = right(node.right)
    sumLeftRight: int = leftRight(node.left)
    sumRightLeft: int = rightLeft(node.right)

    return max(sumLeft, sumRight, sumLeftRight, sumRightLeft)

print(solution(node))