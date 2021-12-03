import aoc_2021.solutions.helpers as helper

# most common bit in position
def get_most_common_bit(input, check_number, match_most_common):
    count = 0
    rows = len(input)
    for x in input:
        if (x[check_number] == "1"):
            count += 1
            
    if (count >= rows/2):
        if match_most_common:
            return "1"
        else:
            return "0"
    elif (count < rows/2):
        if  match_most_common:
            return "0"
        else:
            return "1"

# returns list of bitsequences matching criteria
def get_rows_matching_criteria(rows, match, i):
    matching_rows = []
    for row in rows:
        if(row[i] == match):
            matching_rows.append(row)
    return matching_rows
        
# returns last reamaining bitsequence matching criteria
def get_list_matching_criteria(input, match_most_common):
    result = input
    for item, bitChar in enumerate(input[0]):
        match = get_most_common_bit(result, item, match_most_common)
        result = get_rows_matching_criteria(result, match, item)
        if len(result) == 1:
            return result[0]

def get_int_from_bit(bit):
    return int(bit, 2)

input_path = "inputs\\day3_1_input.txt"
file_path = helper.get_relative_dir(input_path)
input = helper.get_file_as_list(file_path)

oxygen_rating = get_list_matching_criteria(input, True)
co2_scrubber = get_list_matching_criteria(input, False)

print("Readout is Oxy: " + str(oxygen_rating) + ":" + str(get_int_from_bit(oxygen_rating)) + " CO2: " + str(co2_scrubber) + ":" + str(get_int_from_bit(co2_scrubber)))
print("Result: " + str(get_int_from_bit(oxygen_rating)*get_int_from_bit(co2_scrubber)))