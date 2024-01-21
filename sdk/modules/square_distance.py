import numpy as np


def square_distance(p1: list[np.float32], p2: list[np.float32]) -> np.float32:
    if not all(isinstance(x, (int, np.float32)) for x in p1) or not all(isinstance(x, (int, np.float32)) for x in p2):
        raise ValueError("Both p1 and p2 must be arrays or lists of numbers")

    return np.float32(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2 +
        (p1[2] - p2[2]) ** 2
    )
