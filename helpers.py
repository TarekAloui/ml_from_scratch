import numpy as np


# Distance Functions


def euclidean_distance(x1, x2):
    """
    Calculates the euclidean distance between two points x1 and x2

    Args:
        x1: predictors for first point
        x2: predictors for second point

    Returns:
        euclidean distance between x1 and x2
    """

    return np.sqrt(np.sum(np.square(x1 - x2)))


# unit tests
if __name__ == "__main__":

    # fn: euclidean_distance
    print(euclidean_distance(np.array([0, 0]), np.array([2, 2])))  # 2.8284271247461903
    print(euclidean_distance(np.array([1, 1]), np.array([2, 2])))  # 1.4142135623730951
