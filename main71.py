def solution(prices: list, fee: int) -> int:

    pricesCombinations: list = []

    for i in range(len(prices)):

        pricesCombinations.append([])

    for i in range(len(prices)):

        for j in range(i + 1, len(prices)):

            pricesCombinations[i].append((j,(prices[j] - prices[i]), i))

    maxSum: int = 0
    maxSum0: int = 0
    z: int = 0
    a: int = 0

    print(pricesCombinations)

    maxDiff: int = 0
    bought: list = []

    minPrice: int = min(prices)
    minIndex: int = prices.index(minPrice)

    for i in range(len(prices)):

        for j in range(i, len(prices)):

            #if prices[i] != prices[j]:
                result: int = prices[j] - prices[i]

                if result > maxDiff:
                    maxDiff = result
                else:
                    bought.append(maxDiff)
                    maxDiff = 0
                    minPrice = min(prices[j:])

    print(bought)

    for b in range(len(pricesCombinations[0])):

        for i in range(b, len(pricesCombinations[0])):

            result: int = pricesCombinations[0][i][1]

            for x in range(i, len(pricesCombinations[i])):

                for j in range(len(pricesCombinations[x])):

                    if pricesCombinations[0][i][0] < pricesCombinations[x][j][0] and x != 0 and pricesCombinations[0][i][2] < pricesCombinations[x][j][2]:

                        result += pricesCombinations[x][j][1]

                        if result > maxSum:
                            maxSum = result
                            z = pricesCombinations[0][i][1]
                            a = pricesCombinations[x][j][1]
                            result = pricesCombinations[0][i][1]
                            print(z)
                            print(a)

                    result = pricesCombinations[0][i][1]

        if maxSum > maxSum0:
            maxSum0 += maxSum

    return maxSum0

print(solution([1, 3, 2, 8, 4, 10], 2))