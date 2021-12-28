from typing import List
import helpers as helper
import math

def check_line(line: List[str]):    
    queue = []
    while len(line) > 0:
        match line[0]:
            case '(':
                queue.append(line[0])
            case '[':
                queue.append(line[0])
            case '{':
                queue.append(line[0])
            case '<':
                queue.append(line[0])
            case ')':
                res = queue.pop()
                if res != '(':
                    return None
            case ']':
                if queue.pop() != '[':
                    return None
            case '}':
                if queue.pop() != '{':
                    return None
            case '>':
                if queue.pop() != '<':
                    return None
        line.pop(0)
    return queue

# Turned into queue to skip a step with completing row
def get_score(list):
    count = 0
    while len(list) > 0:
        count = count * 5
        match list.pop():
            case '(':
                count += 1
            case '[':
                count += 2
            case '{':
                count += 3
            case '<':
                count += 4
            case _: 
                return 0
    return count


input_path = "inputs\\day10_input.txt"
file_path = helper.get_relative_dir(input_path)
input = helper.get_file_as_list(file_path)

counts = []
for row in input:
    result = check_line(list(row))
    if result != None:
        # print(result)
        counts.append(get_score(result))

middle = math.floor(len(counts)/2)
counts.sort()
print(str(counts[middle]))