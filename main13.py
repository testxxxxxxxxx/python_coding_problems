def solution(text: str, k: int) -> list:

    resultArr: list = []
    it: int = 0
    it0: int = 0
    word: str = ''
    left: int = 0
    length: int = 0
    maxLength: int = 0

    for _ in range(len(text)):

        if text[it] == ' ' and len(text[left : it]) <= k:
            word += text[left : it]
            left += len(text[left : it])
            length = len(word)

            if length > maxLength:
                maxLength = length

            if it0 <= k and maxLength <= k:
                resultArr.append(word)
                word = ''
                it0 = 0

            print(word)

        it += 1
        it0 += 1

    return resultArr

print(solution("the quick brown fox jumps over the lazy dog", 10))