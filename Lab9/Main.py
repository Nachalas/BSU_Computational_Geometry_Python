import matplotlib.pyplot as plt
import numpy as np
import random

from numpy.linalg import norm
import matplotlib.animation as animation

fig, ax = plt.subplots()

# points = [
#    np.array([random.randint(0, 10), random.randint(0, 10)]), np.array([random.randint(0, 10), random.randint(0, 10)]),
#    np.array([random.randint(0, 10), random.randint(0, 10)]), np.array([random.randint(0, 10), random.randint(0, 10)]),
#    np.array([random.randint(0, 10), random.randint(0, 10)]), np.array([random.randint(0, 10), random.randint(0, 10)]),
#    np.array([random.randint(0, 10), random.randint(0, 10)]), np.array([random.randint(0, 10), random.randint(0, 10)]),
#    np.array([random.randint(0, 10), random.randint(0, 10)]), np.array([random.randint(0, 10), random.randint(0, 10)]),
#    np.array([random.randint(0, 10), random.randint(0, 10)]), np.array([random.randint(0, 10), random.randint(0, 10)]),
#    np.array([random.randint(0, 10), random.randint(0, 10)]), np.array([random.randint(0, 10), random.randint(0, 10)]),
#    np.array([random.randint(0, 10), random.randint(0, 10)]), np.array([random.randint(0, 10), random.randint(0, 10)]),
#     np.array([random.randint(0, 10), random.randint(0, 10)])
# ]

points = []
vectors = []
for i in range(20):
    x = random.randint(1, 50)
    y = random.randint(1, 50)
    point = np.array([x, y])
    points.append(point)
    for i in range(0, len(points) - 1):
        if points[i][0] == points[-1][0] and points[i][1] == points[-1][1]:
            points.pop()

for j in range(0, len(points)):
    x = random.randint(-2, 2)
    y = random.randint(-2, 2)
    vector = np.array([x, y])
    vectors.append(vector)
# points.append(np.array([9, 5]))
# points.append(np.array([9, 5.25]))

# points = [
#    np.array([random.randint(0, 10), random.randint(0, 10)]), np.array([random.randint(0, 10), random.randint(0, 10)]),
#    np.array([random.randint(0, 10), random.randint(0, 10)]), np.array([random.randint(0, 10), random.randint(0, 10)]),
#    np.array([random.randint(0, 10), random.randint(0, 10)])
# ]

# points = np.array([
#    np.array([0,3]), np.array([1,0]),
#    np.array([6,7]), np.array([10,4]), np.array([0,3])
# ])

# points = np.array([
#    np.array([0,5]), np.array([0,6]),
#    np.array([0,9]), np.array([2,4]),
#     np.array([3,6]), np.array([4,0]),
#     np.array([7,7]), np.array([8,1])
# ])

# Находим перебором минимальное расстояние во множестве из 2/3 точек
def find_nearest_bruteforce(x):
    quantity = len(x)
    if quantity == 2:
        return [x[0], x[1]]
    # three points case:
    x.append(x[0])
    min = norm([x[0][0] - x[1][0], x[0][1] - x[1][1]])
    left = 0
    right = 1
    for i in range(1, quantity):
        temp = norm([x[i][0] - x[i+1][0], x[i][1] - x[i+1][1]])
        if temp < min:
            min = temp
            left = i
            right = i + 1
    return [x[left], x[right]]


# Это пока не нужно
# def find_index(x,to_find):
#     index = -1
#     for i in range(0, len(x)):
#         index += 1
#         if x[i][0] == to_find[0] and x[i][1] == to_find[1]:
#             return index

def find_two_nearest_points(x, y):
    if len(x) <= 3:
        return find_nearest_bruteforce(x)
    quantity = len(x)
    sep = quantity // 2
    x_l = x[0:sep]
    x_r = x[sep:quantity]
    y_l = []
    y_r = []
    for i in y:
        if i[0] <= x[sep][0]:
            y_l.append(i)
        # elif i[0] == x[sep][0]:
        #     if find_index(x, i) < sep:
        #         y_l.append(i)
        #     else:
        #         y_r.append(i)
        else:
            y_r.append(i)
    delta_l_array = find_two_nearest_points(x_l, y_l)
    delta_r_array = find_two_nearest_points(x_r, y_r)
    delta_l_1 = delta_l_array[0]
    delta_l_2 = delta_l_array[1]
    delta_r_1 = delta_r_array[0]
    delta_r_2 = delta_r_array[1]
    if norm([delta_l_1[0] - delta_l_2[0], delta_l_1[1] - delta_l_2[1]]) < \
            norm([delta_r_1[0] - delta_r_2[0], delta_r_1[1] - delta_r_2[1]]):
        delta = delta_l_array
    else:
        delta = delta_r_array
    delta_norm = norm([delta[0][0] - delta[1][0], delta[0][1] - delta[1][1]])
    y_delta = []
    for i in y:
        if abs(i[0] - x[sep][0]) <= delta_norm:
            y_delta.append(i)
    for i in range(len(y_delta) - 1):
        for j in range(i + 1, min(i + 7, len(y_delta))):
            point_first = y_delta[i]
            point_second = y_delta[j]
            dist = norm([point_first[0] - point_second[0], point_first[1] - point_second[1]])
            if dist < delta_norm:
                delta[0] = point_first
                delta[1] = point_second
                delta_norm = dist
    return delta

    # final_delta = min(delta_l, delta_r)

def sort_by_x(obj):
    return obj[0]

def sort_by_y(obj):
    return obj[1]


d_const = 2


def animate(i):

    X = sorted(points, key=sort_by_x)
    Y = sorted(points, key=sort_by_y)
    # print(X)
    # print(Y)
    final = find_two_nearest_points(X, Y)
    print(final)

    ax.clear()
    points_x = [p[0] for p in points]
    points_y = [p[1] for p in points]
    plt.xlim(-10, 60)
    plt.ylim(-10, 60)
    l1 = ax.scatter(points_x, points_y, marker='o', linestyle='-', color='blue')
    ax.plot([final[0][0], final[1][0]], [final[0][1], final[1][1]], marker='o', linestyle='-', color='red')

    d_curr = norm([final[1][0] - final[0][0], final[1][1] - final[0][1]])

    if d_curr > d_const:
        for i in range(0, len(points)):
            x = random.randint(-2, 2)
            y = random.randint(-2, 2)
            vector = np.array([x, y])
            vectors[i] = vector
            l2 = ax.arrow(points[i][0], points[i][1], vectors[i][0], vectors[i][1], width=0.05)
    for i in range(0, len(points)):
        points[i] += vectors[i]


ani = animation.FuncAnimation(fig, animate, interval=100, repeat=False)
plt.show()
