import aoc_2021.solutions.helpers as helper


def get_increases(input:int):
    count = 0
    i = 0
    while i < len(input) -1:
        if input[i] < input[i+1]:
            count += 1
        i += 1
    return count

input_path = "inputs\\day1_1_input.txt"
file_path = helper.get_relative_dir(input_path)
input = helper.get_file_as_list(file_path)

count = get_increases(input)
print("Number of increases: " + str(count))