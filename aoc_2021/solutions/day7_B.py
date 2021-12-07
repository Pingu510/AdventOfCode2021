import helpers as helper
import decimal

def count_moves(numbers, target_number):
    sum = 0
    i = 0
    while i < len(numbers):
        if(numbers[i] < target_number):
            steps = target_number - numbers[i]
            sum += (steps*(steps + 1))/2
        elif(numbers[i] > target_number):
            steps = -(target_number - numbers[i])
            sum += (steps*(steps + 1))/2
        i += 1
    return sum

input_path = "inputs\\day7_1_input.txt"
file_path = helper.get_relative_dir(input_path)
input = helper.get_file_as_list(file_path)
numbers = list[int](input[0].split(','))
integer_map = map(int, numbers)
numbers = sorted(list(integer_map))
#numbers = sorted([16,1,2,0,4,2,7,1,2,14])

target = 0
for item in numbers:
    target += item
split = target/len(numbers)
decimal.getcontext().rounding = decimal.ROUND_HALF_DOWN
target = decimal.Decimal(split).to_integral_value()
# target = round(split)

sum = count_moves(numbers, target)
print(str(sum))

#guess = 88612611