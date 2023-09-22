with open('day2.txt') as f:
    read_data = f.read().strip().split('\n')

# Part 1
count_2 = 0
count_3 = 0
for i in read_data:
    letters = set(list(i))
    two = False
    three = False
    for letter in letters:
        if i.count(letter) == 2:
            two = True
        elif i.count(letter) == 3:
            three = True
    count_2 += two
    count_3 += three
print(count_2 * count_3)

# Part 2
for i in range(len(read_data) - 1):
    for j in range(i + 1, len(read_data)):
        difference = []
        for k in range(len(read_data[i])):
            if read_data[i][k] != read_data[j][k]:
                difference.append(read_data[i][k])
        if len(difference) == 1:
            result = read_data[i]
            result = result.replace(difference[0], '')
            print(result)
            exit(0)
