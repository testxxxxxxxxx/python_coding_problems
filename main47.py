import math

def getDistance(x1: int, x2: int, y1: int, y2: int) -> float:

    if x1 > x2 or y1 > y2:
        xa: int = x2
        xb: int = x1
        ya: int = y2
        yb: int = y1
   
    else:
        xa: int = x1
        xb: int = x2
        ya: int = y1
        yb: int = y2

    return math.sqrt(pow(yb - ya, 2) + pow(xb - xa, 2))

def getMaxDistance(centalPoint: tuple, points: list) -> float:

    distance: float = 0
    maxDistance: float = 0

    for i in points:

        distance = getDistance(i[0], centalPoint[0], i[1], centalPoint[1])

        if distance > maxDistance:
            maxDistance = distance

    return maxDistance

def solution(centalPoint: tuple, points: list, k: int) -> list:

    maxPoint: tuple = max(points)
    minDistance: float = getDistance(maxPoint[0], centalPoint[0], maxPoint[1], centalPoint[1])
    distance: float = 0
    results: list = []
    minX: int = -1
    minY: int = -1
    deletedIndex: int = 0
    pointsCopy: list = points.copy()

    for i in range(len(points)):

        minDistance = getDistance(maxPoint[0], centalPoint[0], maxPoint[1], centalPoint[1]) + getMaxDistance(centalPoint, pointsCopy)

        if len(results) == k:
            break

        for j in range(len(points)):

            if points[j] != None:

                distance = getDistance(points[j][0], centalPoint[0], points[j][1], centalPoint[1])

                if distance < minDistance:
                    minDistance = distance
                    minX = points[j][0]
                    minY = points[j][1]
                    deletedIndex = j     

        points[deletedIndex] = None

        if minX != -1 and minY != -1:

            results.append((minX, minY))

        minX = -1
        minY = -1
        
    return results

points: list = [(0, 0), (5, 4), (3, 1)]

print(solution((1, 2), points, 2))