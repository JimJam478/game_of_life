def get_grid(board):
    max_row,max_col = board['dimension']
    grid = [['-']*max_col for _ in range(max_row)]
    return grid

def get_alive_cell(grid,board):
    grid = get_grid(board)
    alive_row,alive_col = board['alive']
    grid[alive_row][alive_col] = '*'
    return grid