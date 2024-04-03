import re

def solution(text: str) -> str:

    it: int = -1

    textList: list = re.split('[^a-zA-Z0-9]{1,}', text)

    delimiters: list = ['' for i in range(len(textList))]
    delimiter: str = ''
    result: str = ''

    for x in range(len(textList)):

        if textList[x] == '':
            textList.pop(x)

    for i in range(len(text)):

        if re.search('^[^a-zA-Z0-9]{1,}$', text[i]):
            if text[i] != delimiter:
                it += 1
                delimiter = ''

            delimiters[it] += text[i]
            delimiter += text[i]

    textList.reverse()

    for j in range(len(textList)):

        result += textList[j] + delimiters[j]

    return result

print(solution("hello/world:here"))