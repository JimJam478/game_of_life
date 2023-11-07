def get_grid(board):
    max_row,max_col = board['dimension']
    grid = [['-']*max_col for _ in range(max_row)]
    return grid

