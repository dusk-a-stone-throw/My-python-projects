import get_neighbors
import random


def add_mines(grid: list, mines_amount: int, ignore_y: int,
              ignore_x: int) -> list:
    size = len(grid)
    placed_mines = 0
    is_filled = False
    for y in range(size):
        for x in range(size):
            # FIRST CLICK MUSTN'T BE LETHAL.
            if (y == ignore_y) and (x == ignore_x):
                continue
            else:
                # negative value is a mine
                grid[y][x][1] = -1
                placed_mines += 1
                if placed_mines == mines_amount:
                    is_filled = True
                    break
        if is_filled:
            break
    return grid


# FIXME: FIX SHUFFLE TO PROVIDE SAFE FIRST CLICK WITHOUT MINES


# NOTE: I FIXED THAT WITH REALLY DUMB METHOD. JUST RANDOMLY GENERATE I AND J UNTIL THEY'RE NOT PROHIBITED
def shuffle(grid: list, ignore_y: int, ignore_x: int) -> list:
    size = len(grid)
    for y in range(size):
        for x in range(size):
            if (y == ignore_y) and (x == ignore_x):
                continue
            while (True):
                i = random.randint(y, size - 1)
                j = random.randint(x, size - 1)
                if (i != ignore_y and j != ignore_x):
                    break
            grid[y][x], grid[i][j] = grid[i][j].copy(), grid[y][x].copy()
    return grid


def fill_with_numbers(filled_grid: list) -> list:
    size = len(filled_grid)
    for j in range(size):
        for i in range(size):
            if filled_grid[j][i][1] < 0:
                continue
            else:
                neighbors = get_neighbors.get_neighbors(j, i, size)
                for k in neighbors:
                    y, x = k[0], k[1]
                    if filled_grid[y][x][1] < 0:
                        filled_grid[j][i][1] += 1
    return filled_grid
