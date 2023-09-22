with open("day1_1.txt") as f:
    # Part 1
    read_data = f.read().strip()
    processed_data = [1 if i == '(' else -1 for i in read_data]
    print(sum(processed_data))
    # List comprehension practice
    # Open file, read data, strip white spaces
    # Create a list with '(' is replaced with 1 and ')' is replaced with -1)
    # Sum up the list
    # Part 2
    sum = 0
    for i, j in enumerate(processed_data):
        sum += j
        if sum == -1:
            print(i + 1)
            break
    # Enumerate through processed_data
    # Sum up while keeping track of current index
    # When sum == 0, return current position which is current index + 1


