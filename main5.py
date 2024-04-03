from random import random

elements = [1, 2, 4, 6, 10]

def randomProbability(stream):
    streamCount: int = 0
    selected: int = 0

    it: int = 0

    for _ in range(len(stream)):

        streamCount += 1

        if streamCount == 0:
                selected = elements[it]
        elif random() <= 1 / streamCount:
                selected = elements[it]

        it += 1

    return selected

print(randomProbability(elements))