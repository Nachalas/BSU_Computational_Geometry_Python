import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.animation as animation

# Дано: P = {p1, ..., pn}, Q = {q1, ..., qm}
# оба выпуклые
#
# Надо: аним.движения друг к другу и реализовать
# алгоритм пересечения двух выпуклых многоугольников

fig, ax = plt.subplots()

# polygon_2 = np.array([np.array([5, 10]), np.array([8, 4]), np.array([14, 4]), np.array([17, 10]), np.array([14, 13]), np.array([8, 13]), np.array([5, 10])])
# polygon_2 = np.array([np.array([4, 6]), np.array([14, 6]), np.array([14, 11]), np.array([4, 11]), np.array([4, 6])])
# polygon_2 = np.array([np.array([15, 3]), np.array([25, 3]), np.array([25, 8]), np.array([15, 8]), np.array([15, 3])])
# polygon_2 = np.array([np.array([15, 6]), np.array([25, 6]), np.array([25, 11]), np.array([15, 11]), np.array([15, 6])])
# polygon_2 = np.array([np.array([4, -5]), np.array([14, -5]), np.array([14, 0]), np.array([4, 0]), np.array([4, -5])])
# polygon_2 = np.array([np.array([4, 1]), np.array([14, 2]), np.array([9, 6]), np.array([4, 1])])
# polygon_2 = np.array([np.array([4, -1]), np.array([14, -1]), np.array([9, 4]), np.array([4, -1])])
# polygon_2 = np.array([np.array([4, 9]), np.array([14, 9]), np.array([14, 14]), np.array([4, 14]), np.array([4, 9])])
# polygon_2 = np.array([np.array([-2, 1]), np.array([8, 1]), np.array([8, 6]), np.array([-2, 6]), np.array([-2, 1])])


def is_pointed_at(a, b):
    a_start = a[0]
    a_end = a[1]
    b_start = b[0]
    b_end = b[1]
    # return (np.linalg.det([b_end - b_start, a_end - b_start]) > 0 and np.linalg.det([b_end - b_start, a_end - a_start]) < 0) or \
    #        (np.linalg.det([b_end - b_start, a_end - b_start]) < 0 and np.linalg.det([b_end - b_start, a_end - a_start]) > 0) or \
    #     np.dot(a_start - a_end, b_start - a_end) < 0
    return (np.cross(a_end - a_start, b_end - b_start) > 0 and point_and_a_straight_line(b_start, b_end, a_end) != 2) or \
           (np.cross(a_end - a_start, b_end - b_start) < 0 and point_and_a_straight_line(b_start, b_end, a_end) != 1)


def point_and_a_straight_line(p1, p2, p0):
    v = np.cross(p2 - p1, p0 - p1)
    if v > 0:
        return 1
    elif v < 0:
        return 2
    else:
        return 0


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return []

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return [x, y]


def sort_by_x(obj):
    return obj[0]


def sort_by_y(obj):
    return obj[1]


def is_point_segment(x1, x2, x0):
    by_x = sorted([x1, x2], key=sort_by_x)
    by_y = sorted([x1, x2], key=sort_by_y)
    if x0[0] < by_x[0][0] or x0[0] > by_x[1][0]:
        return 0
    if x0[1] < by_y[0][1] or x0[1] > by_y[1][1]:
        return 0
    x1x2 = x2 - x1
    x1x0 = x0 - x1
    vm = np.cross(x1x2, x1x0)
    if vm == 0 or abs(vm) < 0.000001:
        return 1
    return 0


def is_outer_segment(fs, ss):
    if point_and_a_straight_line(ss[0], ss[1], fs[1]) == 2:
        return True
    elif point_and_a_straight_line(ss[0], ss[1], fs[1]) == 0:
        if point_and_a_straight_line(ss[0], ss[1], fs[0]) == 2:
            return True
    else:
        return False


def check_point_equality(a, b):
    return a[0] == b[0] and a[1] == b[1]


def find_intersection_of_polygons(polygon_1, polygon_2):
    intersection = []
    i = 0
    j = k = 0
    for iter in range(0, len(polygon_1) - 1):
        if point_and_a_straight_line(polygon_1[iter], polygon_1[iter + 1], polygon_2[k]) == 2:
            i = iter
            break
    while k != 2*(len(polygon_1)+len(polygon_2)):
        if i == len(polygon_1) - 1:
            i = 0
        if j == len(polygon_2) - 1:
            j = 0
        segment_first = [polygon_1[i], polygon_1[i+1]] #p
        segment_second = [polygon_2[j], polygon_2[j+1]] #q
    #     Первый случай: направлены друг на друга
        if is_pointed_at(segment_first, segment_second) and is_pointed_at(segment_second, segment_first):
            if is_outer_segment(segment_first, segment_second):
                i += 1
            else:
                j += 1
    #     Второй случай:
        elif is_pointed_at(segment_first, segment_second) and is_pointed_at(segment_second, segment_first) != True:
            if is_outer_segment(segment_first, segment_second) != True:
                intersection.append(segment_first[1])
            i += 1
    #     Третий случай:
        elif is_pointed_at(segment_first, segment_second) != True and is_pointed_at(segment_second, segment_first):
            if is_outer_segment(segment_second, segment_first) != True:
                intersection.append(segment_second[1])
            j += 1
    #     Четвёртый:
        elif is_pointed_at(segment_first, segment_second) != True and is_pointed_at(segment_second, segment_first) != True:
            poi = line_intersection(segment_first, segment_second)
            if len(poi) != 0:
                if is_point_segment(polygon_1[i], polygon_1[i + 1], poi) and is_point_segment(polygon_2[j], polygon_2[j + 1], poi):
                    intersection.append(poi)
            if is_outer_segment(segment_first, segment_second):
                i += 1
            else:
                j += 1
        k += 1
    return intersection


polygon_1 = np.array([np.array([5, 12]), np.array([8, 6]), np.array([13, 6]), np.array([16, 12]), np.array([13, 18]),
                      np.array([8, 18]), np.array([5, 12])])
polygon_2 = np.array([np.array([9, 7]), np.array([12, 1]), np.array([17, 1]), np.array([20, 7]), np.array([17, 13]),
                      np.array([12, 13]), np.array([9, 7])])
polygon_3 = np.array([np.array([5, 6]), np.array([8, 0]), np.array([13, 0]), np.array([16, 6]), np.array([13, 12]),
                      np.array([8, 12]), np.array([5, 6])])


vector = np.array([1, 1])


def animate(i):
    ax.clear()
    plt.xlim(0, 22)
    plt.ylim(0, 25)

    points_p1_x = [p[0] for p in polygon_1]
    points_p1_y = [p[1] for p in polygon_1]

    points_p2_x = [p[0] for p in polygon_2]
    points_p2_y = [p[1] for p in polygon_2]

    intersection1 = find_intersection_of_polygons(polygon_1, polygon_2)
    intersection1_x = [p[0] for p in intersection1]
    intersection1_y = [p[1] for p in intersection1]

    ax.plot(points_p1_x, points_p1_y)
    ax.plot(points_p2_x, points_p2_y)
    ax.plot(intersection1_x, intersection1_y, linestyle='-', color='red')

    if i > 9 and i % 10 == 0:
        x = vector[0]
        y = vector[1]
        vector[0] = x * math.cos(math.pi/2) - y * math.sin(math.pi/2)
        vector[1] = x * math.sin(math.pi/2) + y * math.cos(math.pi/2)

    for i in range(0, len(polygon_2)):
        polygon_2[i] += vector


ani = animation.FuncAnimation(fig, animate, interval=200, repeat=False)
plt.show()
