import colorama

colorama.init()
COLORS = [
    # for numbers from 1 to 8
    colorama.Fore.BLUE,
    colorama.Fore.GREEN,
    colorama.Fore.RED,
    colorama.Fore.YELLOW,
    colorama.Fore.MAGENTA,
    colorama.Fore.LIGHTBLUE_EX,
    colorama.Fore.LIGHTMAGENTA_EX,
    colorama.Fore.LIGHTCYAN_EX,
]


def print_grid(grid: list, cursor_y: int, cursor_x: int):
    size = len(grid)
    line = ""
    print(("┏" + "━" * (size * 2 + 3) + "┓"))
    for y in range(size):
        line += "┃  "
        for x in range(size):
            if (y == cursor_y) and (x == cursor_x):
                line += f"{colorama.Style.BRIGHT}"
                line += f"{colorama.Back.LIGHTBLACK_EX}"
            # if False, this means that tile isn't opened yet.
            if grid[y][x][0] == False:
                # If tile is marked, highlight it with red.
                if grid[y][x][2] == True:
                    line += f"{colorama.Fore.RED}"
                line += "■"
            else:
                # If tile is a mine
                if grid[y][x][1] == -1:
                    line += "@"
                # If tail is empty
                elif grid[y][x][1] == 0:
                    line += "#"
                else:
                    # Get color based on the number of mines around the tile.
                    # TODO: REWRITE THAT ACCORDING TO THE DRY PRINCIPLE
                    if (y == cursor_y) and (x == cursor_x):
                        line += f"{colorama.Fore.BLACK}"
                    else:
                        line += f"{COLORS[grid[y][x][1]-1]}"
                    # Append amount of mines around.
                    line += f"{grid[y][x][1]}"
            line += f"{colorama.Style.RESET_ALL}"
            line += " "
        line += " ┃"
        print(line + "\n", end="")
        line = ""
    print(("┗" + "━" * (size * 2 + 3) + "┛"))
