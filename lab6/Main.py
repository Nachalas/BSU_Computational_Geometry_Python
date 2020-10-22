import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
import random
from Functions import point_and_a_straight_line, triangle_area
from data import points, vectors
import matplotlib.animation as animation
from itertools import groupby

fig, ax = plt.subplots()


def perimeter(a):
    p = 0
    for i in range(0, len(a) - 1):
        p += norm([a[i + 1][0] - a[i][0], a[i + 1][1] - a[i][1]])
    p += norm([a[-1][0] - a[0][0], a[-1][1] - a[0][1]])
    return p


def quick_hull_helper(left, right, set, hull):
    temp = 0
    sep = np.array([0, 0])# самая удаленная от основания lowest, higthrst
    for i in set:
        area = triangle_area(left, right, i)
        if area > temp:
            temp = area
            sep = i
    s_l = []
    s_r = []
    for i in set:
        if point_and_a_straight_line(left, sep, i) == 1:
            s_l.append(i)
        elif point_and_a_straight_line(sep, right, i) == 1:
            s_r.append(i)
    if len(s_l) != 0:
        quick_hull_helper(left, sep, s_l, hull)
    hull.append(sep)
    # else:
    #     if hull[-1][0] != sep[0] or hull[-1][1] != sep[1]:
    #         hull.append(sep)
    if len(s_r) != 0:
        quick_hull_helper(sep, right, s_r, hull)
        hull.append(right)
    # else:
    #     if hull[-1][0] != sep[0] or hull[-1][1] != sep[1]:
    #         hull.append(sep)


def quick_hull(array):
    hull = []
    lowest_point = np.array(min(array, key=lambda p: p[1]))
    highest_point = np.array(max(array, key=lambda p: p[1]))
    # print(highest_point)
    # print(lowest_point)
    s_l = []
    s_r = []
    for i in array:
        if point_and_a_straight_line(lowest_point, highest_point, i) == 1:
            s_l.append(i)
        elif point_and_a_straight_line(lowest_point, highest_point, i) == 2:
            s_r.append(i)
    # print(len(s_l))
    # print(len(s_r))
    hull.append(lowest_point)
    if len(s_l) != 0:
        quick_hull_helper(lowest_point, highest_point, s_l, hull)
    hull.append(highest_point)
    if len(s_r) != 0:
        quick_hull_helper(highest_point, lowest_point, s_r, hull)
    return hull

#
# quick_hull(points)
# print(hull)
# points_x = [p[0] for p in hull]
# points_y = [p[1] for p in hull]
# points_x.append(hull[0][0])
# points_y.append(hull[0][1])
# ax.plot(points_x, points_y, marker='o', linestyle='-', color='red')
# plt.show()


p_const = 40


def animate(i):
    indexes = []
    ax.clear()
    points_x = [p[0] for p in points]
    points_y = [p[1] for p in points]
    l1 = ax.scatter(points_x, points_y, marker='o', linestyle='-', color='blue')
    hull = quick_hull(points)
    size = len(hull)
    i = 0
    while i != size - 1:
        if hull[i][0] == hull[i + 1][0] and hull[i][1] == hull[i + 1][1]:
            del hull[i]
            i -= 1
            size -= 1
        i += 1
    print(hull)
    for i in range(0, len(hull)):
        indexes.append(points.tolist().index(hull[i].tolist()))
    hull_x = [p[0] for p in hull]
    hull_x.append(hull[0][0])
    hull_y = [p[1] for p in hull]
    hull_y.append(hull[0][1])

    plt.xlim(-5, 19)
    plt.ylim(-5, 19)

    ax.plot(hull_x, hull_y, marker='o', linestyle='-', color='red')

    if perimeter(hull) > p_const:
        for i in indexes:
            vectors[i] = vectors[i] * (-1)
            l2 = ax.arrow(points[i][0], points[i][1], vectors[i][0], vectors[i][1], width=0.05)
    for i in range(0, len(points)):
        points[i] += vectors[i]


ani = animation.FuncAnimation(fig, animate, interval=1000, repeat=False)
plt.show()
