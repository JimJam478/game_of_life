def get_grid(board):
    max_row,max_col = board['dimension']
    grid = [[0]*max_col for _ in range(max_row)]
    return grid

def get_alive_cell(grid,board):
    alive_cells = board["alive"]
    for x, y in alive_cells:
        grid[x][y] = 1

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
    neighbours = []
    for i in range(0, k):
        neighbours.append(neighbour_count_list[i::k])
    return neighbours

def get_next_Gen(grid,neighbours):
    row = len(grid)
    col = len(grid[0])
    for i in range(row):
        for j in range(col):
            if grid[i][j]:
                if neighbours[i][j] not in range(2,4):
                    grid[i][j] = 0
            if not grid[i][j]:
                if neighbours[i][j] == 3:
                    grid[i][j] = 1
    return grid 

# def main():
#     board = {}
#     row = int(input('Enter dimension (row): '))
#     col = int(input('Enter dimension (col): '))
#     board["dimension"] = (row,col)
#     grid = get_grid(board)
    
#     print(display_grid(grid))
#     board["alive"] = []
#     while True:
#         starter = input('Add an alive cell ? (y/n): ')
#         if starter in ['Y','y']:
#             alive_row = int(input('Enter alive cell row: '))
#             alive_col = int(input('Enter alive cells col: '))
#             board["alive"].append((alive_row,alive_col))
#             print(board)
#             alive_grid = get_alive_cell(grid,board)
#         else:
#             break
    
#     display_grid(alive_grid)
        
# main()


    
        




