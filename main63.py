def replaceStr(s: str, index: int, removeIndex: int) -> str:

    tmpS: str = ''

    for i in range(len(s)):

            if i >= index and i <= removeIndex:
                tmpS += " "
            else:
                tmpS += s[i]

    return tmpS

def solution(s: str, words: list) -> list:

    index: int = -1
    results: list = []
    index: int = -1
    searchedWords: list = []
    result: str = ''

    for i in range(len(words)):
         
        result += words[i] 

        for j in range(len(words)):

            if words[j] != words[i]:
                result += words[j]

        searchedWords.append(result)

        result = ''

    for i in searchedWords:

        while s.find(i) != -1:

            if s.find(i) != -1:

                index: int = s.find(i)

                results.append(index)

                removeIndex: int = index + len(words)

                s = replaceStr(s, index, removeIndex)

    return results

s: str = 'dogcatcatcodecatdog'
words: list = ["cat", "dog"]

print(solution(s, words))