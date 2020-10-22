import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

from Functions import draw_graph, angle_test, point_position_convex_polygon, segments_intersection_without_output

fig, ax = plt.subplots()

def reflection_vector(a: np.array, b: np.array):
    return 2 * (np.dot(a, b) / np.dot(b, b)) * b - a


points = np.array([np.array([6, 9]), np.array([6, 5.5]), np.array([12, 7]), np.array([8, 9]), np.array([10, 10.2]), np.array([9, 11])])
vectors = np.array([np.array([-0.37, 0.9]), np.array([1, 0]), np.array([-1, 0]), np.array([0, -1]), np.array([-0.9, 0.5]), np.array([0.78, 0.37])])
#points = np.array([np.array([6, 9]), np.array([6, 5.5]), np.array([12, 7]), np.array([8, 9])])
#vectors = np.array([np.array([-0.37, 0.9]), np.array([1, 0]), np.array([-1, 0]), np.array([0, -1])])

simple_polygon_points = np.array([np.array([9.5, 7]), np.array([10, 8]), np.array([9.5, 9]),
                             np.array([10, 10]), np.array([11, 4]), np.array([6.5, 8]),
                             np.array([1 + 8.5, 2 + 5])])
convex_polygon_points = np.array([np.array([3, 9]), np.array([6, 3]), np.array([12, 3]), np.array([15, 9]),
                             np.array([12, 12]),
                             np.array([6, 12]), np.array([3, 9])])

sp_x = [p[0] for p in simple_polygon_points]
sp_y = [p[1] for p in simple_polygon_points]

cp_x = [p[0] for p in convex_polygon_points]
cp_y = [p[1] for p in convex_polygon_points]

def animate(i):
    ax.clear()

    points_x = [p[0] for p in points]
    points_y = [p[1] for p in points]

    #draw_graph(convex_polygon_points, simple_polygon_points, points)
    while angle_test(points[i], simple_polygon_points) != 1:
        ax.plot(sp_x, sp_y)
        ax.plot(cp_x, cp_y)
        ax.scatter(points_x, points_y, marker='o', linestyle='-', color='red')
        if point_position_convex_polygon(points[i] + vectors[i],
                                         convex_polygon_points) == 0 or point_position_convex_polygon(
                points[i] + vectors[i], convex_polygon_points) == -1:
            for i in range(len(convex_polygon_points) - 1):
                if segments_intersection_without_output(convex_polygon_points[i], convex_polygon_points[i + 1],
                                                        points[i], points[i] + vectors[i]):
                    vectors[i] = reflection_vector(vectors[i],
                                                       convex_polygon_points[i] - convex_polygon_points[i + 1])
        if angle_test(points[i], simple_polygon_points) == 1:
            vectors[i] = np.array([0, 0])
        points[i] = (vectors[i] + points[i])
            # draw_graph(convex_polygon_points, simple_polygon_points, points)
        # draw_graph(convex_polygon_points, simple_polygon_points, points)
    #draw_graph(convex_polygon_points, simple_polygon_points, points)



ani = animation.FuncAnimation(fig, animate, frames=range(1, len(points)), interval=100, repeat=False)
plt.show()
