def solution(W: str, S: str) -> list:

    result: list = []
    revW: str = W[::-1]

    for i in range(len(S)):

        if W == S[i: i + len(W)]:
            result.append(i)
        elif revW == S[i: i + len(W)]:
            result.append(i) 

    return result

print(solution("ab", "abxaba"))