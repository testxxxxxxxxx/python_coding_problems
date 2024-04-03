def solution(sets: list) -> list:
    
    def findArr0(arr: list, value: int) -> bool:

        for i in arr:

            if i[0] == value:
                return True
            
        return False
    
    def sort(arr: list) -> None:

        for i in range(len(arr)):

            for j in range(1, len(arr) - i):

                if len(arr[j - 1][1]) < len(arr[j][1]):
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]

    def findDuplicates(arr: list, arr0: list) -> bool:

        for i in range(len(arr)):

            for j in range(len(arr0)):

                if arr[i] == arr0[j]:
                    return True
                    
        return False

    possibleP: list = []
    result: list = []

    for i in range(len(sets)):
        
        if not findArr0(possibleP, sets[i][0]):

            possibleP.append((sets[i][0], []))

        if not findArr0(possibleP, sets[i][1]):

            possibleP.append((sets[i][1], []))
            
    for i in range(len(possibleP)):

        for j in range(len(sets)):

            if possibleP[i][0] >= sets[j][0] and possibleP[i][0] <= sets[j][1]:
                possibleP[i][1].append(j)

    sort(possibleP)

    tempArr: list = []

    for i in range(len(possibleP)):

        result.append([])
        tempArr.append([])
        result[i].append(possibleP[i][0])
        tempArr[i] += possibleP[i][1]

        for j in range(len(possibleP)):

            if not findDuplicates(tempArr[i], possibleP[j][1]):

                result[i].append(possibleP[j][0])
                tempArr[i] += possibleP[j][1]

            if len(sets) == len(tempArr[i]): 
                break

    finalResult: list = []

    minResult: int = len(result)
    minIndex: int = -1

    for i in range(len(result)):

        if len(result[i]) < minResult:
            minResult = len(result[i])
            minIndex = i

    finalResult = result[minIndex]

    finalResult.sort()

    return finalResult

print(solution([(1, 4), (4, 5), (7, 9), (9, 12)]))