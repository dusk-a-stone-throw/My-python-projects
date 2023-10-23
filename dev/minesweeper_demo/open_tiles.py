import get_neighbors


def open_tiles(grid: list, y: int, x) -> tuple[list, bool]:
    neighbors = get_neighbors.get_neighbors(y, x, len(grid))

    # If tile is already opened, ignore
    if grid[y][x][0] == True:
        return grid, False

    # If you opened a mine, you lose and need to open all other tiles (like in original minesweeper).
    if grid[y][x][1] == -1:
        for i in range(len(grid)):
            for j in range(len(grid)):
                grid[i][j][0] = True
        return grid, True

    # Else if it's just a tile with amount of mines, open it.
    elif grid[y][x][1] > 0:
        # NOTE: (IF IT'S NOT MARKED)
        if grid[y][x][2] == False:
            grid[y][x][0] = True

    # ELSE it's an empty tile, open it and all its neighbors.
    # NOTE: Even if it's marked
    else:
        grid[y][x][0] = True
        # NOTE: Also unmark it.
        grid[y][x][2] = False
        for y, x in neighbors:
            open_tiles(grid, y, x)
    return grid, False
