def solution(numbers: list, x: int) -> list:
    
    leftArr: list = []
    centerArr: list = []
    rightArr: list = []

    for i in range(len(numbers)):

        if numbers[i] > x:
            rightArr.append(numbers[i])
        elif numbers[i] < x:
            leftArr.append(numbers[i])
        else:
            centerArr.append(numbers[i])

    return leftArr + centerArr+ rightArr

lst: list = [9, 12, 3, 5, 14, 10, 10]

print(solution(lst, 10))