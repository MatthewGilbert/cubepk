from coord import _coords


def get_coord(points, offset=1, scale=0.5):
    """
    Returns list of coordinates which maximizes the minimum L2 distance
    between points

    Parameters
    ----------
    points: int, {1, 2, ..., 72}
        The number of points to fit in the cube.
    offset: float
        Value to offset the coordinates by
    scale: flaot
        Value to scale the size of the cube by

    """

    coord = [map(lambda val:(val+offset)*scale, x) for x in _coords[points-1]]
    return coord
