numbers: list = [10, 5, 7]

def solution(numbers: list) -> bool:

    it: int = 1
    count: int = 0

    for _ in range(len(numbers) - 1):

        if numbers[it - 1] > numbers[it]:
            count += 1

        it += 1

    if count > 1:
        return False

    return True

print(solution(numbers))