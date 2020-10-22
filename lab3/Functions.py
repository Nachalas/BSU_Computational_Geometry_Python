import numpy as np
import matplotlib.pyplot as plt


def draw_graph(arr, arr2, points):
    arr_x = []
    arr_y = []
    for item in arr:
        arr_x.append(item[0])
        arr_y.append(item[1])
    arr_x.append(arr[0][0])
    arr_y.append(arr[0][1])
    plt.plot(arr_x, arr_y)


    arr_x2 = []
    arr_y2 = []
    for item in arr2:
        arr_x2.append(item[0])
        arr_y2.append(item[1])
    arr_x2.append(arr2[0][0])
    arr_y2.append(arr2[0][1])
    plt.plot(arr_x2, arr_y2)

    for p in points:
        plt.plot(p[0], p[1], 'ro')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.grid(True)
    plt.show()
    plt.close('all')


def octant_check(vector):
    x = vector[0]
    y = vector[1]
    if 0 <= y < x:
        return 1
    if 0 < x <= y:
        return 2
    if 0 <= -x < y:
        return 3
    if 0 < y <= -x:
        return 4
    if 0 <= -y < -x:
        return 5
    if 0 < -x <= -y:
        return 6
    if 0 <= x < -y:
        return 7
    if 0 < -y <= x:
        return 8


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


def point_and_a_straight_line(p1, p2, p0):
    v = np.cross(p2 - p1, p0 - p1)

    if v > 0:
        return 1
    elif v < 0:
        return 2
    else:
        return 0


def angle_test(p0, points):

    s = 0
    for i in range(0, len(points) - 1):
        d = octant_check(points[i + 1] - p0) - octant_check(points[i] - p0)
        if d > 4:
            d -= 8
        if d < -4:
            d += 8
        if d == 4 or d == -4:
            d1 = np.linalg.det([points[i] - p0, points[i+1] - p0])
            if d1 > 0:
                d = 4
            if d1 < 0:
                d = -4
            if d1 == 0:
                return -1  # на границе

        s += d

    if s == 8 or s == -8:
        return 1  #  в многоугольнике
    if s == 0:
        return 0  #  не в многоугольнике


def point_position_convex_polygon(p0, points):
    if point_and_a_straight_line(points[0], points[1], p0) == 2 or point_and_a_straight_line(points[0], points[-2], p0) == 1:
        return 0

    start = 0
    end = len(points)
    while end - start > 1:
        sep = (start + end) // 2
        if point_and_a_straight_line(points[0], points[sep], p0) == 1:
            start = sep
        else:
            end = sep
    if point_and_a_straight_line(points[start], points[end], p0) == 2:
        return 0
    return 1