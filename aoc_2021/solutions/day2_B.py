import aoc_2021.solutions.helpers as helper


def get_resulting_position(input):
    aim = 0
    horizontal = 0
    vertical = 0
    for heading in input:
        movement = str(heading).split(" ")
        match movement[0]:
            case "forward":
                horizontal += int(movement[1])
                vertical += aim * int(movement[1])
            case "up":
                aim -= int(movement[1])
            case "down":
                aim += int(movement[1])
    return horizontal * vertical

input_path = "inputs\\day2_1_input.txt"
file_path = helper.get_relative_dir(input_path)
input = helper.get_file_as_list(file_path)

result = get_resulting_position(input)
print("Final position is: " + str(result))