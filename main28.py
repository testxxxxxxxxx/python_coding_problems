def solution(text: str) -> str:

    textList: list = text.split(' ')

    textList.reverse()

    return ' '.join(textList)
    

print(solution("hello world here"))