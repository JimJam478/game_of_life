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

import random
def main():
    key = input("""AUTO or MANUAL:
Auto (a)
Manual (m)
""")
    if key == 'm':
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
New Alive Cell (a)
> """
            )
            if cont in ["c", "C"]:
                neighbours = get_neighbour_count(alive_grid)
                next_gen = get_next_Gen(alive_grid, neighbours)
                print(display_grid(next_gen))
            
            if cont in ['a','A']:
                alive_row = input("Enter alive cell row: ")
                alive_col = input("Enter alive cells col: ")
                new_board = {}
                new_board["alive"] = []
                new_board["alive"].append((int(alive_row),int(alive_col)))
                new_grid = get_alive_cell(next_gen, new_board)
                print(display_grid(new_grid))
                alive_grid = new_grid

            if cont in ["s", "S"]:
                break
        print("Game stopped !!")
    if key == 'a':
        board = {}
        row = random.randint(2,15)
        col = row
        board["dimension"] = row,col
        grid = get_grid(board)
        print(display_grid(grid))
        board["alive"] = []
        alive_cell_count = random.randint(0,row)
        for i in range(alive_cell_count):
            alive_row = random.randint(0,row)
            alive_col = random.randint(0,col)
            board["alive"].append((alive_row,alive_col))
            alive_grid = get_alive_cell(grid, board)
        print(display_grid(alive_grid))
        
        while True:
            cont = input(
                """Generate the next generation: 
Enter < n >  to get next gen
Enter < S > to stop 
> """)
            if cont == 'n':
                neighbours = get_neighbour_count(alive_grid)
                next_gen = get_next_Gen(alive_grid, neighbours)
                print(display_grid(next_gen))
            if cont in ['s','S']:
                break

    print("Game Stopped !!")

if __name__ == "__main__":
    main()
