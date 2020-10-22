import numpy as np
import matplotlib.pyplot as plt

def point_and_a_straight_line(p1, p2, p0):
    v = np.cross(p2 - p1, p0 - p1)

    if v > 0:
        return 1
    elif v < 0:
        return 2
    else:
        return 0