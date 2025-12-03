filename = "input.txt"

def Day3_1():
    total = 0

    with open(filename) as file:
        for line in file:
            first_digit_index = 0
            first_digit = 0
            second_digit = 0

            for i, c in enumerate(line[0:-1]): # remove the last character (\n)
                digit = int(c)

                if digit > first_digit:
                    first_digit = digit
                    first_digit_index = i

                if first_digit == 9 or i == len(line) - 3: # -1 for the index that starts at 0, -1 for removing \n, -1 because we want the second last index
                    break

            for i, c in enumerate(line[first_digit_index + 1:-1]): # remove the last character (\n)
                digit = int(c)

                if digit > second_digit:
                    second_digit = digit

            number = first_digit * 10 + second_digit
            print(number)
            total = total + number

    return total

def Day3_2(n):
    total = 0

    with open(filename) as file:
        for line in file:
            digit_array = [0] * n
            found_index = 0
            number = 0

            for current_digit in range(n):
                start_index = 0 if current_digit == 0 else found_index + 1
                for i, c in enumerate(line[start_index:-n + current_digit]):
                    digit = int(c)

                    if digit > digit_array[current_digit]:
                        digit_array[current_digit] = digit
                        found_index = i + start_index

                number = number + digit_array[current_digit] * pow(10, (n - 1 - current_digit))
            
            print(number)
            total = total + number

    return total


print(Day3_2(12))
    
