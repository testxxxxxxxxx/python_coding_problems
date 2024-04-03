def sumColumns(coins: list, first: int, column: int) -> int:

    result: int = 0

    for i in range(first ,len(coins)):

        result += coins[i][column]

    return result

def sumRows(coins: list, first: int, row: int) -> int:

    result: int = 0

    for i in range(first ,len(coins[0])):

        result += coins[row][i]

    return result

def solution(coins: list) -> int:

    maxSum: int = 0
    sumCoins: int = 0
    sumCoins0: int = 0
    it: int = len(coins[0]) - 1

    for i in range(len(coins)):

        sumCoins0 = sumColumns(coins, i, it)
        sumCoins = sumCoins0 + sumRows(coins, i, i)

        if sumCoins > maxSum:
            maxSum = sumCoins

        it -= 1

    return maxSum

coins: list = [

    [0, 3, 1, 1],
    [2, 0, 0, 4],
    [1, 5, 3, 1]

]

print(solution(coins))