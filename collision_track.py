import numpy as np


def get_intersect(a1, a2, b1, b2):
    s = np.vstack([a1, a2, b1, b2])
    h = np.hstack((s, np.ones((4, 1))))
    l1 = np.cross(h[0], h[1])
    l2 = np.cross(h[2], h[3])
    x, y, z = np.cross(l1, l2)
    if z == 0:
        return (float('inf'), float('inf'))
    return (x/z, y/z)


def get_distance(point1, point2):
    a = np.array(point1)
    b = np.array(point2)
    dist = np.linalg.norm(a - b)

    return dist


print(get_intersect((0, 1), (1, 5), (2, 4), (3, 5)))
