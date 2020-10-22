import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import random

fig, ax = plt.subplots()

# points = np.array([np.array([1, 1]), np.array([2, 4]), np.array([4, 3]), np.array([6, 5]), np.array([8, 3])])
# points = np.array([np.array([1, 1]), np.array([5, 5]), np.array([10, 1])])
# points = np.array([np.array([1, 1]), np.array([10, 10]), np.array([1, 10]), np.array([10, 1])])
# points = np.array([np.array([1, 1]), np.array([10, 1]), np.array([10, 10]), np.array([1, 10]), np.array([1, 1])])
points = []
for i in range(5):
    x = random.randint(1, 30)
    y = random.randint(1, 30)
    point = np.array([x, y])
    points.append(point)
    for i in range(0, len(points) - 1):
        if points[i][0] == points[-1][0] and points[i][1] == points[-1][1]:
            points.pop()

segments = []

for i in range(0, len(points) - 1):
    segments.append([points[i], points[i+1]])


def find_point_with_parameter(line, parameter):
    return line[0] * (1 - parameter) + line[1] * parameter


def recursive(segments, parameter):
    if len(segments) == 1:
        return find_point_with_parameter(segments[0], parameter)
    new_points = []
    for i in segments:
        new_points.append(find_point_with_parameter(i, parameter))
    new_segments = []
    for i in range(0, len(new_points) - 1):
        new_segments.append([new_points[i], new_points[i + 1]])
    xs = []
    ys = []
    for i in new_segments:
        xs.append(i[0][0])
        xs.append(i[1][0])
        ys.append(i[0][1])
        ys.append(i[1][1])
    plt.plot(xs, ys)
    return recursive(new_segments, parameter)


# i = 0
# curve = []
# while not i > 1.01:
#     new_point = recursive(segments, i)
#     curve.append(new_point)
#     i += 0.01
# xsc = [p[0] for p in curve]
# ysc = [p[1] for p in curve]

curve = []
counter = 0
old_point = points[0]
def animate(i):
    plt.clf()
    global segments
    global curve
    xs = []
    ys = []
    for j in segments:
        xs.append(j[0][0])
        xs.append(j[1][0])
        ys.append(j[0][1])
        ys.append(j[1][1])
    plt.plot(xs, ys)
    global counter
    global old_point
    new_point = recursive(segments, counter)
    plt.scatter(new_point[0], new_point[1])
    curve.append(new_point)
    # plt.plot([old_point[0], new_point[0]], [old_point[1], new_point[1]], color='red')
    # old_point = new_point
    xsc = []
    ysc = []
    for j in curve:
        xsc.append(j[0])
        ysc.append(j[1])
    plt.plot(xsc, ysc)
    counter += 0.01



ani = animation.FuncAnimation(fig, animate, frames=100, interval=10, repeat=False)
plt.show()