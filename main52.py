import math

def findArr(keys: list, value: int) -> int:

    for i in range(len(keys)):

        if value == keys[i]:
            return i
        
    return -1

def solution(numbers: list):

    keys: list = []
    values: list = [1 for i in range(len(set(numbers)))]

    for i in numbers:

        if findArr(keys, i) == -1:
            keys.append(i)
        else:
            index: int = findArr(keys, i)

            values[index] += 1

    maxCount: int = max(values)

    indexCount: int = findArr(values, maxCount)

    if maxCount > math.floor(len(set(numbers)) / 2.0):
        return keys[indexCount]

numbers: list = [1, 2, 1, 1, 3, 4, 0]

print(solution(numbers))