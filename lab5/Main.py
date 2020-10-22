import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from numpy.linalg import norm


def point_and_a_straight_line(p1, p2, p0):
    v = np.cross(p2 - p1, p0 - p1)

    if v > 0:
        return 1  # левее
    elif v < 0:
        return 2  # правее
    else:
        return 0  # на прямой


fig, ax = plt.subplots()

points = np.array([
      np.array([8, 8]), np.array([2, 9]), np.array([3, 2]), np.array([1, 1]), np.array([5, 3]), np.array([6, 8]),
      np.array([2, 6]), np.array([7, 5]), np.array([5, 5]), np.array([10, 10]), np.array([4, 8]),
      np.array([4, 5]), np.array([4, 4]), np.array([3, 3]), np.array([6, 7]), np.array([5, 8]), np.array([3, 5]),
      np.array([6, 10])
      ])

vectors = np.array([
      np.array([1, 2]), np.array([2, 1]), np.array([2, 1]), np.array([3, 1]), np.array([-2, 1]),
      np.array([2, 1]), np.array([1, 1]), np.array([-2, -2]), np.array([-1, 1]), np.array([2, 2]),
      np.array([1, 1]), np.array([-1, 1]), np.array([-1, -3]), np.array([-2, -1]),
      np.array([-1, -1]), np.array([3, 1]), np.array([1, 3]), np.array([-1, -3])
    ])

# vectors = np.array([
#      np.array([1, 1]), np.array([1, 1]), np.array([1, 1]), np.array([1, 1]), np.array([1, 1]),
#      np.array([2, 1]), np.array([1, 1]), np.array([1, 1]), np.array([1, 1]), np.array([1, 1]),
#      np.array([1, 1]), np.array([1, 1]), np.array([1, 1]), np.array([1, 1]),
#      np.array([1, 1]), np.array([1, 1]), np.array([1, 3]), np.array([1, 1])
#    ])

# vectors = np.array([
#       np.array([1, 2]), np.array([-1, 1]), np.array([3, 1]), np.array([0, -2]), np.array([2, 0]),
#       np.array([2, 1]), np.array([2, -1]), np.array([2, -1]), np.array([2, 4]), np.array([-2, 1]),
#       np.array([3, 1]), np.array([-1, 3]), np.array([2, -3]), np.array([-3, -1]),
#       np.array([1, 2]), np.array([1, -1]), np.array([1, 3]), np.array([1, 0])
#     ])


def triangle_area(a, b, c):
    return 0.5 * norm(np.cross(b - a, c - a))


def find_diameter(hull):
    i = 0
    d0 = 0
    while triangle_area(hull[0], hull[-1], hull[i + 1]) > triangle_area(hull[0], hull[-1], hull[i]):
        i += 1
    start = i
    k = start
    j = 0
    while j < len(hull):
        while k < len(hull) - 1 and triangle_area(hull[j], hull[j + 1], hull[k]) <= \
                triangle_area(hull[j], hull[j + 1], hull[k + 1]):
            k += 1
        end = k
        for i in range(start, end):
            if norm(hull[j] - hull[i]) > d0:
                d0 = norm(hull[j] - hull[i])
        j += 1
        start = end
        if k == len(hull) - 1:
            break
    return d0


def jarvis_hull(array):
    start_point = np.array(min(array, key=lambda p: p[1]))
    convex_hull = [start_point]
    while True:
        if convex_hull[-1][0] == array[0][0] and convex_hull[-1][1] == array[0][1]:
            right = 1
        else:
            right = 0
        for i in range(0, len(array)):
            if point_and_a_straight_line(convex_hull[-1], array[right], array[i]) == 2:
                right = i
        if array[right][0] == convex_hull[0][0] and array[right][1] == convex_hull[0][1]:
            break
        else:
            convex_hull.append(array[right])
    return convex_hull


d_const = 20


def animate(i):
    hull_x = []
    hull_y = []
    ax.clear()
    points_x = [p[0] for p in points]
    points_y = [p[1] for p in points]
    l1 = ax.scatter(points_x, points_y, marker='o', linestyle='-', color='blue')

    convex_hull = jarvis_hull(points)
    hull_x = [p[0] for p in convex_hull]
    hull_x.append(convex_hull[0][0])
    hull_y = [p[1] for p in convex_hull]
    hull_y.append(convex_hull[0][1])
    ax.plot(hull_x, hull_y, marker='o', linestyle='-', color='red')

    diameter = find_diameter(convex_hull)
    print(diameter)
    if diameter > d_const:
        for v in vectors:
            v *= -1
    for i in range(len(points)):
        points[i] += vectors[i]


ani = animation.FuncAnimation(fig, animate, interval=100, repeat=False)
plt.show()
