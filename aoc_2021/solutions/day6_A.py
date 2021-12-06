import helpers as helper

def total_lanternfish(lanternfishes :list[int]):
    sum = 0
    for fish in lanternfishes:
        sum += fish
    return sum

input_path = "inputs\\day6_1_input.txt"
file_path = helper.get_relative_dir(input_path)
with open(file_path) as file:
    input = file.read().split(",")

integer_map = map(int, input)
input = list(integer_map)
# input = [3,4,3,1,2]
lanternfish = [0,0,0,0,0,0,0,0,0]

# read input to list
i = 0
while i <= 8:
    lanternfish[i] = input.count(i)
    i += 1

print(str(lanternfish))

# itterate days
days = 0
while days < 80:
    days += 1
    # get zeros
    zeroes = lanternfish[0]        
    i = 0  
    while i < 8:
        # shift spwan days
        i += 1
        lanternfish[i-1] = lanternfish[i]        
    lanternfish[6] += zeroes    
    lanternfish[8] = zeroes

print(str(lanternfish))
print("Result: " + str(total_lanternfish(lanternfish)))