import aoc_2021.solutions.helpers as helper


def get_average_increase(input:int):
    count = 0
    i = 0
    while i < (len(input) -3):
        num1 = input[i] + input[i+1] + input[i+2]
        num2 = input[i+1]+ input[i+2] + input[i+3]
        if num1 < num2:
            count += 1
        i += 1
    return count

input_path = "inputs\\day1_1_input.txt"
file_path = helper.get_relative_dir(input_path)
input = helper.get_file_as_list(file_path)

count = get_average_increase(input)

print("Number of increases: " + str(count))