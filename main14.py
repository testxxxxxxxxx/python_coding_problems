def goRight(arr: list,N: int, M: int, end: int) -> None:

    for _ in arr:

        print(arr[N][M])

        if M == end:
            break

        M += 1

def goDown(arr: list, N: int, M: int, end: int) -> None:

    for _ in arr:

        if N == end:
            break

        print(arr[N][M])

        N += 1

def goLeft(arr: list, N: int, M: int, end: int) -> None:

    for _ in arr:

        print(arr[N][M])

        if M == end:
            break

        M -= 1

def goUp(arr: list, N: int, M: int, end: int) -> None:

    for _ in arr:

        if N == end:
            break

        print(arr[N][M])

        N -= 1    

def solution(arr: list) -> None:

    #go right

    goRight(arr, 0, 0, len(arr[0]) - 2)

    #go down

    goDown(arr, 0, len(arr[0]) - 1, len(arr[0]) - 1)

    #go left

    goLeft(arr, len(arr[0]) - 2, len(arr[0]) - 2, 1)

    #go up

    goUp(arr, len(arr[0]) - 2, 0, 0)

    #go right

    goRight(arr, 1, 1, len(arr[0]) - 2) 

    #go down

    goLeft(arr, 2, len(arr[0]) - 2, 1)

matrix: list = [[1,  2,  3,  4,  5],
                [6,  7,  8,  9,  10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20]]

print(solution(matrix))