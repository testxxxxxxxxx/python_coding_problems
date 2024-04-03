def solution(text: str) -> bool:

    count: int = 0
    results: list = []
    result: str = ''
    textArr: list = list(text)

    for i in range(len(textArr)//2):

        if (textArr[i] == '(' or textArr[i] == '*') and (textArr[len(textArr) - 1 - i] == ')' or textArr[len(textArr) - 1 - i]):
            result = f'{text[i]}{text[len(text) - 1 - i]}'
            textArr[i] = ''
            textArr[len(textArr) - 1 - i] = ''
            results.append(result)

    for j in range(len(results)):

        if (results[j][0] == '(' or results[j][0] == '*') and (results[j][1] == ')' or results[j][1] == '*'):
            count += 1

    if count != len(results):
        return False
    
    for x in range(len(textArr)):

        if textArr[x] == '(' or textArr[x] == ')':
            return False

    return True

print(solution('(()*'))