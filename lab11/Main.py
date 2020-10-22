from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm
import random
import math

# points = []
#
# for i in range(20):
#     x = random.randint(1, 50)
#     y = random.randint(1, 50)
#     point = np.array([x, y])
#     points.append(point)
#     for i in range(0, len(points) - 1):
#         if points[i][0] == points[-1][0] and points[i][1] == points[-1][1]:
#             points.pop()

# points = np.array([
#     np.array([8, 8]), np.array([2, 9]), np.array([3, 2]), np.array([1, 1]), np.array([5, 3]), np.array([6, 8]),
#     np.array([2, 6]), np.array([7, 5]), np.array([5, 5]), np.array([10, 10]), np.array([4, 8]),
#     np.array([4, 5]), np.array([4, 4]), np.array([3, 3]), np.array([6, 7]), np.array([5, 8]), np.array([3, 5]),
#     np.array([6, 10])
# ])
#
# final = []
# used_points = []
#
#
# def point_and_a_straight_line(p1, p2, p0):
#     v = np.cross(p2 - p1, p0 - p1)
#
#     if v > 0:
#         return 1  # левее
#     elif v < 0:
#         return 2  # правее
#     else:
#         return 0  # на прямой
#
#
# def jarvis_hull(array):
#     start_point = np.array(min(array, key=lambda p: p[1]))
#     convex_hull = [start_point]
#     while True:
#         if convex_hull[-1][0] == array[0][0] and convex_hull[-1][1] == array[0][1]:
#             right = 1
#         else:
#             right = 0
#         for i in range(0, len(array)):
#             if point_and_a_straight_line(convex_hull[-1], array[right], array[i]) == 2:
#                 right = i
#         if array[right][0] == convex_hull[0][0] and array[right][1] == convex_hull[0][1]:
#             break
#         else:
#             convex_hull.append(array[right])
#     convex_hull.append(convex_hull[0])
#     return convex_hull
#
#
# def check_point_equality(a, b):
#     return a[0] == b[0] and a[1] == b[1]
#
#
# def find_angle(base_1, base_2, point):
#     dp = np.dot(base_1 - point, base_2 - point)
#     normal = (norm(base_1 - point) * norm(base_2 - point))
#     if normal == 0 or abs(normal) < 0.00001:
#         return 0
#     cos = dp / normal
#     if abs(math.acos(cos)) < 0.1:
#         return 0
#     print(math.acos(cos) * 180 / math.pi)
#     return math.acos(cos) * 180 / math.pi
#
#
# def is_in_array(segment, array):
#     for i in array:
#         if check_point_equality(segment[0], i[0]) and check_point_equality(segment[1], i[1]):
#             return True
#     return False
#
#
# def triangulation_helper(points, start_line_1, start_line_2):
#     max = 0
#     point = None
#     for i in points:
#         if check_point_equality(i, start_line_1) != True and check_point_equality(i, start_line_2) != True:
#             if find_angle(start_line_1, start_line_2, i) > max and point_and_a_straight_line(start_line_1, start_line_2, i) == 1:
#                 max = find_angle(start_line_1, start_line_2, i)
#                 point = i
#     if point is not None:
#         if is_in_array([start_line_1, point], final) and is_in_array([start_line_2, point], final):
#             return
#         final.append([start_line_1, point])
#         final.append([start_line_2, point])
#         triangulation_helper(points, point, start_line_2)
#         triangulation_helper(points, start_line_1, point)
#
#
# def triangulation(points, start_line_1, start_line_2):
#     max = 0
#     point = points[0]
#     for i in points:
#         if check_point_equality(i, start_line_1) != True and check_point_equality(i, start_line_2) != True:
#             if find_angle(start_line_1, start_line_2, i) > max:
#                 max = find_angle(start_line_1, start_line_2, i)
#                 point = i
#     final.append([start_line_1, point])
#     final.append([start_line_2, point])
#     # if len(final) > 1000:
#     #     return
#     triangulation_helper(points, start_line_1, point)
#     triangulation_helper(points, point, start_line_2)
#
#
# # tri = Delaunay(points)
# # points_x = [p[0] for p in points]
# # points_y = [p[1] for p in points]
# # plt.plot(points_x, points_y, 'o')
# # hull = jarvis_hull(points)
# # triangulation(points, hull[0], hull[1])
# # hull_x = [p[0] for p in hull]
# # hull_y = [p[1] for p in hull]
# # plt.plot(hull_x, hull_y)
# # triang_x = []
# # triang_y = []
# # print(final)
# # for i in final:
# #     triang_x.append(i[0][0])
# #     triang_x.append(i[1][0])
# #     triang_y.append(i[0][1])
# #     triang_y.append(i[1][1])
# # print(triang_x)
# # print(triang_y)
# # plt.plot(triang_x, triang_y)
# # print(find_angle(points[0], points[1], points[2]))
# # for i in tri.simplices:
# #    plt.plot([points[i[0]][0], points[i[1]][0]], [points[i[0]][1], points[i[1]][1]])
# #    plt.plot([points[i[1]][0], points[i[2]][0]], [points[i[1]][1], points[i[2]][1]])
# #    plt.plot([points[i[0]][0], points[i[2]][0]], [points[i[0]][1], points[i[2]][1]])
points = open("F:\siplasplus\DelaunayFinal2\DelaunayFinal2\ouput.txt", 'r').read()
lines = points.split('\n')
segments_x = lines[0]
segments_y = lines[1]
points_x = lines[2]
points_y = lines[3]
points_x = [float(p) for p in points_x.split(',')]
points_y = [float(p) for p in points_y.split(',')]
segments_x = [float(p) for p in segments_x.split(',')]
segments_y = [float(p) for p in segments_y.split(',')]
# print(segments_x)
# print(segments_y)

i = 0
plt.scatter(points_x, points_y)
while i < len(segments_x) - 1:
    plt.plot([segments_x[i], segments_x[i+1]], [segments_y[i], segments_y[i+1]])
    i += 2
plt.show()