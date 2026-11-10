def manhattan(a, b):
    d_x = abs(b[0] - a[0])
    d_y = abs(b[1] - a[1])

    distance = d_x + d_y
    return distance
