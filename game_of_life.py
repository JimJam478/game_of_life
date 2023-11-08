def get_grid(board):
    max_row, max_col = board["dimension"]
    grid = [[0] * max_col for _ in range(max_row)]
    return grid


def get_alive_cell(grid, board):
    alive_cells = board["alive"]
    for x, y in alive_cells:
        grid[x][y] = 1
    return grid


def display_grid(grid):
    row = len(grid)
    col = len(grid[0])
    display = ""
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                display += " * |"
            else:
                display += "   |"
        display += "\n"
    return display


def get_neighbour_count(grid):
    rows = len(grid)
    cols = len(grid[0])
    neighbours = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            neighbors_count = 0
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if x == 0 and y == 0:
                        continue
                    new_i, new_j = i + x, j + y
                    if 0 <= new_i < rows and 0 <= new_j < cols:
                        if grid[new_i][new_j] == 1:
                            neighbors_count += 1
            neighbours[i][j] = neighbors_count
    return neighbours


def get_next_Gen(grid, neighbours):
    row = len(grid)
    col = len(grid[0])
    for i in range(row):
        for j in range(col):
            if grid[i][j]:
                if neighbours[i][j] not in [2, 3]:
                    grid[i][j] = 0
            if not grid[i][j]:
                if neighbours[i][j] == 3:
                    grid[i][j] = 1
    return grid


def main():
    board = {}
    row = int(input("Enter dimension (row): "))
    col = int(input("Enter dimension (col): "))
    board["dimension"] = (row, col)
    grid = get_grid(board)
    print(display_grid(grid))
    board["alive"] = []
    while True:
        starter = input("Add an alive cell ? (y/n): ")
        if starter in ["Y", "y"]:
            alive_row = input("Enter alive cell row: ")
            alive_col = input("Enter alive cells col: ")
            board["alive"].append((int(alive_row), int(alive_col)))
            alive_grid = get_alive_cell(grid, board)
            print(display_grid(alive_grid))
        else:
            break

    print("---------------------------------------------")
    while True:
        cont = input(
            """Generate the next generation: 
Yes (c)
No (s)
> """
        )
        if cont in ["c", "C"]:
            neighbours = get_neighbour_count(alive_grid)
            next_gen = get_next_Gen(alive_grid, neighbours)
            print(display_grid(next_gen))
        if cont in ["s", "S"]:
            break
    print("Game stopped !!")


if __name__ == "__main__":
    main()
