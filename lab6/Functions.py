import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm

def point_and_a_straight_line(p1, p2, p0):
    v = np.cross(p2 - p1, p0 - p1)

    if v > 0:
        return 1
    elif v < 0:
        return 2
    else:
        return 0

def triangle_area(a, b, c):
    return 0.5 * norm(np.cross(b - a, c - a))