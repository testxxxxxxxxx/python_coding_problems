from random import randint

def firstGame() -> int:

    amount: int = 0
    rollAmount: int = 0
    count: int = 0

    while True:

        rollAmount = randint(1, 6)

        if count > 1:
            count = 0

        if rollAmount == 5:
            count += 1

        if rollAmount == 6 and count == 1:
            break

        amount += 1

    return amount

def secondGame() -> int:

    amount: int = 0
    rollAmount: int = 0
    count: int = 0

    while True:

        rollAmount = randint(1, 6)

        if count > 1:
            count = 0

        if rollAmount == 5 and count == 1:
            break

        if rollAmount == 5:
            count += 1

        amount += 1

    return amount

print(firstGame())
print(secondGame())