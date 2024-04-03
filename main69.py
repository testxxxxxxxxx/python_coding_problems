from random import randint

def silnia(n: int) -> int:

    if n <= 1:
        return 1
    
    return n * silnia(n - 1)

def computeCombinations(k: int, n: int) -> int:

    result: int = silnia(n) // (silnia(n - k) * silnia(k))

    return result

def solution(sets: list) -> list:

    setList: list = sets
    firstSetResults: list = []
    secondSetResults: list = []
    choosenIndex: list = []

    length: int = len(setList) // 2

    numberOfCombinations: int = computeCombinations(2, len(setList))

    firstSet: set = set()
    secondSet: set = set()

    for x in range(len(setList)):

        length = x
        numberOfCombinations = computeCombinations(x, len(setList))

        for i in range(numberOfCombinations):

            firstSet = set()

            while firstSet in firstSetResults:

                randomNumber: int = 0
                choosenIndex = []
                firstSet: set = set()

                while True:

                    randomNumber = randint(0, len(setList) - 1)

                    if randomNumber not in choosenIndex:
                        choosenIndex.append(randomNumber)
                        firstSet.add(setList[randomNumber])

                    if len(choosenIndex) == length:
                        break

            firstSetResults.append(firstSet)

    for i in range(len(firstSetResults)):

        secondSet: set = set()

        for j in range(len(setList)):

            if setList[j] not in firstSetResults[i]:
                secondSet.add(setList[j])

        secondSetResults.append(secondSet) 

    print(firstSetResults)
    print(secondSetResults)        

    minDiff: int = sum(setList)
    firstSet0: set = set()
    secondSet0: set = set()

    for i in range(len(firstSetResults)):

        sumFirst: int = sum(firstSetResults[i])
        sumSecond: int = sum(secondSetResults[i])

        if sumFirst > sumSecond:
            result: int = sumFirst - sumSecond
        else:
            result: int = abs(sumSecond - sumFirst)

        if result < minDiff:
            minDiff = result
            firstSet0 = firstSetResults[i]
            secondSet0 = secondSetResults[i]

    return [firstSet0, secondSet0]

print(solution([5, 10, 15, 20, 25]))