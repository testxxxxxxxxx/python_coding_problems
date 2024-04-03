def sum(i: int, j: int) -> int:

    global L

    tempArr = L[i:j]

    result: int = 0

    for x in range(len(tempArr)):

        result += tempArr[x]

    return result

L = [1, 2, 3, 4, 5]

print(sum(1, 3))