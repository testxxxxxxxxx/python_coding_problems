def solution(A: str, B: str) -> bool:

    result: str = ""
    textCopyA: list= list(A)

    for i in range(len(A)):

        for j in range(len(A)):
            
            textCopyA[i], textCopyA[j] = textCopyA[j], textCopyA[i]

            result = "".join(textCopyA)

        if result == B:
            return True

    return False

print(solution("abcde", "cdeab"))            