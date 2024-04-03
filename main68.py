def solution(numbers: list) -> int:

    maxDenominator: int = 1
    count: int = 0

    for i in range(len(numbers)):

        count = 0

        for j in range(len(numbers)):

            if numbers[j] % numbers[i] == 0:
                count += 1

            if count == len(numbers):
                maxDenominator = numbers[i]

    return maxDenominator

print(solution([42, 56, 14]))