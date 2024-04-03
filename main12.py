from multiset import Multiset

def getSum0(numbers: Multiset) -> int:

    result: int = 0

    for i in numbers:
        result += i

    return result

def solution0(numbers: Multiset) -> list | None:

    maxSum: int = int(getSum0(numbers) / 2)
    subArr: Multiset = Multiset()
    subArrResult: list = []
    it: int = 0
    result: int = 0

    for i in numbers:

        if result <= maxSum:
            result += i
            subArr.add(i)

            if result == maxSum:
                subArrResult.append(subArr)
                subArr = Multiset()
                result = 0

        it += 1

    if len(subArrResult) == 2:
        return subArrResult
    
    return None

numbers = [15, 5, 20, 10, 35, 15, 10]

numbers.sort()

print(solution0(Multiset(numbers)))