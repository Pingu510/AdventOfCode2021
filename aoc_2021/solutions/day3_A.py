# import aoc_2021.solutions.helpers as helper
import helpers as helper

def get_gamma(input):    
    gamma = input[0]
    i = 0
    for item, bitChar in enumerate(input[0]): 
        gamma = gamma[:i] + str(get_highest_bit(input, i)) + gamma[i + 1:]
        i += 1
        
    return gamma

def get_highest_bit(input, check_number):
    print("counting")
    count = 0
    rows = len(input)
    for x in input:
        if (x[check_number] == "1"):
            count += 1
            if count > rows/2:
                return 1

    return 0
        
def get_epsilon_from_gamma(gamma):
    return "110011101111" # todo invert properly

def get_int_from_bit(bit):
    return int(bit, 2)

input_path = "inputs\\day3_1_input.txt"
file_path = helper.get_relative_dir(input_path)
input = helper.get_file_as_list(file_path)

gamma = get_gamma(input)
epsilon = get_epsilon_from_gamma(gamma)

print("Readout is Gamma: " + str(gamma) + ":" + str(get_int_from_bit(gamma)) + " Epsilon: " + str(epsilon) + ":" + str(get_int_from_bit(epsilon)))
print("Result: " + str(get_int_from_bit(gamma)*get_int_from_bit(epsilon)))