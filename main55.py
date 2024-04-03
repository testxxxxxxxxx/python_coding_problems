def solution(matrix: list) -> int:

    count: int = 0
    maxWays: int = len(matrix) * len(matrix[0])
    x: int = 0
    y: int = 0

    return 0

def isTrue(matrix: list, right: bool = False, start: int = 0) -> bool:

    x: int = 0
    y: int = 0

    if right:
        x = start + 1

    while True:

        if matrix[x][y] == 0 or x == len(matrix) - 1:
            x += 1
        else:
            x -= 1
            y += 1

        if x == len(matrix) - 1 and y == len(matrix[0]) - 1:
            return True