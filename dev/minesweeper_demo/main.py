import keyboard
import time
import colorama
import print_grid
import generate_grid
import open_tiles


# If you opened all tiles that are not mines, you won!
def is_win(grid: list) -> bool:
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j][1] == -1:
                continue
            else:
                if grid[i][j][0] == False:
                    return False
    return True


# Need to actualize number of markers used.
# Perhaps I could do it in open_tiles() but it seems to me it's harder to do.
# The func below is simple as fk, but it's even not slow in big games (25*25).
def get_used_markers_amount(grid: list) -> int:
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j][2] == True:
                count += 1
    return count

def clear_screen():
    # awful but works
    print("\n"*100)
size, mines_amount = 0, 0
print(f"""
      Welcome to the minesweeper game!
      Open tiles until you open a bomb (in this case you lose!)
      If you open all tiles that are not bombs, you win.
      Number on the tile is the amount of bombs surrounding that tile.
      Press "{colorama.Fore.RED}m{colorama.Style.RESET_ALL}" to {colorama.Fore.RED}mark{colorama.Style.RESET_ALL} the tile to avoid its accidental opening.
      Good luck!
      {colorama.Style.DIM}Game created by Dusk a stone's throw.{colorama.Style.RESET_ALL}
      """)
while True:
    while True:
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("""Please enter the level of difficulty you want:
                1. Beginner
                2. Intermediate
                3. Advanced
                4. Expert
                5. Custom level""")
        difficulty_level = input(">>> ")
        match difficulty_level:
            case "1":
                size = 9
                mines_amount = 7
                break
            case "2":
                size = 14
                mines_amount = 17
                break
            case "3":
                size = 18
                mines_amount = 43
                break
            case "4":
                size = 25
                mines_amount = 110
                break
            case "5":
                size = int(input("Enter the grid size (X*X): "))
                mines_amount = int(input("Enter the amount of mines: "))
                break
            case _:
                print("Incorrect input!")
    clear_screen()
    # INIT
    grid = [[] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            grid[i].append([False, 0, False])
    # Start at the center of the grid.
    CURSOR_X = size // 2
    CURSOR_Y = size // 2
    first_click = True
    is_lost = False
    # START THE GAME
    while True:
        mines_marked = get_used_markers_amount(grid)
        print("Flags used:", mines_marked, "/", mines_amount)
        print_grid.print_grid(grid, CURSOR_Y, CURSOR_X)
        if is_lost:
            print(f"{colorama.Fore.RED}YOU LOST!{colorama.Style.RESET_ALL}")
            break
        if is_win(grid):
            print(f"{colorama.Fore.GREEN}YOU WON!{colorama.Style.RESET_ALL}")
            break
        key_pressed = keyboard.read_key(suppress=True)
        time.sleep(0.2)
        match key_pressed:
            case "left":
                if (CURSOR_X - 1) >= 0:
                    CURSOR_X -= 1
            case "right":
                if (CURSOR_X + 1) <= (size - 1):
                    CURSOR_X += 1
            case "down":
                if (CURSOR_Y + 1) <= (size - 1):
                    CURSOR_Y += 1
            case "up":
                if (CURSOR_Y - 1) >= 0:
                    CURSOR_Y -= 1
            case "enter":
                if first_click:
                    grid = generate_grid.add_mines(grid, mines_amount, CURSOR_Y,
                                                   CURSOR_X)
                    grid = generate_grid.shuffle(grid, CURSOR_Y, CURSOR_X)
                    grid = generate_grid.fill_with_numbers(grid)
                    first_click = False
                # If tile is not marked
                if grid[CURSOR_Y][CURSOR_X][2] == False:
                    grid, is_lost = open_tiles.open_tiles(grid, CURSOR_Y, CURSOR_X)
            case "m":
                # If selected tile is not marked, mark it.
                if (grid[CURSOR_Y][CURSOR_X][2]
                        == False) and (grid[CURSOR_Y][CURSOR_X][0] == False):
                    # ...if you got enough markers, obviously.
                    if mines_marked + 1 <= mines_amount:
                        grid[CURSOR_Y][CURSOR_X][2] = True
                # Else toggle it (set as unmarked).
                else:
                    grid[CURSOR_Y][CURSOR_X][2] = False
            case "esc":
                # a = input("Exit? (y/n): ").lower()
                # print(a)
                # input()
                # if a == "y":
                break
        clear_screen()
