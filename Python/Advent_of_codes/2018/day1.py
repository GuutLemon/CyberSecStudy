with open('day1.txt') as f:
    read_data = f.read().strip().split('\n')
    processed_data = [int(i) for i in read_data]

print(sum(processed_data))
freq = set()
sum = 0
while True:
    for i in processed_data:
        sum += i
        if sum in freq:
            print(sum)
            exit(0)
        freq.add(sum)
