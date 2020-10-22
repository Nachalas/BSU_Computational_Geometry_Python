import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()

polygon_1 = np.array([np.array([3, 9]), np.array([6, 3]), np.array([12, 3]), np.array([15, 9]), np.array([12, 12]),
                      np.array([6, 12]), np.array([3, 9])])
# Две точки пересечения
segment1 = [np.array([4, 3.5]), np.array([13, 3.5])]
segment2 = [np.array([4, 5]), np.array([8, 7])]
segment3 = [np.array([4, 14]), np.array([16, 8])]
segment4 = [np.array([2, 6]), np.array([13, 11])]
segment5 = [np.array([12, 8]), np.array([15, 6])]
# Параллельно стороне
segment6 = [np.array([3, 9]), np.array([14, 9])]
segment7 = [np.array([4, 3]), np.array([14, 3])]
segment8 = [np.array([12, 3]), np.array([15, 9])]
# Одна точка пересечения
segment9 = [np.array([3, 1]), np.array([3, 13])]
# Не пересекает
segment10 = [np.array([4, 13]), np.array([13, 13])]
segment11 = [np.array([3, 12]), np.array([13, 17])]
segment12 = [np.array([13, 3]), np.array([16, 9])]

segments = np.array([segment1, segment2, segment3, segment10, segment4, segment5, segment9, segment6, segment8,
                     segment11,  segment7, segment12])


def point_and_a_straight_line(p1, p2, p0):
    v = np.cross(p2 - p1, p0 - p1)

    if v > 0:
        return 1
    elif v < 0:
        return 2
    else:
        return 0


def find_crossing_parameter(line1, line2):
    normal = [line1[1][1] - line1[0][1],
              -(line1[1][0] - line1[0][0])]
    numerator = -1 * np.dot(normal, line2[0] - line1[0])
    denominator = np.dot(normal, line2[1] - line2[0])
    if denominator != 0:
        t = numerator/denominator
        return t
    else:
        return None


def is_potentially_entering(segment, polygon_segment):
    polygon_segment_first = polygon_segment[0]
    polygon_segment_second = polygon_segment[1]
    segment_first = segment[0]
    segment_second = segment[1]
    normal = [polygon_segment_second[1] - polygon_segment_first[1],
              -(polygon_segment_second[0] - polygon_segment_first[0])]
    segment_vector = [segment_second[0] - segment_first[0],
                      segment_second[1] - segment_first[1]]
    if np.dot(segment_vector, normal) < 0:
        return True
    else:
        return False


def check_point_equality(a, b):
    return a[0] == b[0] and a[1] == b[1]


def find_clipping(polygon, segment):
    t_0 = 0
    t_1 = 1
    for i in range(0, len(polygon) - 1):
        intersection_parameter = find_crossing_parameter(np.array([polygon[i], polygon[i+1]]), segment)
        if intersection_parameter is None:
            if point_and_a_straight_line(polygon[i], polygon[i+1], segment[0]) != 1:
                return None
        else:
            if is_potentially_entering(segment, [polygon[i], polygon[i+1]]):
                t_0 = max(intersection_parameter, t_0)
            else:
                t_1 = min(intersection_parameter, t_1)
    return t_0, t_1


def animate(i):
    ax.clear()
    plt.xlim(0, 16)
    plt.ylim(0, 15)

    polygon_1_x = [p[0] for p in polygon_1]
    polygon_1_y = [p[1] for p in polygon_1]

    segment = segments[i]
    segment_x = [segment[0][0], segment[1][0]]
    segment_y = [segment[0][1], segment[1][1]]

    color = 'blue'
    t1, t0 = None, None
    if find_clipping(polygon_1, segment) is not None:
        t0, t1 = find_clipping(polygon_1, segment)
        if t0 > t1:
            t1, t0 = None, None
            print("No intersection")
            color = "black"
    else:
        print("No intersection")
        color = "black"

    for i in range(0, len(segments)):
        # arr_x.append([p[0] for p in segments[i]])
        # arr_y.append([p[1] for p in segments[i]])
        arr_x = [p[0] for p in segments[i]]
        arr_y = [p[1] for p in segments[i]]
        ax.plot(arr_x, arr_y, color='orchid')
    ax.plot(polygon_1_x, polygon_1_y, linestyle='-', color='blue')
    ax.plot(segment_x, segment_y, color=color)

    if t1 is not None and t0 is not None:
        first_inter_p = segment[0] * (1 - t0) + segment[1] * t0
        second_inter_p = segment[0] * (1 - t1) + segment[1] * t1
        intersection_x = [first_inter_p[0], second_inter_p[0]]
        intersection_y = [first_inter_p[1], second_inter_p[1]]
        ax.plot(intersection_x, intersection_y, linestyle='-', color='red')
        ax.scatter(intersection_x, intersection_y, marker='o', linestyle='-', color='red')


ani = animation.FuncAnimation(fig, animate, frames=range(0, len(segments)), interval=1000, repeat=True)
plt.show()
