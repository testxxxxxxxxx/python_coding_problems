def solution(parentheses: str) -> int:

    count: int = 0
    it: int = 0

    for _ in range(len(parentheses) - 1):

        if it == len(parentheses) - 1:
            break

        if parentheses[it] == '(' and parentheses[it + 1] == ')':
            count += 2 

        it += 1

    return (len(parentheses) - count)

print(solution("()())()"))