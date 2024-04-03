def getVarriation(n: int) -> int:

    return pow(2, n)

def generateCode(n: int) -> str:

    result: str = ''

    for i in range(n):

        result += '0'

    return result

def add(value: str, changeElement: str, it: int) -> str:

    valueArr: list = list(value)

    if valueArr[it] != changeElement:

        valueArr[it] = changeElement

    value = ''

    for i in valueArr:

        value += i

    return value

def isInArr(item: str, arr: list) -> bool:

    for i in arr:

        if item == i:
            return False

    return True

def solution(n: int) -> list:

    results: list = []
    startCode: str = generateCode(n)
    count: int = getVarriation(n)
    changeElement: str = '1'
    it: int = n - 1
    it0: int = 1
    code: str = ''
    state: bool = True
    count0: int = 0
    count1: float = 0
    y: int = 1

    results.append(startCode)

    for i in range(count - 1):

        if it < 0:

            count0 += 1
            count1 += 0.5

            if count0 == 2:

                y += 1
                count0 = 0
            
            it = n - y

            state = not state

        if state:
            changeElement = '1'
        else:
            changeElement = '0'

        code = add(results[it0 - 1], changeElement, it)

        results.append(code)

        it -= 1
        it0 += 1

    return results

print(solution(2))