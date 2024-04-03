from random import random
from typing import Tuple

def coordinate_gen() -> Tuple[float, float]:
    return random(), random()

def pi_approx(iterations: int = 1_000_000) -> float:
    circle_area = 0
    for _ in range(iterations):
        x, y = coordinate_gen()
        if pow(x, 2) + pow(y, 2) <= 1:
            circle_area += 1

    return round(4 * circle_area / iterations, 3)

if __name__ == '__main__':
    print(pi_approx())