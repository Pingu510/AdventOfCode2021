#TopLeft to Bottom Right, Lowest Risk
import helpers as helper

# read input into matrix
def get_grid_from_str_list(input: list[str]):
    grid = [[0] * len(input) for _ in range(len(input))]
    i = 0
    while i < len(input):
        j = 0
        while j < len(input[i]):
            grid[i][j] = int(input[i][j])
            j += 1
        i += 1
        j = 0
    return grid

def find_neighbor(matrix: list[int], y_pos: int, x_pos: int, danger_count: int, visited: list[int,int]):
    global current_min_count
    danger_count += matrix[y_pos][x_pos]
    size = len(matrix) -1

    # Discard if danger is higher than parent
    if(danger_count > current_min_count):
        return -1

    # No need for double visit paths
    if (y_pos, x_pos) in visited:
        return -1
    visited.append((y_pos, x_pos))

    # Reached end?
    if y_pos == size and x_pos == size:
        if(is_danger_overloaded(danger_count, current_min_count) == False):
            current_min_count = danger_count
            return danger_count
        return -1

    # Right
    if x_pos < size:
        find_neighbor(matrix, y_pos, x_pos + 1, danger_count, visited)
    # Down
    if y_pos < size:
        find_neighbor(matrix, y_pos + 1, x_pos, danger_count, visited)
    # Left
    if x_pos - 1 >= 0:
        find_neighbor(matrix, y_pos, x_pos - 1, danger_count, visited)
    # Up
    if y_pos - 1 >= 0:
        find_neighbor(matrix, y_pos - 1, x_pos, danger_count, visited)

    return -1

# Compare current path count with previous least dangerous path count
def is_danger_overloaded(current: int, least_dangerous_ancestor: int):
    if (current > least_dangerous_ancestor):
        return True
    return False

# testinput count = 40

input = []
current_min_count = 49

input_path = "inputs\\day15_test_input.txt"
file_path = helper.get_relative_dir(input_path)
input = helper.get_file_as_list(file_path)
global_count = 0

lowpoints = []
grid = get_grid_from_str_list(input)

# result = navigate_through_dangerzone(grid,0,0,current_min_count)

result = find_neighbor(grid, 0, 0, 0, [])
print(str(current_min_count - grid[0][0]))