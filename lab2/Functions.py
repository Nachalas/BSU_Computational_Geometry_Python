import numpy as np
import matplotlib.pyplot as plt


def print_polygon(p0, q, *args):
    x = []
    y = []
    for i in range(0, len(args), 1):
        x.append(args[i][0])
        y.append(args[i][1])
    x.append(x[0])
    y.append(y[0])
    plt.plot(x, y, 'b', [p0[0], q[0], p0[0]], [p0[1], q[1], p0[1]], 'ro')
    plt.annotate('  q', q)
    plt.annotate('  p', p0)
    plt.grid(True)
    plt.show()


def point_and_a_straight_line_without_output(p1, p2, p0):
    v = np.cross(p2 - p1, p0 - p1)
    if v > 0:
        return 1
    elif v < 0:
        return 2
    else:
        return 0


def is_point_segment(x1, x2, x0):
    x = [x1[0], x2[0]]
    x.sort()
    if x0[0] < x[0] or x0[0] > x[1]:
        return 0
    x1x2 = x2 - x1
    x1x0 = x0 - x1
    vm = np.cross(x1x2, x1x0)
    if vm == 0:
        return 1
    return 0


def segments_intersection_without_output(p1, p2, p3, p4):
    d1 = np.cross(p4 - p3, p1 - p3)
    d2 = np.cross(p4 - p3, p2 - p3)
    d3 = np.cross(p2 - p1, p3 - p1)
    d4 = np.cross(p2 - p1, p4 - p1)

    c1 = np.dot(p3 - p1, p4 - p1)
    c2 = np.dot(p3 - p2, p4 - p2)
    c3 = np.dot(p1 - p3, p2 - p3)
    c4 = np.dot(p1 - p4, p2 - p4)

    if all([d1, d2, d3, d4, 0]):
        if c1 < 0 or c2 < 0 or c3 < 0 or c4 < 0:
            return 1
        else:
            return 0
    else:
        if d1 * d2 <= 0 and d3 * d4 <= 0:
            return 1
        else:
            return 0


def polygon_simplicity(arr, draw):
    length = len(arr)
    i = 0
    flag = 0
    while i < length - 1:
        j = i + 2
        while j < length - 1:
            if i == 0 and j == length - 2:
                j += 1
                continue
            rez = segments_intersection(arr[i], arr[i + 1], arr[j], arr[j + 1], 0)
            if rez == 1:
                flag = 1
                break
            j += 1
        if flag == 1:
            break
        i += 1
    if flag == 1:
        print("not simple")
    else:
        print("simple")
    if draw == 1:
        arr_x = []
        arr_y = []
        for item in arr:
            arr_x.append(item[0])
            arr_y.append(item[1])
        arr_x.append(arr[0][0])
        arr_y.append(arr[0][1])
        plt.plot(arr_x, arr_y)

        plt.xlabel(r'$x$')
        plt.ylabel(r'$y$')
        plt.grid(True)
        plt.show()

    return flag