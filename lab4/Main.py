import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

from numpy.linalg import norm

from Functions import point_and_a_straight_line

fig, ax = plt.subplots()


def sort_method(point):
    i = np.array([1, 0])
    v = np.array(point - start_point)
    if (math.sqrt(v[1] * v[1] + v[0] * v[0])) == 0:
        return 1
    #print((v.dot(i)) / (math.sqrt(v[1] * v[1] + v[0] * v[0])))
    return (v.dot(i)) / (math.sqrt(v[1] * v[1] + v[0] * v[0]))


points = np.array(
    [np.array([8, 8]), np.array([2, 9]), np.array([3, 2]), np.array([1, 1]), np.array([5, 3]), np.array([6, 8]),
     np.array([2, 6]), np.array([7, 5]),
     np.array([4, 5]), np.array([4, 4]), np.array([3, 3]), np.array([6, 7]), np.array([5, 8]), np.array([3, 5]),
     np.array([6, 10])])

# points = np.array(
#     [np.array([1, 1]), np.array([5, 1]), np.array([5, 5]), np.array([1, 5])])

# points = np.array(
#     [np.array([1, 1]), np.array([5, 1]), np.array([5, 5]), np.array([5, 10]), np.array([1, 10]), np.array([1, 5])])


start_point = np.array(min(points, key=lambda p: p[1]))

rez = sorted(points, key=sort_method, reverse=True)

convex_hull = [start_point, rez[1]]

points_x = [p[0] for p in points]
points_y = [p[1] for p in points]


def animate(i):
    xs = []
    ys = []
    while point_and_a_straight_line(convex_hull[-2], convex_hull[-1], rez[i]) == 2:
        convex_hull.pop()
    # if convex_hull[len(convex_hull) - 1][0] == rez[i][0] and convex_hull[len(convex_hull) - 1][1] == rez[i][1]:
    #     convex_hull.pop()
    convex_hull.append(rez[i])

    xs = [p[0] for p in convex_hull]
    ys = [p[1] for p in convex_hull]

    ax.clear()
    l1 = ax.scatter(points_x, points_y, marker='o', linestyle='-', color='blue')
    ax.plot(xs, ys, marker='o', linestyle='-', color='red')
    if i == len(points) - 1:
        plt.plot([convex_hull[-1][0]] + [convex_hull[0][0]], [convex_hull[-1][1]] + [convex_hull[0][1]],
                 marker='o', linestyle='-', color='red')


ani = animation.FuncAnimation(fig, animate, frames=range(2, len(points)), interval=100, repeat=False)
plt.show()
