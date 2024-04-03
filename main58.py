def notBits(x: int) -> int:

    return int(not x)

def solution(binaryNumber: int) -> str:

    binaryNumberStr: str = str(binaryNumber)
    result: str = ''

    for i in range(len(binaryNumberStr)):

        binary: int = int(binaryNumberStr[i])

        binary = notBits(binary)

        result += str(binary)

    return result

print(solution(11110000111100001111000011110000))