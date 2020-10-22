import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Functions import point_and_a_straight_line

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
points = []
hull = []

def dynamic_hull(array) -> list:
    for i in range(0, len(array) - 1):
        if array[i][0] == array[-1][0] and array[i][1] == array[-1][1]:
            array.pop()
            return
    if len(array) == 1:
        hull.append(array[0])
    elif len(array) == 2:
        hull.append(array[1])
    elif len(array) == 3:
        if point_and_a_straight_line(array[0], array[1], array[2]) == 0:
            hull.clear()
            for i in range(0, 3):
                if np.dot(array[i - 1] - array[i], array[i - 2] - array[i]) >= 0:
                    hull.append(array[i])
        else:
            if point_and_a_straight_line(array[0], array[1], array[2]) == 1:
                hull.append(array[2])
            else:
                hull[1] = array[2]
                hull.append(array[1])
    else:
        hull.append(hull[0])

        right = []
        for i in range(0, len(hull) - 1):
            if point_and_a_straight_line(hull[i], hull[i+1], array[-1]) == 2:
                right.append([hull[i], hull[i+1]])
        if len(right) == 0:
            hull.pop()
            return
        else:
            if right[-1][0][0] == hull[-2][0] \
                    and right[-1][0][1] == hull[-2][1] \
                    and right[-1][1][0] == hull[-1][0] \
                    and right[-1][1][1] == hull[-1][1]:  # 4.3
                hull.insert(0, array[-1])
                hull.pop()
                hull.append(array[-1])
                while point_and_a_straight_line(hull[1], hull[2], hull[0]) == 2:
                    del hull[1]
                while point_and_a_straight_line(hull[-3], hull[-2], hull[-1]) == 2:
                    del hull[-2]
                hull.pop()
            else: #4.2
                iterLeft = 0
                iterRight = 0
                for i in range(0, len(hull) - 1):
                    if hull[i][0] == right[0][0][0] and hull[i][1] == right[0][0][1]:
                        iterLeft = i
                    if hull[i][0] == right[-1][1][0] and hull[i][1] == right[-1][1][1]:
                        iterRight = i
                for i in range(iterRight - iterLeft - 1):
                    del hull[iterLeft + 1]
                hull.insert(iterLeft + 1, array[-1])
                hull.pop()


def animate(i):
    x = random.randint(1, 40)
    y = random.randint(1, 40)
    point = np.array([x, y])
    points.append(point)
    points_x = [p[0] for p in points]
    points_y = [p[1] for p in points]

    dynamic_hull(points)
    hull_x = [p[0] for p in hull]
    hull_y = [p[1] for p in hull]
    hull_x.append(hull[0][0])
    hull_y.append(hull[0][1])

    ax.clear()
    ax.plot(hull_x, hull_y, marker='o', linestyle='-', color='red')
    ax.scatter(points_x, points_y, marker='o', linestyle='-', color='blue')


ani = animation.FuncAnimation(fig, animate, interval=500, repeat=False)
plt.show()
