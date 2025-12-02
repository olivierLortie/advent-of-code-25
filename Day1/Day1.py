filename = "Data1.txt"

def Day1_1():
    total = 50
    password = 0

    with open(filename) as file:
        for line in file:
            instruction = line.rstrip()[0:1]
            number = int(line.rstrip()[1:])

            if (instruction == "L"):
                total -= number
            else:
                total += number

            total = total%100

            if (total == 0):
                password += 1

    return password

def Day1_2():
    total = 50
    password = 0

    with open(filename) as file:
        for line in file.readlines():
            instruction = line.rstrip()[0:1]
            number = int(line.rstrip()[1:])

            if instruction == "L":
                if number >= total:
                    password += (1 + int((number - total) / 100))
                    if total == 0:
                        password -= 1
                total -= number
            else:
                if number >= (100 - total):
                    password += (1 + int((number - 100 + total) / 100))
                total += number

            total = total%100

    return password

def Day1_2_methode_bs():
    total = 50
    password = 0

    with open(filename) as file:
        for line in file.readlines()[0:500]:
            instruction = line.rstrip()[0:1]
            number = int(line.rstrip()[1:])

            if instruction == "L":
                for i in range(number):
                    total -= 1
                    total = total%100
                    if total == 0:
                        password += 1
            else:
                for i in range(number):
                    total += 1
                    total = total%100
                    if total == 0:
                        password += 1
            
            print(instruction +  str(number) + " - "  + str(total) + " - " + str(password))

    return password


print(Day1_2())