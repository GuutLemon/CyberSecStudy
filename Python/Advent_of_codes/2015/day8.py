with open("day8.txt") as f:
    read_data = f.read().strip().split("\n")
    sum_literal = sum([len(i) for i in read_data])
    string_values = []

    # Part 1
    for i in read_data:
        string_values.append(eval(i))       # Run the line as code
    sum_string_values = sum([len(i) for i in string_values])
    print(sum_literal - sum_string_values)

    # Part 2
    # Brute force
    string_encoded = []
    for i in read_data:
        i = i.replace('\\', '\\\\').replace('"', '\\"')
        i = '"' + i + '"'
        print(i)
        string_encoded.append(i)
    sum_string_encoded = sum([len(i) for i in string_encoded])
    print(string_encoded)
    print(sum_string_encoded - sum_literal)
