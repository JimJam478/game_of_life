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
                display += "* "
            else:
                display += "- "
        display += "\n"
    return display
