import helpers as helper

def pmedian(sortedLst):
    lstLen = len(sortedLst)
    index = (lstLen - 1) // 2
   
    if (lstLen % 2):
        return sortedLst[index]
    else:
        print(str(sortedLst[index]) + " " + str(sortedLst[index+1]))
        return sortedLst[index]
        # return (sortedLst[index] + sortedLst[index + 1])/2.0

def count_moves(numbers, target_number):
    sum = 0
    i = 0
    while i < len(numbers):
        if(numbers[i] < target_number):
            sum += target_number - numbers[i]
        elif(numbers[i] > target_number):
            sum += -(target_number - numbers[i])
        i += 1
    return sum

input_path = "inputs\\day7_1_input.txt"
file_path = helper.get_relative_dir(input_path)
input = helper.get_file_as_list(file_path)
numbers = list[int](input[0].split(','))
integer_map = map(int, numbers)
numbers = sorted(list(integer_map))
# numbers = sorted([16,1,2,0,4,2,7,1,2,14])

med = pmedian(numbers)
sum = count_moves(numbers, med)
print(str(sum))

# for item in numbers:
#     sum += item
# print(str(sum/len(numbers)))
# List = [2, 1, 2, 2, 1, 3]