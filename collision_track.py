<<<<<<< HEAD
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
=======
def point_in_rectangle(point, rectangle):
    """
        Determine if the given point is inside the rectangle
        Args:
            point(tuple): tuple of points x and y
            rectangle
        Returns:
            bool: True if point in the rect, False otherwise
    """

    left_sides = 0
    for i in range(0, 4):

        corner_1 = rectangle[i % 4]
        corner_2 = rectangle[(i+1) % 4]

        dot = (corner_2[0] - corner_1[0]) * (point[1] - corner_1[1]) - \
            (point[0] - corner_1[0]) * (corner_2[1] - corner_1[1])
        # print("point",point,"rect",rectangle,"dot",dot)
        if dot < 0:
            left_sides += 1
        else:
            return False

    if left_sides == 4:
        return True
    else:
        return False


def rectangle_collison(rect1, rect2):

    for point in rect1:

        result = point_in_rectangle(point, rect2)
        # print("point:",point,"rect",rect2,"result",result)
        if result:
            return True

    for point in rect2:

        result = point_in_rectangle(point, rect1)
        # print("point:",point,"rect",rect1,"result",result)
        if result:
            return True

    return False
>>>>>>> 17f24328ade001d49b84c0dd4e746d0e7fe6e180
