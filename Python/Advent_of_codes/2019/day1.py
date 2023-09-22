with open('day1.txt') as f:
    read_data = f.read().strip().split('\n')

# Part 1
fuels = []
for m in read_data:
    fuels.append(int(m) // 3 - 2)
print(sum(fuels))

# Part 2
def cal_fuel(m, sum=0):
    if m // 3 - 2 <= 0:
        return 0
    m = m // 3 - 2
    return m + cal_fuel(m)


fuels = []
for m in read_data:
    fuels.append(cal_fuel(int(m)))
print(sum(fuels))