def get_grid(board):
    max_row,max_col = board['dimension']
    grid = [[0]*max_col for _ in range(max_row)]
    return grid

def get_alive_cell(grid,board):
    alive_row,alive_col = board['alive']
    grid[alive_row][alive_col] = 1
    return grid

def display_grid(grid):
    row = len(grid)
    col =  len(grid[0])
    display = ""
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                display += " * |"
            else:
                display += " - |"
        display += "\n"
    return display

def get_neighbour_count(grid):
    neighbour_count_list = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbour_count = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and (x, y) != (i, j):
                        neighbour_count += grid[x][y]
            neighbour_count_list.append(neighbour_count)
    k = len(grid)
    res = []
    for i in range(0, k):
        res.append(neighbour_count_list[i::k])
    return res

    
        




