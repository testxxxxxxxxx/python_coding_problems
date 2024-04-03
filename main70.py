from random import randint

def silnia(n: int) -> int:

    if n <= 1:
        return 1
    
    return n * silnia(n - 1)

def computeCombinations(k: int, n: int) -> int:

    result: int = silnia(n) // (silnia(n - k) * silnia(k))

    return result

def findArr(arr: list, value: int) -> bool:

    for i in arr:

        if i == value:
            return True
        
    return False

def solution(sets: list) -> list:

    setList: list = sets.copy()
    firstSetResults: list = []
    secondSetResults: list = []
    length: int = 1
    firstSet: set = set()
    secondSet: set = set()
    choosenIndex: list = []

    while length < len(setList):

        for i in range(len(setList)):

            choosenIndex = []

            for x in range(len(setList)):

                firstSet.add(setList[i])

                if length >= 3:
                    choosenIndex.append(x)

                for j in range(len(setList)):

                    if not findArr(choosenIndex, j) and setList[j] != setList[i]:
                        firstSet.add(setList[j])
                        if length < 3:
                            choosenIndex.append(j)

                    if len(firstSet) == length:
                        break

                if firstSet not in firstSetResults:

                    firstSetResults.append(firstSet)
                
                firstSet = set()
        
        length += 1

    for i in range(len(firstSetResults)):

        secondSet: set = set()

        setList = sets.copy()

        for j in range(len(setList)):

            if setList[j] not in firstSetResults[i]:
                secondSet.add(setList[j])

        secondSetResults.append(secondSet)        

    minDiff: int = sum(setList)
    firstSet0: set = set()
    secondSet0: set = set()

    for i in range(len(firstSetResults)):

        sumFirst: int = sum(firstSetResults[i])
        sumSecond: int = sum(secondSetResults[i])

        if sumFirst > sumSecond:
            result: int = sumFirst - sumSecond
        else:
            result: int = sumSecond - sumFirst

        if result < minDiff:
            minDiff = result
            firstSet0 = firstSetResults[i]
            secondSet0 = secondSetResults[i]

    return [firstSet0, secondSet0]

print(solution([5, 10, 15, 20, 25]))