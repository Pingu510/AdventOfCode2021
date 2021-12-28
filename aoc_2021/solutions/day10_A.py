from typing import List
import helpers as helper

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
                    return line[0]
            case ']':
                if queue.pop() != '[':
                    return line[0]
            case '}':
                if queue.pop() != '{':
                    return line[0]
            case '>':
                if queue.pop() != '<':
                    return line[0]
        line.pop(0)
        if len(queue) == 0:
            return None
    return None

def get_score(char):
    match char:
        case ')':
            return 3
        case ']':
            return 57
        case '}':
            return 1197
        case '>':
            return 25137
        case _: 
            return 0

                    

def get_highscore(score: list[int]):
    sum = 0
    sum += score[0] * 3 # ): 3 points
    sum += score[1] * 57 # ]: 57 points
    sum += score[2] * 1197 # }: 1197 points
    sum += score[3] * 25137 # >: 25137 points
    return sum

input_path = "inputs\\day10_input.txt"
file_path = helper.get_relative_dir(input_path)
input = helper.get_file_as_list(file_path)

count = 0
for row in input:
    result = check_line(list(row))
    print(result)
    count += get_score(result)

print(str(count))