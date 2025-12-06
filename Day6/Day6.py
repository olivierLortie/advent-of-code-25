filename = "input.txt"

def Day6_1():
    total = 0
    problems = []

    with open(filename) as file:
        for line in file:
            values = line[0:-1].split(" ") # remove \n at the end
            values = [item for item in values if item.strip()] # remove all empty spaces
            problems.append(values)

    problems = [list(row) for row in zip(*problems)] # transpose matrix

    for problem in problems:
        operation = problem[-1]
        problem_total = int(problem[0])
        for val in problem[1:-1]: # remove first and last value
            if operation == "+":
                problem_total += int(val)
            elif operation == "*":
                problem_total *= int(val)
        
        total += problem_total

    return total

def Day6_2():
    total = 0
    problems = []

    with open(filename) as file:
        for i, line in enumerate(file):
            problems.append([])
            for c in line:
                if c == " " or c == "\n":
                    c = ""
                problems[i].append(c)

    problems = [list(row) for row in zip(*problems)] # transpose matrix
    #problems.append([""] * len(problems[0])) # add empty characters at ther end of the file

    new_problem = True
    current_val = 0
    current_operation = "+" # default value
    problem_val = 0
    for i, row in enumerate(problems):
        if "".join(row) == "" or i is len(problems) - 1: # new problem to solve
            new_problem = True
            print(problem_val)
            total += problem_val
            continue

        if new_problem:
            current_operation = row[-1]
            current_val = int("".join(row[:-1]))
            problem_val = current_val
            new_problem = False
            continue
        else:
            current_val = int("".join(row))

        if current_operation == "+":
            problem_val += current_val
        elif current_operation == "*":
            problem_val *= current_val
        
    return total

print(Day6_2())