def get_resulting_position(input):
    horizontal = 0
    vertical = 0
    for heading in input:
        movement = str(heading).split(" ")
        match movement[0]:
            case "forward":
                horizontal += int(movement[1])
            case "up":
                vertical -= int(movement[1])
            case "down":
                vertical += int(movement[1])
    return horizontal * vertical

test_input = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

import helpers
input_path = "inputs\day2_1_input.txt"
file_path = helpers.get_relative_dir(input_path)
input = helpers.get_file_as_list(file_path)

result = get_resulting_position(input)
print("Final position is: " + str(result))