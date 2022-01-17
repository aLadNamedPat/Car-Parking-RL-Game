import numpy as np
import math


def onSegment(p, q, r):
    px, py = p
    qx, qy = q
    rx, ry = r
    if ((qx <= max(px, rx)) and (qx >= min(px, rx)) and (qy <= max(py, ry)) and (qy >= min(py, ry))):
        return True
    return False


def orientation(p, q, r):
    # finds orientation of 3 points
    # 0 --> Collinear
    # 1 --> Clockwise points
    # 2 --> Counterclockwise points
    # accepts inputs of (x1, y1), (x2, y2), (x3, y3)
    px, py = p
    qx, qy = q
    rx, ry = r

    val = (float(qy - py) * (rx - qx)) - (float(qx - px) * (ry - qy))
    if val > 0:
        # Clockwise orientation
        return 1

    elif (val < 0):
        # Counterclockwise orientation
        return 2

    else:
        # Collinear
        return 0


def doIntersect(segment1, segment2):
    p1, q1 = segment1
    p2, q2 = segment2

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    if (o1 != o2 and o3 != o4):
        return True

    if ((o1 == 0) and onSegment(p1, p2, q1)):
        return True

    # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
    if ((o2 == 0) and onSegment(p1, q2, q1)):
        return True

    # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
    if ((o3 == 0) and onSegment(p2, p1, q2)):
        return True

    # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
    if ((o4 == 0) and onSegment(p2, q1, q2)):
        return True

    # If none of the cases
    return False


def get_intersect(segment1, segment2):
    """
    Returns the point of intersection of the lines passing through a2,a1 and b2,b1.
    a1: [x, y] a point on the first line
    a2: [x, y] another point on the first line
    b1: [x, y] a point on the second line
    b2: [x, y] another point on the second line
    """
    a1, a2 = segment1
    b1, b2 = segment2
    s = np.vstack([a1, a2, b1, b2])        # s for stacked
    h = np.hstack((s, np.ones((4, 1))))  # h for homogeneous
    l1 = np.cross(h[0], h[1])           # get first line
    l2 = np.cross(h[2], h[3])           # get second line
    x, y, z = np.cross(l1, l2)          # point of intersection
    if z == 0:                          # lines are parallel
        return (10000, 10000)
    return (x/z, y/z)


def get_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.hypot(abs(x2 - x1), abs(y2 - y1))


def amplify(staticPoint, point2, distance=1000):
    x1, y1 = staticPoint
    x2, y2 = point2
    relativePointx = x2 - x1
    relativePointy = y2 - y1
    factor = distance / math.hypot(relativePointx, relativePointy)
    newPointx = (factor * relativePointx) + x1
    newPointy = (factor * relativePointy) + y1
    return (staticPoint, (newPointx, newPointy))


# print(doIntersect(
#     (
#         (0, 5), (5, 0)
#     ),
#     (
#         (0, 0), (5, 5)
#     )
# )
# )

# print(get_intersect(
#     (
#         amplify((0, 5), (5, 0))
#     ),
#     (
#         (0, 0), (5, 5)
#     )
# ))
