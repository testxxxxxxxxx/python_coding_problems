def solution(bits: str) -> str:

    bitsLits: list = list(bits) 
    
    for i in range(0, len(bitsLits) - 1, 2): bitsLits[i], bitsLits[i + 1] = bitsLits[i + 1], bitsLits[i]

    bits = ""

    for i in bitsLits:
        bits += i

    return bits

print(solution("11100010"))