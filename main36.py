def getInsertId(rods: list) -> int:

    for i in range(len(rods)):

        if rods[i] != 0:
            return i
        
    return len(rods) - 1

def toRight(rods: list, n: int, i: int = 0, it: int = 0, it0: int = 0) -> None:

    count: int = 0

    if ((rods[i][getInsertId(rods[i])] < rods[it][getInsertId(rods[it])] and rods[i][getInsertId(rods[i])] != 0) or rods[it][getInsertId(rods[it])] == 0) and i != it:

        print(i)
        print(it)

        rods[i][getInsertId(rods[i])], rods[it][getInsertId(rods[it])] = rods[it][getInsertId(rods[it])], rods[i][getInsertId(rods[i])]

        print(f'Move {i + 1} to {it + 1}')

        it -= 1
    else:
        i += 1
        it = n - 1

    if i == n:
        i = 0

    if it < 0:
        it = n - 1

    if it0 < 0:
        it0 = n - 1

    if rods[2][2] != 0 and rods[1][2] != 0:
        return

    toRight(rods, n, i, it)

def toLeft(rods: list, n: int, i: int = 0, it: int = 0) -> None:

    count: int = 0

    if ((rods[i][getInsertId(rods[i])] < rods[it][getInsertId(rods[it])] and (rods[it][getInsertId(rods[it])] - rods[i][getInsertId(rods[i])]) == 1)) and i != it:

        rods[i][getInsertId(rods[i])], rods[it][getInsertId(rods[it])] = rods[it][getInsertId(rods[it])], rods[i][getInsertId(rods[i])]

        print(f'Move {i + 1} to {it + 1}')

        it += 1
    else:
        i -= 1

    if i == 0:
        i = n - 1

    if it >= n:
        it = 0

    for j in rods[2]:

        if j != 0:
            count += 1

    if count == n:
        return

    toLeft(rods, n, i, it)

n: int = 3

rods: list = [

    [i for i in range(1, n + 1)],
    [0 for i in range(n)],
    [0 for i in range(n)]

]

toRight(rods, n, 0, n - 1)

print(rods)

toLeft(rods, n, 2)