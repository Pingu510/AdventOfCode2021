import helpers as helper

def get_three_largest_basins(basins:list[(int,int)]):
    toplist = [0, 0, 0]
    i = 0 
    while i < len(basins):
        if min(toplist) < len(basins[i]):
            index = toplist.index(min(toplist))
            toplist[index] = len(basins[i])
        i += 1
    return toplist[0] * toplist[1] * toplist[2]

def find_neighbor(matrix: list[str], x_pos: int, y_pos: int, basins: list[(int, int)]):
    if((x_pos,y_pos) in basins):
        return
    if int(matrix[y_pos][x_pos]) < 9:
        basins.append((x_pos, y_pos))
    if int(matrix[y_pos][x_pos]) == 9:
        return basins

    if x_pos + 1 < len(matrix[0]) and int(matrix[y_pos][x_pos + 1]) != 9:
        find_neighbor(matrix, x_pos + 1, y_pos, basins)
    if x_pos - 1 >= 0 and int(matrix[y_pos][x_pos - 1]) != 9:
        find_neighbor(matrix, x_pos - 1, y_pos, basins)
    if y_pos + 1 < len(matrix) and int(matrix[y_pos + 1][x_pos]) != 9:
        find_neighbor(matrix, x_pos, y_pos + 1, basins)
    if y_pos - 1 >= 0 and int(matrix[y_pos - 1][x_pos]) != 9:
        find_neighbor(matrix, x_pos, y_pos - 1, basins)    
    return basins

def is_lowpoint_horizontal(row: list[str], pos: int):
    is_lowpoint = True
    if(pos - 1 >= 0 and int(row[pos - 1]) <= int(row[pos])):
        is_lowpoint = False
    if(pos + 1 < len(row) and int(row[pos + 1]) <= int(row[pos])):
        is_lowpoint = False
    return is_lowpoint

def is_lowpoint_vertical(list, list_index, list_position_index):
    is_lowpoint = True
    if list_index - 1 >= 0:
        if int(list[list_index - 1][list_position_index]) <= int(list[list_index][list_position_index]):
            is_lowpoint = False
    if list_index + 1 < len(list):        
        if int(list[list_index + 1][list_position_index]) <= int(list[list_index][list_position_index]):
            is_lowpoint = False
    return is_lowpoint

def is_lowpoint(list, list_index, list_position_index):
    if(is_lowpoint_horizontal(list[list_index], list_position_index) == False or is_lowpoint_vertical(list, list_index, list_position_index) == False):
        return False
    else:
        return True

input_path = "inputs\\day9_1_input.txt"
file_path = helper.get_relative_dir(input_path)
input = helper.get_file_as_list(file_path)

lowpoints = []
all_basins = []
#check if lowest, vertical, horizontal, diagonal and reverse diagonal
i = 0
while i < len(input):
    j = 0
    while j < len(input[i]):
        basin = []
        if(is_lowpoint(input, i, j)):
            #if lovest point of adjacent numbers, add to lowpoints
            lowpoints.append(int(input[i][j]) + 1)
            basin = find_neighbor(input, j, i, [])
            all_basins.append(list(basin))        
        j += 1
    i += 1

largest_basins = get_three_largest_basins(all_basins)
print(str(largest_basins))