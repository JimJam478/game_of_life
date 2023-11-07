import game_of_life 

def test_grid():
    board = {"dimension":(5,5),"alive":[]}
    grid = game_of_life.get_grid(board)
    assert grid == [['-','-','-','-','-',],['-','-','-','-','-',],['-','-','-','-','-',],['-','-','-','-','-',],['-','-','-','-','-',]]

def test_make_alive():
    grid = [['-','-','-','-','-',],
            ['-','-','-','-','-',],
            ['-','-','-','-','-',],
            ['-','-','-','-','-',],
            ['-','-','-','-','-',]]
    board = {"dimension":(5,5),"alive":(3,3)}
    alive_cell = game_of_life.get_alive_cell(grid,board)
    assert alive_cell == [['-','-','-','-','-',],
            ['-','-','-','-','-',],
            ['-','-','-','-','-',],
            ['-','-','-','*','-',],
            ['-','-','-','-','-',]]

def test_display():
    grid = [['-','-','-','-','-',],
            ['-','-','-','-','-',],
            ['-','-','-','-','-',],
            ['-','-','-','-','-',],
            ['-','-','-','-','-',]]
    board = {"dimension":(5,5),"alive":(3,3)}
    display = game_of_life.get_alive_cell(grid,board)
    assert display == """-----
    -----
    -----
    ---*-
    -----"""