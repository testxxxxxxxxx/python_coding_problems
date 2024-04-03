def findArr(arr: list, value: str) -> bool:

    index: int = len(value)

    for i in range(len(arr)):

        if arr[i] != None:

            if arr[i][0:index] == value:

                return True

    return False 

def findWordInArr(arr: list, value: str) -> bool:

    for i in arr:

        if i == value:
            return True
        
    return False

def solution(words: list) -> list:

    result: list = []
    it: int = 1
    it0: int = 1
    index: int = 0
    value: str = ''

    for i in range(1, len(words) + 1):

        it = 1
        it0 = 1

        index = i - 1

        value = words[index]

        words[index] = None

        while True: 
        
            if not findArr(words, value[0:it]) and not findArr(result, value[0:it]):
                break

            if findWordInArr(result, value):
                tempArr: list = list(value)
                tempArr.append(value[0:it0])

                it0 += 1

                value = ''

                for i in tempArr:
                    value += i

            elif len(value[0:it]) == it:
                tempArr: list = list(value)
                tempArr.append(' ')

                value = ''

                for i in tempArr:
                    value += i

            it += 1

        result.append(value[0:it].strip())

        words[index] = value

    return result

words: list = [
    
    'dog',
    'cat',
    'apple',
    'apricot',
    'fish',
    
]

print(solution(words))