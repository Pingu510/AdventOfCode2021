import helpers as helper

# Count sum risklevel
def count_risk_level_sum(risklevels : list[int]):
    sum = 0
    for risklevel in risklevels:
        sum += risklevel
    return sum

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

#check if lowest, vertical, horizontal, diagonal and reverse diagonal
i = 0
while i < len(input):
    j = 0
    while j < len(input[i]):
        if(is_lowpoint(input, i, j)):
            #if lovest point of adjacent numbers, add to lowpoints
            lowpoints.append(int(input[i][j]) + 1)
        j += 1
    i += 1

print(str(lowpoints))
print(str(count_risk_level_sum(lowpoints)))