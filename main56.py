def findArr(value: str, arr: list) -> bool:

    for i in arr:

        if value == i:
            return True
        
    return False

def solution(text: str) -> str | None:

    keys: list = []
    values: list = [1 for i in range(len(set(text)))]
    index: int = -1
    isFirst: list = [-1 for i in range(len(set(text)))]
    it: int = -1

    for i in range(1 ,len(text)):

        if text[i - 1] == text[i]:
            return text[i - 1]
        
    for j in range(len(text)):

        if findArr(text[j], keys):
            it += 1
            index = keys.index(text[j])
            values[index] += 1
            isFirst[index] = it
        else:
            keys.append(text[j])

    for x in range(len(isFirst)):

        if isFirst[x] == 0:
            return keys[x]
        
    return None

print(solution("acbbac"))