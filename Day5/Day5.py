filename = "input3.txt"

def Day5_1():
    total = 0
    finished_parsing_ids = False
    ids_sequences = []

    with open(filename) as file:
        for line in file:
            if line == "\n":
                finished_parsing_ids = True
            elif finished_parsing_ids:
                id = int(line)
                for id_sequence in ids_sequences:
                    bounds = id_sequence.split("-")
                    min = int(bounds[0])
                    max = int(bounds[1])

                    if id > min and id <= max:
                        print("id " + str(id) + " is fresh")
                        total = total + 1
                        break

            else:
                ids_sequences.append(line)

    return total

def Day5_2():
    total = 0
    sequences = [[0] * 2]

    with open(filename) as file:
        for line in file:
            bounds = line.split("-")
            min = int(bounds[0])
            max = int(bounds[1])

            sequences.append([min, max])

    sequences.pop(0)
    sequences.sort()

    last_id = 0
    for sequence in sequences:
        if sequence[0] <= last_id:
            sequence[0] = last_id + 1

        if sequence[0] <= sequence[1]:
            last_id = sequence[1]

    for sequence in sequences:
        if sequence[1] >= sequence[0]:
            total += 1 + sequence[1] - sequence[0]

    print(sequences)

    return total

print(Day5_2())