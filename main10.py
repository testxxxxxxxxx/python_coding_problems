def solution(firstString: str, lastString: str) -> int:
    count: int
    it: int = 0
    numberOfLetter: int = 0
    maxLength: int
    minLength: int 

    if len(firstString) > len(lastString):
        count = len(firstString)
        minLength = len(lastString)
    else:
        count = len(lastString)
        minLength = len(firstString)

    maxLength = count

    for _ in range(count):
        if it >= minLength:
            numberOfLetter += maxLength - minLength
            break

        if firstString[it] != lastString[it]:
            numberOfLetter += 1

        it += 1

    return numberOfLetter

print(solution("kitten", "sitting"))