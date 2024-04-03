def solution(field: list) -> int:

    steps: int = 0

    for i in range(len(field) - 1):

        if field[i][0] == field[i + 1][0] + 1 and field[i][1] == field[i + 1][1] or field[i][0] == field[i + 1][0] - 1 and field[i][1] == field[i + 1][1] or field[i][0] == field[i + 1][0] and field[i][1] == field[i + 1][1] + 1 or field[i][0] == field[i + 1][0] and field[i][1] == field[i + 1][1] - 1 or field[i][0] == field[i + 1][0] - 1 and field[i][1] == field[i + 1][1] - 1 or field[i][0] == field[i + 1][0] - 1 and field[i][1] == field[i + 1][1] + 1 or field[i][0] == field[i + 1][0] + 1 and field[i][1] == field[i + 1][1] -1:
            steps += 1
        else:
            steps -= 1

    return steps

print(solution([(0, 0), (1, 1), (1, 2)]))