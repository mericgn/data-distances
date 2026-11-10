import math


def manhattan(a, b):
    d_x = abs(b[0] - a[0])
    d_y = abs(b[1] - a[1])

    distance = d_x + d_y
    return distance


def euclidean(a, b):
    d_x = b[0] - a[0]
    d_y = b[1] - a[1]
    return math.sqrt(d_x ** 2 + d_y ** 2)
