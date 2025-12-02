filename = "input.txt"

def Day2_1():
    result = 0

    with open(filename) as file:
        line = file.readlines()[0]
        sequences = line.split(",")

        for sequence in sequences:
            bounds = sequence.split("-")
            min = int(bounds[0])
            max = int(bounds[1])

            for id in range(min, max + 1):
                id_string = str(id)
                id_len = len(id_string)
                if id_len%2 == 0:
                    first = id_string[0:int(id_len/2)]
                    second = id_string[int(id_len/2):]

                    if first == second:
                        result += id
                        print("removing : " + str(id))
        
    return result

def are_all_items_same_set(my_list):
    if not my_list:  # Handle empty list case
        return True
    return len(set(my_list)) == 1

def Day2_2():
    result = 0

    with open(filename) as file:
        line = file.readlines()[0]
        sequences = line.split(",")

        for sequence in sequences:
            bounds = sequence.split("-")
            min = int(bounds[0])
            max = int(bounds[1])

            for id in range(min, max + 1):
                id_string = str(id)
                id_len = len(id_string)
                x = 2
                while int(id_len / x) > 0:
                    if id_len%x == 0:
                        chunk_len = int(id_len / x)
                        chunks = [id_string[i:i+chunk_len] for i in range(0, id_len, chunk_len)]
                        if are_all_items_same_set(chunks):
                            result += id
                            x = 1000 # break out of the while
                            print("removing : " + id_string)
                    
                    x += 1
        
    return result

print(Day2_2())