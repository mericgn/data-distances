def minkowski(a, b, p):
    d_x = abs(b[0] - a[0])
    d_y = abs(b[1] - a[1])
    return (d_x ** p + d_y ** p) ** (1 / p)


def manhattan(a, b):
    return minkowski(a, b, 1)


def euclidean(a, b):
    return minkowski(a, b, 2)
