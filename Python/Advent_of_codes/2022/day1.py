with open('day1.txt') as f:
    read_data = f.read().strip().split('\n\n')
    processed_data = [[int(j) for j in i.split('\n')] for i in read_data]
    print(processed_data)


# Part 1
print(max([sum(i) for i in processed_data]))

# Part 2
print(sum(sorted([sum(i) for i in processed_data])[-3:]))