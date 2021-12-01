def get_average_increase(input):
    count = 0
    i = 0
    while i < (len(input) -3):
        num1 = int(input[i]) + int(input[i+1]) + int(input[i+2])
        num2 = int(input[i+1])+ int(input[i+2]) + int(input[i+3])
        if num1 < num2:
            count += 1
        i += 1
    return count

import helpers
inputfile = "inputs\day1_1_input.txt"
file_path = helpers.get_relative_dir(inputfile)

with open(file_path) as file:
    input = [line.strip() for line in file]
count = get_average_increase(input)

print("Number of increases: " + str(count))