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
