def hello_me():
    return "Hello"

def get_increases(input):
    count = 0
    i = 0
    while i < len(input) -1:
        if int(input[i]) < int(input[i+1]):
            count += 1
        i += 1
    return count

msg = "Hello Word!"
print(msg)

input_test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

import helpers
input_path = "inputs\day1_1_input.txt"
file_path = helpers.get_relative_dir(input_path)
input = helpers.get_file_as_list(file_path)

count = get_increases(input)
print("Number of increases: " + str(count))