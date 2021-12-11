import helpers as helper

def check_flash(grid, x_pos, y_pos):
    if (grid[y_pos][x_pos][1] == False and grid[y_pos][x_pos][0] > 9):
        global global_count
        global_count += 1
        grid = flash_area(grid, x_pos, y_pos)    
    return grid
        
def flash_area(grid, x_pos, y_pos):
    grid[y_pos][x_pos] = ((grid[y_pos][x_pos][0] + 1), True)

    size = len(grid) -1
    y_minus = True
    y_plus = True
    x_minus = True
    x_plus = True

    if  x_pos - 1 < 0:
        x_minus = False
    elif x_pos + 1 > size:
        x_plus = False
    if y_pos - 1 < 0:
        y_minus = False
    elif y_pos + 1 > size:
        y_plus = False

    # check row y - 1
    if y_minus and x_minus:
        grid[y_pos -1][x_pos -1]  = (grid[y_pos -1][x_pos -1][0] + 1, grid[y_pos -1][x_pos -1][1])
        grid = check_flash(grid, x_pos-1, y_pos-1)
    if y_minus:
        grid[y_pos -1][x_pos] = (grid[y_pos -1][x_pos][0] + 1, grid[y_pos -1][x_pos][1])
        grid = check_flash(grid, x_pos, y_pos-1)
    if y_minus and x_plus:
        grid[y_pos -1][x_pos +1] = (grid[y_pos -1][x_pos +1][0] + 1, grid[y_pos -1][x_pos +1][1])
        grid = check_flash(grid, x_pos+1, y_pos-1)

    # check row y
    if x_minus:
        grid[y_pos][x_pos -1] = (grid[y_pos][x_pos -1][0] + 1, grid[y_pos][x_pos -1][1])
        grid = check_flash(grid, x_pos-1, y_pos)
    if x_plus:
        grid[y_pos][x_pos +1] = (grid[y_pos][x_pos +1][0] + 1, grid[y_pos][x_pos +1][1])
        grid = check_flash(grid, x_pos+1, y_pos)

    # check row y + 1
    if y_plus and x_minus:
        grid[y_pos +1][x_pos -1] = (grid[y_pos +1][x_pos -1][0] + 1, grid[y_pos +1][x_pos -1][1])
        grid = check_flash(grid, x_pos -1, y_pos+1)
    if y_plus:
        grid[y_pos +1][x_pos] = (grid[y_pos +1][x_pos][0] + 1, grid[y_pos +1][x_pos][1])
        grid = check_flash(grid, x_pos, y_pos +1)
    if y_plus and x_plus:
        grid[y_pos +1][x_pos +1] = (grid[y_pos +1][x_pos +1][0] + 1, grid[y_pos +1][x_pos +1][1])
        grid = check_flash(grid, x_pos+1, y_pos+1)   

    return grid

def loop_through_add_step(grid):
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            grid[i][j] = (grid[i][j][0] + 1, grid[i][j][1])
            j += 1
        i += 1
        j = 0
    return grid
            
def loop_through_nine_to_zero(grid):
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            if grid[i][j][0] > 9:
                grid[i][j] = (0, False)
            else:
                grid[i][j]= (grid[i][j][0], False) # reset for new step
            j += 1
        i += 1
        j = 0
    return grid

def loop_through_did_all_flash(grid):
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            if grid[i][j][1] == False:
                return False            
            j += 1
        i += 1
        j = 0
    return True

def get_grid_from_str_list(input: list[str]):
    grid = [[0] * len(input) for _ in range(len(input))]
    i = 0
    while i < len(input):
        j = 0
        while j < len(input[i]):
            grid[i][j] = (int(input[i][j]), False)
            j += 1
        i += 1
        j = 0
    return grid


input_path = "inputs\\day11_input.txt"
file_path = helper.get_relative_dir(input_path)
input = helper.get_file_as_list(file_path)
global_count = 0

lowpoints = []
grid = get_grid_from_str_list(input)

#check if lowest, vertical, horizontal, diagonal and reverse diagonal
step = 0
while step < 1000:
    # add 1 to all
    grid = loop_through_add_step(grid)

    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            grid = check_flash(grid, j, i)            
            j += 1
        i += 1
    step += 1

    if loop_through_did_all_flash(grid):
        print(str(step))
        break
    # set > 9 to 0
    grid = loop_through_nine_to_zero(grid)

print("Failed")
