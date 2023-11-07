import game_of_life 

def test_grid():
    board = {"dimension":(5,5),"alive":[]}
    grid = game_of_life.get_grid(board)
    assert grid == [['-','-','-','-','-',],['-','-','-','-','-',],['-','-','-','-','-',],['-','-','-','-','-',],['-','-','-','-','-',]]

