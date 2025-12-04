filename = "input.txt"

def build_array():
    with open(filename) as file:
        lines = file.readlines()
        nb_lines = len(lines) + 2 # add padding
        line_len = len(lines[0]) + 1 #remove \n and add 2 for padding

        arr = [0] * nb_lines * line_len # flat array

        for i, line in enumerate(lines):
            for j, c in enumerate(line[0:-1]): #remove \n character
                arr[(i + 1) * line_len + (j + 1)] = 1 if c == "@" else 0

    return nb_lines, line_len, arr

def remove_rolls(line_len, input_array):
    rolls_removed = 0
    output_array = input_array

    pos_to_check = [-line_len - 1, -line_len, -line_len + 1, -1, 1, + line_len - 1, + line_len, + line_len + 1]

    for i, val in enumerate(input_array):
        nb_adjacents = 0
        if val == 1:
            for pos_delta in pos_to_check:
                if input_array[i + pos_delta] == 1:
                    nb_adjacents += 1

            if nb_adjacents < 4:
                output_array[i] = 0
                rolls_removed = rolls_removed + 1

    return rolls_removed, output_array


def Day4_1():
    total = 0
    nb_lines, line_len, input_array = build_array()

    pos_to_check = [-line_len - 1, -line_len, -line_len + 1, -1, 1, + line_len - 1, + line_len, + line_len + 1]

    for i, val in enumerate(input_array):
        nb_adjacents = 0
        if val == 1:
            for pos_delta in pos_to_check:
                if input_array[i + pos_delta] == 1:
                    nb_adjacents += 1

            if nb_adjacents < 4:
                total = total + 1

    return total

def Day4_2():
    total = 0
    nb_lines, line_len, input_array = build_array()

    rolls_removed = 0

    while True:
        current_rolls_removed, input_array = remove_rolls(line_len, input_array)
        
        rolls_removed = rolls_removed + current_rolls_removed

        if current_rolls_removed == 0:
            break

    return rolls_removed

print(Day4_2())

