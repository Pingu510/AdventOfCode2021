from typing import List
import helpers as helper

def calculate_board(bingo_board: list, winning_number: int):
    sum = 0
    for row in bingo_board:
        for number in row:
            if(number[1] == False):
                sum += int(number[0])
    return sum * winning_number


def find_number_in_bingo_board(grid: list[list[int, tuple]], number):
    board_index = 0
    hit = -1
    while board_index < len(grid):
        try:
            hit = grid[board_index].index((number, False))
        except ValueError:   
            None
        if(hit != -1):
            grid[board_index][hit] = (number, True)
            #check for 5 in row 
            lisat = []
            i = 0
            while i < len(grid):
                lisat.append(grid[i][hit])
                i += 1
            if(check_tuple_list_for_bool(grid[board_index]) or check_tuple_list_for_bool(lisat)):
                return grid
            hit = -1
        board_index += 1
    return None

def check_tuple_list_for_bool(bingo_row: list[int, tuple]):
    for tup in bingo_row:
        if(tup[1] == False):
            return False
    return True

def get_bingo_row_from_str_list(numbers: list[str]):
    bingo_row = []
    for num in numbers:
        bingo_row.append((int(num), False))
    return bingo_row

def read_numbers_from_row(row: str):
    row_split = row.split()
    return row_split
    

def make_grid(size):
    return [[0] * size for _ in range(size)]

def print_grid(grid):
    for row in grid:
        print(row)


input_path = "inputs\\day4_1_numbers.txt"
file_path = helper.get_relative_dir(input_path)
input_numbers = helper.get_file_as_list(file_path)
numbers = input_numbers[0].split(',')

input_path = "inputs\\day4_1_bingo.txt"
file_path = helper.get_relative_dir(input_path)
input_bingo = helper.get_file_as_list(file_path)


grid_size = 5
grid = make_grid(grid_size)
board_index = 0
total_index = 0
bingo_boards = [grid]

# make bingo boards
for input_row in input_bingo:
    if(input_row == ""):
        bingo_boards.append(make_grid(grid_size))
        total_index += 1
        board_index = 0
        continue
    row = read_numbers_from_row(input_row)
    current_board = bingo_boards[total_index]
    current_board[board_index] = get_bingo_row_from_str_list(row)
    board_index += 1

# draw sequence
finished = False
number_index = 0
while (number_index < len(numbers) and finished != True):
    for board in bingo_boards:
        # insert number into board and calculate adjecent True
        # if adjecent > 4 = BINGO
        winner = find_number_in_bingo_board(board, int(numbers[number_index]))
        if(winner != None):
            #for bingo calculate sum of all False * last number
            result = calculate_board(winner, int(numbers[number_index]))
            print("Final score: " + str(result))
            finished = True
