import numpy as np

points = np.array([np.array([4, 6]), np.array([6, 8]), np.array([5, 5]), np.array([4, 8]),
                  np.array([4, 5]), np.array([4, 4]), np.array([6, 6]), np.array([5, 7]), np.array([3, 5])])

vectors = np.array([np.array([-1, 0]), np.array([1, 1]), np.array([0, 1]), np.array([-1, 1]),
                   np.array([0, -1]), np.array([0, -1]), np.array([1, -1]), np.array([1, -1]), np.array([-1, -1])])

# points = np.array([
#    np.array([random.randint(0, 10), random.randint(0, 10)]), np.array([random.randint(0, 10), random.randint(0, 10)]),
#    np.array([random.randint(0, 10), random.randint(0, 10)]), np.array([random.randint(0, 10), random.randint(0, 10)]),
#    np.array([random.randint(0, 10), random.randint(0, 10)]), np.array([random.randint(0, 10), random.randint(0, 10)]),
#    np.array([random.randint(0, 10), random.randint(0, 10)]), np.array([random.randint(0, 10), random.randint(0, 10)]),
#    np.array([random.randint(0, 10), random.randint(0, 10)]), np.array([random.randint(0, 10), random.randint(0, 10)]),
#    np.array([random.randint(0, 10), random.randint(0, 10)]), np.array([random.randint(0, 10), random.randint(0, 10)]),
#    np.array([random.randint(0, 10), random.randint(0, 10)]), np.array([random.randint(0, 10), random.randint(0, 10)]),
#    np.array([random.randint(0, 10), random.randint(0, 10)]), np.array([random.randint(0, 10), random.randint(0, 10)]),
#     np.array([random.randint(0, 10), random.randint(0, 10)]), np.array([random.randint(0, 10), random.randint(0, 10)])
# ])
#
# vectors = np.array([
#    np.array([random.randint(-2, 3), random.randint(-2, 3)]), np.array([random.randint(-2, 3), random.randint(-2, 3)]),
#    np.array([random.randint(-2, 3), random.randint(-2, 3)]), np.array([random.randint(-2, 3), random.randint(-2, 3)]),
#    np.array([random.randint(-2, 3), random.randint(-2, 3)]), np.array([random.randint(-2, 3), random.randint(-2, 3)]),
#    np.array([random.randint(-2, 3), random.randint(-2, 3)]), np.array([random.randint(-2, 3), random.randint(-2, 3)]),
#    np.array([random.randint(-2, 3), random.randint(-2, 3)]), np.array([random.randint(-2, 3), random.randint(-2, 3)]),
#    np.array([random.randint(-2, 3), random.randint(-2, 3)]), np.array([random.randint(-2, 3), random.randint(-2, 3)]),
#    np.array([random.randint(-2, 3), random.randint(-2, 3)]), np.array([random.randint(-2, 3), random.randint(-2, 3)]),
#    np.array([random.randint(-2, 3), random.randint(-2, 3)]), np.array([random.randint(-2, 3), random.randint(-2, 3)]),
#    np.array([random.randint(-2, 3), random.randint(-2, 3)]), np.array([random.randint(-2, 3), random.randint(-2, 3)])
# ])