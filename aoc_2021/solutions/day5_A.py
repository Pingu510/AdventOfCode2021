import helpers as helper
import re
from collections import Counter

def count_intersects_in_grid(grid: list[list[int]], grid_size: int):
    count = 0 
    for row in grid:
        c = Counter(row)
        count += grid_size -(c[0] + c[1])
    return count

def insert_coordinate_list_to_grid(line_coordinates, grid: list[list[int]]):
    for coordinate in line_coordinates:
        grid[int(coordinate[1])][int(coordinate[0])] = grid[int(coordinate[1])][int(coordinate[0])] + 1
    return

def get_line_coordinates(start_x: int, start_y: int, end_x: int, end_y: int):
    line_coordinates = [(start_x, start_y)]
    current_x = start_x
    current_y = start_y
    # diagonal check
    if not(start_x == end_x or start_y == end_y):
        return

    while(True):
        if(end_x > current_x):
            current_x += 1
        elif(end_x < current_x):
            current_x -=1
        if(end_y > current_y):
            current_y +=1
        elif(end_y < current_y):
            current_y -= 1
        line_coordinates.append((current_x, current_y))
        if(current_x == end_x and current_y == end_y):
            return line_coordinates

def read_coordinates_from_row(row: str): #0,9 -> 5,9
    row_split = re.split(r",|\s+",row)
    return [ int(row_split[0]), int(row_split[1]), int(row_split[-2]), int(row_split[-1]) ]
    

def make_grid(size):
    return [[0] * size for _ in range(size)]

def print_grid(grid):
    for row in grid:
        print(row)



grid_size = 1000
grid = make_grid(grid_size)

input_path = "inputs\\day5_1_input.txt"
file_path = helper.get_relative_dir(input_path)
input = helper.get_file_as_list(file_path)

for row in input:
    coordinates = read_coordinates_from_row(row)
    coordinate_line_list = get_line_coordinates(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
    if(coordinate_line_list != None):
        insert_coordinate_list_to_grid(coordinate_line_list, grid)


print("Result: " + str(count_intersects_in_grid(grid,  grid_size)))
# print_grid(grid)