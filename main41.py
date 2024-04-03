def solution(numbers: list, index: int) -> int | None:

    element: int = numbers[index]
    firstMaxIndex: int = 0
    firstMax: int | None = None
    count: int = 0

    for i in range(len(numbers)):

        if numbers[i] > element:

            if count == 0:
                firstMaxIndex = i
                firstMax = numbers[i]

            if numbers[i] < firstMax:
                firstMaxIndex = i
                firstMax = numbers[i]

            count += 1

    if firstMax == None:
        return None

    return firstMaxIndex

print(solution([4, 1, 3, 5, 6], 0))