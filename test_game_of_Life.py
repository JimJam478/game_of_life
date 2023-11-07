import game_of_life 

def test_grid():
    board = {"dimension":(5,5),"alive":[]}
    grid = game_of_life.get_grid(board)
    assert grid == [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]

def test_make_alive():
    grid = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    board = {"dimension":(5,5),"alive":(2,0)}
    alive_cell = game_of_life.get_alive_cell(grid,board)
    assert alive_cell == [[0,0,0],
                          [0,0,0],
                          [1,0,0]]

def test_display():
    grid = [[0,0,0],
            [0,0,0],
            [0,1,0]]
    
    display = game_of_life.display_grid(grid)
    assert display == """- - - 
- - - 
- * - 
"""