import matplotlib.pyplot as plt
import numpy as np
from Functions import draw_graph, angle_test, point_position_convex_polygon, segments_intersection_without_output


def reflection_vector(a, b):
    return 2 * (np.dot(a, b) / np.dot(b, b)) * b - a


if __name__ == '__main__':
    points = np.array([np.array([6, 9]), np.array([6, 5.5]), np.array([12, 7]), np.array([8, 9]), np.array([10, 10.2]), np.array([9, 11])])
    vectors = np.array([np.array([-0.37, 0.9]), np.array([1, 0]), np.array([-1, 0]), np.array([0, -1]), np.array([-0.9, 0.5]), np.array([0.78, 0.37])])
    #points = np.array([np.array([6, 9]), np.array([6, 5.5]), np.array([12, 7]), np.array([8, 9])])
    #vectors = np.array([np.array([-0.37, 0.9]), np.array([1, 0]), np.array([-1, 0]), np.array([0, -1])])

    simple_polygon_points = np.array([np.array([9.5, 7]), np.array([10, 8]), np.array([9.5, 9]),
                             np.array([12, 10]), np.array([9, 4]), np.array([6.5, 8]),
                             np.array([1 + 8.5, 2 + 5])])
    convex_polygon_points = np.array([np.array([3, 9]), np.array([6, 3]), np.array([12, 3]), np.array([15, 9]),
                             np.array([12, 12]),
                             np.array([6, 12]), np.array([3, 9])])
    counter = 0
    while counter != len(points):
        draw_graph(convex_polygon_points, simple_polygon_points, points)
        for index in range(0, len(points)):
            while angle_test(points[index], simple_polygon_points) != 1:
                if point_position_convex_polygon(points[index] + vectors[index], convex_polygon_points) == 0:
                    for i in range(len(convex_polygon_points) - 1):
                        if segments_intersection_without_output(convex_polygon_points[i], convex_polygon_points[i+1], points[index], points[index] + vectors[index]):
                            vectors[index] = reflection_vector(vectors[index], convex_polygon_points[i] - convex_polygon_points[i + 1])
                if angle_test(points[index], simple_polygon_points) == 1:
                    vectors[index] = np.array([0, 0])
                points[index] = (vectors[index] + points[index])
                #draw_graph(convex_polygon_points, simple_polygon_points, points)
            counter += 1
            draw_graph(convex_polygon_points, simple_polygon_points, points)
        #draw_graph(convex_polygon_points, simple_polygon_points, points)
