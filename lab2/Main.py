import Functions as bf
import numpy as np


p1 = np.array([1, 1])
p2 = np.array([2, 4])
p3 = np.array([2, 1])
p4 = np.array([2.5, 2])
p5 = np.array([3, 2])
p6 = np.array([3.5, 1])
p7 = np.array([4, 2])
p8 = np.array([5, 3])
p9 = np.array([6, 3])
p10 = np.array([5, 0])
polygon = [p10, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
p0 = np.array([3, 1])


def point_and_a_polygon(point,  *args):

    x = []
    y = []
    for i in range(len(args)):
        x.append(args[i][0])
        y.append(args[i][1])
    if p0[0] < min(x) or p0[0] > max(x) or p0[1] > max(y) or p0[1] < min(y):
        return 0
    q0 = np.array([min(x)-1, p0[1]])
    bf.print_polygon(p0, q0, *polygon)

    s = 0
    i = 1
    while i < len(args) - 1:
        if bf.is_point_segment(args[i], args[i+1], point):
            return 1
        if bf.segments_intersection_without_output(q0, point, args[i], args[i+1]):
            if bf.is_point_segment(q0, point, args[i]) == 0 and bf.is_point_segment(q0, point, args[i+1]) == 0:
                s += 1
            elif bf.is_point_segment(q0, point, args[i]):
                k = 0
                while bf.is_point_segment(q0, point, args[i+k]):
                    k += 1
                if bf.point_and_a_straight_line_without_output(q0, point, args[i - 1]) != bf.point_and_a_straight_line_without_output(q0, point, args[i+k]):
                    s += 1
                i += k - 1
        i += 1

    if s % 2 == 0:
        return 0
    else:
        return 1


print(point_and_a_polygon(p0, *polygon))
