def solution(n: int, count: int = 0, lastSquaredNumber: int = 0, result: int = 0, i: int = 1) -> int:

    if result == n:
        return count

    if (pow(i, 2) + result <= n):

        lastSquaredNumber = pow(i, 2)

    else:
        result += lastSquaredNumber
        count += 1
        i = 0

    i += 1

    return solution(n, count, lastSquaredNumber, result, i)

print(solution(27))