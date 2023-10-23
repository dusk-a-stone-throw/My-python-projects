def get_neighbors(y: int, x: int, grid_size: int) -> list:
    """
    Returns the array of neighbors of a tile (but not the tile itself).
    In such format:
    [[y1,y1],[y2,x2],...,[yn,xn]]
    Note that yOx system starts from left top corner of a matrix.
    For example, for the matrix
    [
            [a,b,c,d],
            [e,f,g,h],
            [i,j,k,l]
     ]
    "a" has coordinates [0,0].
    "g" has coordinates [1,2].

    Examples:
    >>> get_neighbors(1,2,10)
    [[0, 1], [1, 1], [2, 1], [0, 2], [2, 2], [0, 3], [1, 3], [2, 3]]
    >>> get_neighbors(9,9,10)
    [[8, 8], [9, 8], [8, 9]]
    """
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if ((x + i) < 0) or ((x + i) >= grid_size) or ((y + j) < 0) or (
                (y + j) >= grid_size) or (i == 0 and j == 0):
                continue
            else:
                neighbors.append([y + j, x + i])
    return neighbors
