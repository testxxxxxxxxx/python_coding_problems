def solution(numbers: list) -> list:

    for i in range(len(numbers)):

        numbers[i] = numbers[i]**2

    numbers.sort()

    return numbers

print(solution([-9, -2, 0, 2, 3]))